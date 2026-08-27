#!/usr/bin/env python3
"""Собирает юридическое заключение в .docx на фирменном шаблоне.

Читает текстовый исходник (см. references/outline-format.md) и подставляет его
в assets/template.docx, сохраняя стили, шапку, колонтитулы и автонумерацию
Word. Нумерация пунктов (1, 1.1, (a), (i)) и приложений («Приложение 1»)
проставляется самим Word из стилей шаблона — в исходнике номера не пишутся.

Зависимостей нет, только стандартная библиотека.

    python render_opinion.py заключение.md -o Заключение_ООО_Ромашка.docx
"""

from __future__ import annotations

import argparse
import copy
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
w = lambda tag: f"{{{W}}}{tag}"  # noqa: E731

XML_DECL = b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n'
ROOT_TAG_RE = re.compile(rb"<(\w+:?\w*)\b[^>]*>")

# Разметка исходника -> стиль абзаца в шаблоне.
HEADING_STYLES = {1: "SBLL1", 2: "SBLL2", 3: "SBLL3", 4: "SBLL4", 5: "SBLL5", 6: "SBLL6"}

# Ключи шапки: русские и английские варианты пишутся одинаково в результат.
META_ALIASES = {
    "наименование": "to_name", "адресат": "to_name", "to_name": "to_name",
    "адрес": "to_address", "to_address": "to_address",
    "сокращение": "to_short", "to_short": "to_short",
    "дата": "date", "date": "date",
    "кас": "re", "касательно": "re", "re": "re",
    "подпись": "closing", "closing": "closing",
}


class OutlineError(Exception):
    """Ошибка в исходнике — сообщается юристу с номером строки."""


# --------------------------------------------------------------------------
# Работа с OOXML-частями
# --------------------------------------------------------------------------

def register_namespaces(xml_bytes: bytes) -> None:
    """Регистрирует префиксы ровно так, как их объявил Word.

    Без этого ElementTree переименует mc: в ns1: и т.п., и ссылки вида
    mc:Ignorable="w14 wp14" укажут на необъявленные префиксы.
    """
    header = xml_bytes[:4000].decode("utf-8", errors="ignore")
    for prefix, uri in re.findall(r'xmlns:(\w+)="([^"]+)"', header):
        ET.register_namespace(prefix, uri)


def check_styles(styles_xml: bytes) -> None:
    """Проверяет, что в шаблоне есть все стили, которыми мы размечаем текст.

    Если фирма обновит шаблон и переименует стили, лучше упасть с внятным
    сообщением, чем отдать юристу документ с потерянной нумерацией.
    """
    root = ET.fromstring(styles_xml)
    present = {s.get(w("styleId")) for s in root.findall(w("style"))}
    required = set(HEADING_STYLES.values()) | {"BodyText", "BodyText2", "SBLSchL1"}
    missing = sorted(required - present)
    if missing:
        raise OutlineError(
            "в шаблоне отсутствуют стили: " + ", ".join(missing) +
            ". Похоже, шаблон изменился — сверьтесь с references/outline-format.md"
        )


def serialize_part(root: ET.Element, original: bytes) -> bytes:
    """Сериализует часть документа, сохраняя корневой тег оригинала дословно.

    Word объявляет в корне десятки пространств имён и перечисляет часть из них
    в mc:Ignorable. ElementTree выводит только фактически использованные, и
    документ перестаёт открываться. Поэтому корневой тег берём из оригинала.
    """
    original_root = ROOT_TAG_RE.search(original)
    generated = ET.tostring(root, encoding="utf-8")
    generated_root = ROOT_TAG_RE.search(generated)
    if original_root is None or generated_root is None:
        return XML_DECL + generated
    return XML_DECL + generated[:generated_root.start()] + original_root.group(0) + \
        generated[generated_root.end():]


# --------------------------------------------------------------------------
# Разбор исходника
# --------------------------------------------------------------------------

def parse_outline(text: str) -> tuple[dict, list[dict]]:
    meta: dict[str, str] = {}
    blocks: list[dict] = []

    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.rstrip()
        if not line.strip():
            continue

        if line.lstrip().startswith("@@"):
            body = line.lstrip()[2:].strip()
            kind, _, value = body.partition(" ")
            kind = kind.lower()
            value = value.strip()
            if kind in ("schedule", "приложение"):
                blocks.append({"kind": "schedule", "text": value, "lineno": lineno})
            elif kind in ("part", "часть"):
                blocks.append({"kind": "part", "text": value, "lineno": lineno})
            elif kind in ("pagebreak", "разрыв"):
                blocks.append({"kind": "pagebreak", "lineno": lineno})
            else:
                raise OutlineError(f"строка {lineno}: неизвестная команда @@{kind}")
            continue

        if line.startswith("@"):
            key, sep, value = line[1:].partition(":")
            if not sep:
                raise OutlineError(f"строка {lineno}: ожидался формат @ключ: значение")
            key = key.strip().lower()
            if key not in META_ALIASES:
                raise OutlineError(
                    f"строка {lineno}: неизвестный ключ шапки @{key}; "
                    f"допустимы: {', '.join(sorted(set(META_ALIASES)))}"
                )
            meta[META_ALIASES[key]] = value.strip()
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            blocks.append({"kind": "heading", "level": level, "text": m.group(2).strip(),
                           "lineno": lineno})
            continue

        m = re.match(r"^(>{1,2})\s+(.*)$", line)
        if m:
            style = "BodyText" if len(m.group(1)) == 1 else "BodyText2"
            blocks.append({"kind": "body", "style": style, "text": m.group(2).strip(),
                           "lineno": lineno})
            continue

        m = re.match(r"^(-{1,2})\s+(.*)$", line)
        if m:
            blocks.append({"kind": "item", "ilvl": len(m.group(1)) - 1,
                           "text": m.group(2).strip(), "lineno": lineno})
            continue

        raise OutlineError(
            f"строка {lineno}: не распознан маркер абзаца.\n"
            f"  {line[:70]}\n"
            "  Ожидается # / ## / ### (пункты), > (абзац без номера), "
            "- (пункт перечня), @@приложение, @ключ: значение."
        )

    return meta, blocks


# --------------------------------------------------------------------------
# Сборка XML
# --------------------------------------------------------------------------

def make_run(text: str, bold: bool = False) -> ET.Element:
    run = ET.Element(w("r"))
    if bold:
        rpr = ET.SubElement(run, w("rPr"))
        ET.SubElement(rpr, w("b"))
    t = ET.SubElement(run, w("t"))
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return run


def make_paragraph(text: str = "", style: str | None = None, num_id: int | None = None,
                   ilvl: int = 0, keep_lines: bool = False,
                   page_break: bool = False) -> ET.Element:
    p = ET.Element(w("p"))
    if style or num_id is not None or keep_lines:
        ppr = ET.SubElement(p, w("pPr"))
        if style:
            ET.SubElement(ppr, w("pStyle")).set(w("val"), style)
        if keep_lines:
            ET.SubElement(ppr, w("keepLines"))
        if num_id is not None:
            numpr = ET.SubElement(ppr, w("numPr"))
            ET.SubElement(numpr, w("ilvl")).set(w("val"), str(ilvl))
            ET.SubElement(numpr, w("numId")).set(w("val"), str(num_id))
    if page_break:
        br_run = ET.SubElement(p, w("r"))
        ET.SubElement(br_run, w("br")).set(w("type"), "page")
    for chunk, bold in split_bold(text):
        if chunk:
            p.append(make_run(chunk, bold))
    return p


def split_bold(text: str) -> list[tuple[str, bool]]:
    """**жирный** -> отдельные прогоны. Всё остальное остаётся как есть."""
    parts: list[tuple[str, bool]] = []
    for i, chunk in enumerate(re.split(r"\*\*(.+?)\*\*", text, flags=re.S)):
        parts.append((chunk, i % 2 == 1))
    return parts


# --------------------------------------------------------------------------
# Нумерация перечней в приложениях
# --------------------------------------------------------------------------

class NumberingPool:
    """Выдаёт новый экземпляр нумерованного списка для каждого перечня.

    Перечни документов в разных приложениях/частях должны начинаться с 1.
    В OOXML это отдельный <w:num>, ссылающийся на тот же abstractNum, с
    принудительным startOverride — иначе второй перечень продолжит первый.
    """

    #: numId перечня документов в шаблоне — образец, у которого берём abstractNum
    SOURCE_NUM_ID = "17"

    def __init__(self, numbering_root: ET.Element):
        self.root = numbering_root
        self.abstract_id = None
        max_id = 0
        for num in self.root.findall(w("num")):
            nid = num.get(w("numId"))
            if nid and nid.isdigit():
                max_id = max(max_id, int(nid))
            if nid == self.SOURCE_NUM_ID:
                abstract = num.find(w("abstractNumId"))
                if abstract is not None:
                    self.abstract_id = abstract.get(w("val"))
        if self.abstract_id is None:
            raise OutlineError(
                f"в шаблоне не найден список numId={self.SOURCE_NUM_ID}; "
                "шаблон не соответствует ожидаемому формату"
            )
        self.next_id = max(max_id, 100) + 1

    def new_list(self) -> int:
        num = ET.SubElement(self.root, w("num"))
        num.set(w("numId"), str(self.next_id))
        ET.SubElement(num, w("abstractNumId")).set(w("val"), self.abstract_id)
        override = ET.SubElement(num, w("lvlOverride"))
        override.set(w("ilvl"), "0")
        ET.SubElement(override, w("startOverride")).set(w("val"), "1")
        self.next_id += 1
        return self.next_id - 1


# --------------------------------------------------------------------------
# Шапка документа
# --------------------------------------------------------------------------

def fill_header_table(table: ET.Element, meta: dict) -> None:
    """Заполняет таблицу-шапку: «Кому» (наименование, адрес, сокращение) и «Дата»."""
    rows = table.findall(w("tr"))
    if len(rows) < 3:
        return

    def cell_paragraphs(row):
        cell = row.find(w("tc"))
        return cell, cell.findall(w("p")) if cell is not None else (None, [])

    # Строка «Кому»: первый абзац — метка, дальше строки адресата.
    cell, paragraphs = cell_paragraphs(rows[1])
    if cell is not None and len(paragraphs) > 1:
        template_p = paragraphs[1]
        lines = [
            meta.get("to_name", "[наименование]"),
            meta.get("to_address", "[адрес]"),
            f"(далее – «{meta['to_short']}»)" if meta.get("to_short") else "(далее – «[•]»)",
        ]
        for p in paragraphs[1:]:
            cell.remove(p)
        for line in lines:
            new_p = copy.deepcopy(template_p)
            replace_paragraph_text(new_p, line)
            cell.append(new_p)

    # Строка «Дата»: второй абзац — само значение.
    cell, paragraphs = cell_paragraphs(rows[2])
    if cell is not None and len(paragraphs) > 1:
        replace_paragraph_text(paragraphs[1], meta.get("date", "ПРОЕКТ"))


def replace_paragraph_text(p: ET.Element, text: str) -> None:
    """Оставляет в абзаце один прогон с новым текстом, сохраняя формат абзаца."""
    runs = p.findall(w("r"))
    keeper = None
    for run in runs:
        if keeper is None:
            keeper = run
        else:
            p.remove(run)
    if keeper is None:
        p.append(make_run(text))
        return
    for t in keeper.findall(w("t")):
        keeper.remove(t)
    for br in keeper.findall(w("br")):
        keeper.remove(br)
    t = ET.SubElement(keeper, w("t"))
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text


# --------------------------------------------------------------------------
# Основная сборка
# --------------------------------------------------------------------------

def build_document(document_root: ET.Element, numbering: NumberingPool,
                   meta: dict, blocks: list[dict]) -> None:
    body = document_root.find(w("body"))
    if body is None:
        raise OutlineError("в шаблоне нет <w:body>")

    children = list(body)
    header_table = next((c for c in children if c.tag == w("tbl")), None)
    sect_pr = children[-1] if children and children[-1].tag == w("sectPr") else None

    for child in children:
        if child is not header_table and child is not sect_pr:
            body.remove(child)

    if header_table is not None:
        fill_header_table(header_table, meta)

    def append(element: ET.Element) -> None:
        if sect_pr is not None:
            body.insert(list(body).index(sect_pr), element)
        else:
            body.append(element)

    append(make_paragraph(""))
    append(make_paragraph(f"Кас.: {meta.get('re', '[краткое описание сделки]')}"))

    closing_text = meta.get("closing", "С уважением,")
    closing_written = False
    current_list: int | None = None

    for block in blocks:
        kind = block["kind"]

        if kind == "schedule":
            if not closing_written and closing_text.lower() not in ("нет", "no", "-"):
                append(make_paragraph(closing_text))
                closing_written = True
            current_list = None
            append(make_paragraph("", page_break=True))
            append(make_paragraph(block["text"], style="SBLSchL1"))

        elif kind == "part":
            current_list = None
            append(make_paragraph(block["text"]))

        elif kind == "pagebreak":
            append(make_paragraph("", page_break=True))

        elif kind == "heading":
            level = block["level"]
            style = HEADING_STYLES.get(level)
            if style is None:
                raise OutlineError(f"строка {block['lineno']}: уровень заголовка {level} не поддержан")
            append(make_paragraph(block["text"], style=style))

        elif kind == "body":
            append(make_paragraph(block["text"], style=block["style"]))

        elif kind == "item":
            if current_list is None:
                current_list = numbering.new_list()
            append(make_paragraph(block["text"], style="BodyText", num_id=current_list,
                                  ilvl=block["ilvl"], keep_lines=True))

    if not closing_written and closing_text.lower() not in ("нет", "no", "-"):
        append(make_paragraph(closing_text))


def render(outline_path: Path, output_path: Path, template_path: Path) -> None:
    meta, blocks = parse_outline(outline_path.read_text(encoding="utf-8"))
    if not blocks:
        raise OutlineError("исходник пуст — нет ни одного абзаца заключения")

    with zipfile.ZipFile(template_path) as zf:
        parts = {name: zf.read(name) for name in zf.namelist()}

    for name in ("word/document.xml", "word/numbering.xml", "word/styles.xml"):
        if name not in parts:
            raise OutlineError(f"шаблон повреждён: в нём нет {name}")
        register_namespaces(parts[name])
    check_styles(parts["word/styles.xml"])

    document_source = parts["word/document.xml"]
    numbering_source = parts["word/numbering.xml"]
    document_root = ET.fromstring(document_source)
    numbering_root = ET.fromstring(numbering_source)
    numbering = NumberingPool(numbering_root)

    build_document(document_root, numbering, meta, blocks)

    parts["word/document.xml"] = serialize_part(document_root, document_source)
    parts["word/numbering.xml"] = serialize_part(numbering_root, numbering_source)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, data in parts.items():
            zf.writestr(name, data)


def main() -> int:
    default_template = Path(__file__).resolve().parent.parent / "assets" / "template.docx"
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("outline", type=Path, help="текстовый исходник заключения")
    parser.add_argument("-o", "--output", type=Path, required=True, help="путь к .docx")
    parser.add_argument("--template", type=Path, default=default_template,
                        help="шаблон фирмы (по умолчанию assets/template.docx)")
    args = parser.parse_args()

    if not args.template.exists():
        print(f"Шаблон не найден: {args.template}", file=sys.stderr)
        return 2
    try:
        render(args.outline, args.output, args.template)
    except OutlineError as exc:
        print(f"Ошибка исходника: {exc}", file=sys.stderr)
        return 1
    print(f"Готово: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Digest format ("Обзор изменений законодательства РФ")

A digest is a periodic round-up of multiple legislative developments, written in a neutral, reporting register — it tells the client what happened, not what to think about it.

## Output medium

Word `.docx` on the firm's template, same as an Alert. Not a slide deck. Build it with the `docx` skill's unzip-edit-rezip workflow on a copy of the firm template so the numbering definitions and styles come across intact.

The whole document is one auto-numbered outline driven by a single numbering definition, so numbering (1 → 1.1 → a. → i.) is produced by the styles, not typed by hand. Continuation paragraphs — the body of an item, a citation line — carry the same style as the level they belong to plus a number-suppressing `numPr`.

| Level | Style ID | What it holds | Rendered as |
|---|---|---|---|
| Cover | `Normal` | title, period line, framing sentence | unnumbered |
| L1 | `SBLENGL1` | priority tag (ОСОБЕННО ВАЖНО и т.д.), bold caps | `1.` `2.` `3.` |
| L2 | `SBLENGL2` | item headline; item body paragraphs, suppressed | `1.1` `1.2` |
| L3 | `SBLENGL3` | lettered sub-items; citation line, suppressed | `a.` `b.` |
| L4 | `SBLENGL4` | roman sub-sub-items | `i.` `ii.` |
| L5 | `SBLRUSL5` | deepest nesting, used rarely | `A.` `B.` |

Never type the numbers into the text — set the style and let Word number the paragraph.

### Building a continuation paragraph correctly

Suppressing the number takes three things together, and leaving any of them out produces a visibly wrong document:

```xml
<w:pPr>
  <w:pStyle w:val="SBLENGL2"/>
  <w:numPr><w:ilvl w:val="0"/><w:numId w:val="0"/></w:numPr>
  <w:ind w:left="720" w:firstLine="0"/>
  <w:rPr><w:b w:val="0"/><w:bCs w:val="0"/><w:rFonts w:cstheme="minorHAnsi"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr>
</w:pPr>
```

- **`numId 0`** removes the number.
- **`w:firstLine="0"`** cancels the hanging indent the numbering would otherwise leave behind. Without it the paragraph hangs out to the left of the item it belongs to.
- **`<w:b w:val="0"/><w:bCs w:val="0"/>`, repeated on every run in the paragraph**, is required because `SBLENGL1` and `SBLENGL2` are bold styles. Without the override the whole body of an item renders bold. `SBLENGL3` and `SBLENGL4` are not bold, so they need no override.
- Every run also carries `<w:rFonts w:cstheme="minorHAnsi"/><w:sz w:val="24"/><w:szCs w:val="24"/>` to match the rest of the document.

Indent values observed in the client files:

| Paragraph | `w:left` |
|---|---|
| Item body under a headline (`SBLENGL2`, suppressed) | `720` |
| Citation line at the end of an item (`SBLENGL3`, suppressed) | `720` |
| Prose continuing after a lettered list (`SBLENGL3`, suppressed) | `1440` |
| Prose continuing after a roman list (`SBLENGL4`, suppressed) | `2160` |

When an item has no lettered list at all, a trailing line such as "Судебное заседание назначено на …" stays at `SBLENGL2`/`720` rather than dropping to `SBLENGL3`.

### Court-practice items

`СУДЕБНАЯ ПРАКТИКА` covers decided cases as well as pending ones, and first-instance courts as well as the ВС РФ — a well-reasoned arbitrazh-court ruling on a live question (e.g. whether sanctions make an ICC arbitration clause unenforceable) belongs there on its merits. Shape for a decided case:

1. Headline at `SBLENGL2`, agent-first and stating the outcome ("Арбитражный суд оставил без рассмотрения иск иностранного поставщика, отклонив довод о неисполнимости арбитражной оговорки из-за санкций.").
2. Facts, then each side's position, as suppressed `SBLENGL2` paragraphs at `720`.
3. A lead-in ("Суд оставил иск без рассмотрения и указал следующее:") followed by the court's reasoning as lettered `SBLENGL3` items — one ground per item, each naming the authority it rests on with number and date.
4. Procedural tail (returned госпошлина and similar) as a suppressed `SBLENGL3` paragraph at `1440`, since it follows the lettered list.
5. Citation line at `SBLENGL3`/`720`.

For a pending case (an **определение о передаче**) the shape stops at the parties' positions and closes with "Судебное заседание назначено на …" — do not write the outcome as a holding.

## Text conventions

The rules in `references/writing-style.md` apply in full, and the same hard bans as for Alerts: **no "ё" and no em dash "—" anywhere** in the delivered text. Inside a defined-term parenthetical the digest uses an **en dash**: `(далее – «Указ № 604»)`. Everywhere else in running text a dash is a **hyphen with spaces**. Defined terms themselves are set in **bold italic** - italic alone is wrong, and the bold+italic run covers the guillemets too: ***«Указ № 604»***. Placeholders awaiting a real number or date are highlighted yellow.

Unlike an Alert, a digest's lettered and roman lists do **not** take "и" before the final item. Every item ends with a plain semicolon and the last one with a full stop.

## Cover

All three cover paragraphs use the `Normal` style with direct formatting on top — they are not headings, and the `Title` style is not used.

| Paragraph | Text | Formatting |
|---|---|---|
| Title | **"Обзор изменений законодательства РФ"** | `<w:jc w:val="center"/>`, runs **bold** |
| Period line | **"С [date] по [date] [месяц] [year] года"** | `<w:jc w:val="center"/>`, not bold |
| Framing sentence | fixed wording, see below | `<w:ind w:left="0"/>`, not bold, not centred |

Every run on the cover carries `<w:rFonts w:cstheme="minorHAnsi"/><w:sz w:val="24"/><w:szCs w:val="24"/>`, like the rest of the document. Leaving the cover as bare `Normal` paragraphs is wrong: the title then renders left-aligned and in body weight, which is the first thing a reviewer notices.

The earlier version of this file gave the title as "Дайджест изменений законодательства РФ"; the client-facing wording actually in use is "Обзор".

The period line matches the exact coverage window, with no gaps or overlaps with the previous issue.

The framing sentence is reused verbatim, varying the practice areas only if the scope genuinely differs: *"Представляем вашему вниманию дайджест наиболее интересных и значимых законодательных изменений в области корпоративного, финансового, а также в других отраслях права, которые могут затронуть ваш бизнес."*

## Item structure (repeats for every development)

Each item is a self-contained block with this exact shape, in this order:

1. **Priority tag** — its own `SBLENGL1` paragraph in caps, opening the section: one of
   - `ОСОБЕННО ВАЖНО` — the single most significant development(s) of the period, always first
   - `ТАКЖЕ ИНТЕРЕСНО` — noteworthy but secondary legislative/regulatory news
   - `СУДЕБНАЯ ПРАКТИКА` — court decisions, always its own final section
   These are the only three tags observed — don't invent new ones without the user's sign-off. Because the tag is `SBLENGL1`, it takes the section number automatically (1, 2, 3), which is what makes item numbers come out as 1.1, 2.1, 3.1.
2. **Item number**: `<section>.<order>` — produced by the `SBLENGL2` style, never typed. The first digit follows from the tag's position (1 = ОСОБЕННО ВАЖНО, 2 = ТАКЖЕ ИНТЕРЕСНО, 3 = СУДЕБНАЯ ПРАКТИКА), the second is the sequence within that tag.
3. **Headline**: `SBLENGL2`, numbered. One declarative sentence stating what happened, agent-first ("Правительство РФ внесло...", "Государственная дума приняла...", "Президент подписал...", "Верховный суд защитил..."). Not a question, not a teaser.
4. **Body**: `SBLENGL2` with `numId 0` so it sits under the headline without taking its own number. One to a few short paragraphs, third person, factual. Complex provisions are broken into lettered sub-items at `SBLENGL3` and, where the source itself has that depth, roman-numeral sub-sub-items at `SBLENGL4` — again numbered by the style, not typed. Keep numbers, dates, article references exact and in the same place they'd appear in the source law.
5. **Citation line**, `SBLENGL3` with `numId 0`, verbatim official title with number, at the end of the item:
   - Bill: `Законопроект № XXXXXXX-X «[full official title]»`
   - Regulation/instruction: `Указание Банка России от DD.MM.YYYY № XXXX-У «[title]»` (same pattern for other regulator instruments — decree, order, resolution — always dated and numbered)
   - Court decision: `Определение/Постановление [суд, коллегия] от DD.MM.YYYY № [case-court-number] по делу № [case number]`
   - Presidential order: `Распоряжение Президента Российской Федерации от DD.MM.YYYY № XXX-рп «[title]»`
   - If the fact comes from press reporting rather than the primary legal text, add a separate line **"Материал СМИ"** (or a link/reference to it) and hedge the claim in the body with "по данным СМИ" — never present media speculation with the same certainty as a primary-source fact.
   - Where the official text is online, make the citation line a hyperlink (`publication.pravo.gov.ru`, `sozd.duma.gov.ru`, the regulator's own site). A citation without a link is acceptable; a wrong or invented link is not.

## Continuity between issues

The coverage window starts the day after the previous issue's window ends, so ask for or check the previous issue before choosing the period. Do not leave gaps.

When a development already covered in a previous digest has progressed (e.g. a bill moves from first to second/third reading), open the item with a short pointer — *"Подробнее о законопроекте мы писали ранее"* — then give only the delta, not a re-explanation of the whole thing.

A development that fell inside the previous window but was not covered there can be picked up in the current issue rather than dropped. Say so when handing the draft over, so the reviewer knows why an item is dated before the period line.

## Where to research

- **КонсультантПлюс legal news** (`consultant.ru/legalnews/`) is the workhorse. Its weekly "Важные новости для юриста за неделю с … по …" round-ups cover the period in blocks and each item names its source act with number and date. Pull every weekly round-up that overlaps the window; the list is paginated (`?page=N`).
- **Судебная практика СКЭС ВС РФ** (`t.me/vs_court`, readable without login at `t.me/s/vs_court`) gives Supreme Court economic-chamber matters with case numbers, facts and the court's reasoning. Distinguish two kinds of post: an **определение о передаче** means the case is only scheduled for a hearing, so write it as "ВС РФ рассмотрит спор о …" and give the hearing date; a post with a "Позиция Верховного суда" block is a decided case and can be reported as a holding.
- **publication.pravo.gov.ru** carries official texts and is the right target for a citation hyperlink when the document number is known.
- Право.ру, ККПМ, Better Chance and similar channels are usable, but paraphrase rather than copy, and prefer citing the underlying act.

Several legal databases block automated access from this environment (`cbr.ru`, `garant.ru` document pages, `pravo.gov.ru` document pages, files and API all return 403). When a needed text is unreachable, take the facts from КонсультантПлюс's summary of it and cite the act itself, rather than dropping the item.

### Recovering a document КонсультантПлюс's summary is too thin for

When the user gives a `publication.pravo.gov.ru` link (403) and the annotation on `consultant.ru/law/hotdocs` is one sentence, the **full text is usually reachable anyway**, in three steps:

1. `consultant.ru/law/hotdocs/?date_start=DD.MM.YYYY&date_end=DD.MM.YYYY&page=N` - strip the tags and grep the listing for the topic word. This gives the act's exact number, date and official title.
2. The listing links a per-document annotation page, `consultant.ru/law/hotdocs/<id>.html`, which carries the annotation plus a `consultant.ru/document/cons_doc_LAW_<n>` link.
3. That document page lists the act's sections as `/document/cons_doc_LAW_<n>/<hash>/` sub-pages. Fetching each sub-page gives the **operative text verbatim** - which paragraph of which annex is restated, what the new clause says, what deadline it sets. This is what turns a one-line annotation into a real lettered breakdown.

### Reading a law firm's redline PDF

Legal-update PDFs from firms (Better Chance and similar) are often a redline of the old instrument against the new one. `pdftotext` silently interleaves deleted and inserted text, which produces nonsense like "от 21 мая 202529 июня 2026 г. N 70607402-У" and, worse, makes it easy to report a deleted threshold as the current one. Extract by span colour instead:

```python
import pymupdf
d = pymupdf.open('file.pdf')
for p in d:
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                print(s['color'], s['text'])   # red = deleted, coloured = inserted, 0 = unchanged
```

Old text always precedes new text in the interleaved stream, so the second of a pair is the rule in force. Verify any figure that changed by locating the surviving black text around it before writing a number into the digest.

### Entry into force is read from the act's last article, never from a summary

The most damaging error found in a partner review of a digest was an inverted commencement date: the item said the law "вступает в силу с 1 октября 2026 года, за исключением отдельных положений", when its final article said the opposite - in force on publication, with one article deferred to 1 October. КонсультантПлюс's annotation and the press coverage both stated the deferred date prominently, and neither made clear which half was the exception.

So for every act in a digest, open its **final article** (`Статья N` on the last `cons_doc_LAW_<n>/<hash>/` sub-page) and read the commencement clause verbatim. The pattern "вступает в силу со дня официального опубликования, за исключением статьи X … Статья X вступает в силу с [date]" is common and inverts easily. Name in the item which provision carries the deferred date, not just the date.

Where an act carries no commencement clause at all, do not present the default as if it came from the document: say so and cite the default rule, e.g. "Специальной нормы о вступлении в силу постановление не содержит, поэтому по общему правилу п. 6 Указа Президента РФ от 23.05.1996 № 763 оно вступает в силу по истечении 7 дней после дня официального опубликования."

### An item's own numbers must reconcile

A reviewer will divide the figures in an item by each other. If a court reduced an award to a stated sum, the facts quoted in the item have to produce that sum: when the digest gave the plot area as the claimant's 800 кв. м but the appellate court had computed from the technical passport's 252 кв. м and the 915 336 руб. 30 коп. actually paid, the arithmetic was out by a factor of four and the item read as wrong even though every individual number was accurate. Before delivery, recompute any figure the item implies, and if a source uses two different values for the same quantity, give both and say whose each is.

### Preserving hyperlinks when rebuilding a paragraph

Citation lines are hyperlinks. Rebuilding a paragraph from its `<w:pPr>` plus a fresh run silently drops the `<w:hyperlink>` wrapper (or the `fldChar`/`instrText` field pair, which is how Word writes them when the link was typed rather than inserted from a rel). After any batch of paragraph-level edits, count `<w:hyperlink` and `HYPERLINK` occurrences against the original and restore anything lost.

## Register

- Third person, no "мы полагаем" / "мы рекомендуем" editorializing (that belongs to Alerts, not digests).
- No recommendations section, no client-specific risk framing — a digest reports; it does not advise.
- Precision over color: exact dates, exact article numbers, exact bill/case numbers every time — treat these as immutable in the same sense as the legal-doc-translation skill's "specific hits."

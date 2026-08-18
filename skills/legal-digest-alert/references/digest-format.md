# Digest format ("Обзор изменений законодательства РФ")

A digest is a periodic round-up of multiple legislative developments, written in a neutral, reporting register — it tells the client what happened, not what to think about it.

## Output medium

Word `.docx` on the firm's template, same as an Alert. Not a slide deck. Build it with the `docx` skill's unzip-edit-rezip workflow on a copy of the firm template so the numbering definitions and styles come across intact.

The whole document is one auto-numbered outline driven by a single numbering definition, so numbering (1 → 1.1 → a. → i.) is produced by the styles, not typed by hand. Continuation paragraphs — the body of an item, a citation line — carry the same style as the level they belong to plus `<w:numId w:val="0"/>`, which suppresses the number while keeping the indent.

| Level | Style ID | What it holds | Rendered as |
|---|---|---|---|
| Cover | `Normal` | title, period line, framing sentence | unnumbered |
| L1 | `SBLENGL1` | priority tag (ОСОБЕННО ВАЖНО и т.д.), bold caps | `1.` `2.` `3.` |
| L2 | `SBLENGL2` | item headline; item body paragraphs with `numId 0` | `1.1` `1.2` |
| L3 | `SBLENGL3` | lettered sub-items; citation line with `numId 0` | `a.` `b.` |
| L4 | `SBLENGL4` | roman sub-sub-items | `i.` `ii.` |
| L5 | `SBLRUSL5` | deepest nesting, used rarely | `A.` `B.` |

Never type the numbers into the text — set the style and let Word number the paragraph.

## Text conventions

The rules in `references/writing-style.md` apply in full, and the same hard bans as for Alerts: **no "ё" and no em dash "—" anywhere** in the delivered text (hyphen with spaces instead; en dash only inside numeric ranges). Defined terms introduced with `(далее – «X»)` are set in bold italic; placeholders awaiting a real number or date are highlighted yellow.

## Cover

- Title: **"Обзор изменений законодательства РФ"** (the earlier version of this file said "Дайджест изменений законодательства РФ"; the client-facing wording actually in use is "Обзор").
- Period line: **"С [date] по [date] [месяц] [year] года"** — matches the exact coverage window, no gaps or overlaps with the previous issue.
- One fixed framing sentence (reuse verbatim, only vary the practice areas if the scope genuinely differs): *"Представляем вашему вниманию дайджест наиболее интересных и значимых законодательных изменений в области корпоративного, финансового, а также в других отраслях права, которые могут затронуть ваш бизнес."*

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

## Continuity between issues

When a development already covered in a previous digest has progressed (e.g. a bill moves from first to second/third reading), open the item with a short pointer — *"Подробнее о законопроекте мы писали ранее"* — then give only the delta, not a re-explanation of the whole thing.

## Register

- Third person, no "мы полагаем" / "мы рекомендуем" editorializing (that belongs to Alerts, not digests).
- No recommendations section, no client-specific risk framing — a digest reports; it does not advise.
- Precision over color: exact dates, exact article numbers, exact bill/case numbers every time — treat these as immutable in the same sense as the legal-doc-translation skill's "specific hits."

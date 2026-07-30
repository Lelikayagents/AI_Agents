---
name: legal-digest-alert
description: Research Russian legislative and regulatory developments and turn that research into client-facing deliverables in Stonebridge Legal's established formats — a periodic multi-item "Дайджест изменений законодательства" deck, a single-topic advisory "Alert" deck, or a справка memo answering one client question — then revise them against the user's feedback. Use whenever the user asks to compile, draft, or update a "дайджест", "Alert", or "справка", asks for a legislative round-up or single-topic legal brief for a client, or wants an existing one edited. See references/digest-format.md and references/alert-format.md for the exact templates this skill follows.
---

# Legal digest / Alert / справка

## Three deliverable types

| Type | Register | Scope | Closing section |
|---|---|---|---|
| **Дайджест** | Neutral, third person, reporting only | Multiple developments over a period | None — no recommendations |
| **Alert** | First-person-plural, advisory ("мы полагаем...") | One development, deep dive | Mandatory "Наши предложения и рекомендации" |
| **Справка** | Same as Alert | One client question, treated as the "development" | Mandatory recommendations — a справка without a practical answer isn't useful |

Read `references/digest-format.md` or `references/alert-format.md` in full before drafting either — they carry the exact slide-by-slide shape, citation formats, and the specific fixed wording (titles, framing sentences, footer, contact block) that must be reproduced verbatim, not paraphrased.

Don't blend the registers: a digest item must not editorialize, and an Alert/справка must not skip its recommendations section for the sake of sounding neutral.

## Workflow

1. **Clarify scope** if not already given: which deliverable type, the coverage period (digest) or the specific instrument/question (Alert/справка), and which practice areas matter to this client.
2. **Research.** Pull primary sources — bill texts, regulator instructions/decrees/orders, court decisions — with exact numbers and dates. Use the Legal Data Hunter MCP tool where it covers the jurisdiction/instrument; for anything sourced from press reporting rather than a primary legal text, keep that distinction explicit (see the digest's "Материал СМИ" rule) rather than presenting it with primary-source certainty.
3. **For a digest**, sort findings into the three tags (ОСОБЕННО ВАЖНО / ТАКЖЕ ИНТЕРЕСНО / СУДЕБНАЯ ПРАКТИКА) and check the previous issue, if the user has or references one, so continuing items open with a delta pointer instead of restating the whole history.
4. **For an Alert/справка**, group findings into bespoke thematic subsections, and don't compress away analysis of any nuance, ambiguity, or apparent drafting conflict — that depth is the deliverable's value.
5. **Draft.** Follow the matched reference file's structure exactly: fixed wording where the template specifies it verbatim, exact citation formats, correct nesting of `(a)(b)(c)` / `(i)(ii)(iii)` sub-items mirroring the source, and the mandatory footer/contact block content (reuse the firm's real details from `alert-format.md` — never invent placeholder contact info or a placeholder logo).
6. **Output format.** These are slide decks in production (cover slide, per-slide footer, slide numbers, a closing contact slide) — build the final deliverable as a `.pptx` using the `pptx` skill. If the user hasn't approved the content yet, or asks for a quick draft, it's fine to write the text out in chat/markdown first for fast review, then convert to the branded deck once the content is settled — say which mode you're in so the user knows whether they're reviewing content or the final artifact.
7. **Revise.** When the user pushes back on wording, structure, or emphasis, treat their correction as an update to how *this* skill should behave next time too, not just a one-off fix — apply it consistently across the rest of the current draft.

## Citation discipline

Every legal instrument, case, or bill named must carry its full official title, number, and date verbatim at the point it's introduced — same discipline as this repo's `legal-doc-translation` skill treats defined terms and structural references: never paraphrase a title, drop a number, or renumber a citation.

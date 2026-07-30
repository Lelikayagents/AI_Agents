---
name: legal-doc-translation
description: Translate legal documents (contracts, statutes, court filings, powers of attorney, corporate charters, etc.) between Russian and English while precisely preserving every legally load-bearing detail — clause/article numbers, statute and case citations, defined terms, dates, sums and currencies, party names, cross-references, and the original numbering/formatting structure. Produces a formatted .docx translation plus a short flagged-terms appendix listing concepts with no exact equivalent in the target legal system, with a translator's note for each. Use this whenever the user asks to translate a legal or official document, a contract, a law/statute excerpt, a court document, or mentions "юридический перевод", "перевести договор/закон", or needs an RU↔EN legal translation — even if they don't use the word "skill".
---

# Legal Document Translation (RU ↔ EN)

## Why this is different from ordinary translation

A fluent, natural-sounding translation of a legal document can still be a bad translation if it silently drops or subtly shifts a detail that carries legal weight. A missing "не позднее" (no later than), a renumbered sub-clause, or a paraphrased defined term can change what a contract obligates someone to do. The goal here is not elegance — it's that a lawyer reading the translation next to the original could verify, item by item, that nothing load-bearing moved or disappeared.

Treat the document in two layers:
1. **The prose** — translate this for a native, professional legal register in the target language (formal contract/statute style, not literal word-for-word where natural phrasing serves the same legal meaning).
2. **The specific hits** — treat these as near-immutable anchors, not prose to be rendered freely.

## Specific hits: what must never be lost or altered

Before translating, scan the source and mentally (or literally, in a scratch note) tag every instance of:

- **Structural references**: article/clause/section/paragraph/annex numbers (e.g. "п. 4.2 ст. 15", "Section 8(b)(iii)", "Приложение №2"). Keep the same numbering scheme visible in the translation — don't renumber, and don't drop a sub-letter or sub-number.
- **Citations**: statute names and numbers (e.g. "ст. 421 ГК РФ", "15 U.S.C. § 78j"), case names, decree/order numbers, registration numbers.
- **Defined terms**: capitalized or quote-marked terms that are defined elsewhere in the document (e.g. "the Company", "Заказчик", "Confidential Information"). Once you pick a target-language rendering for a defined term, use that exact same rendering every single time it recurs — never vary it for stylistic reasons, since consistency is what makes the definition binding.
- **Dates and deadlines**: preserve format precision — "in no event later than 30 (thirty) calendar days" needs both the digit and the spelled-out form preserved if the source has both.
- **Money and quantities**: amounts, currencies, percentages, and any words-plus-digits redundancy (e.g. "100 000 (сто тысяч) рублей" → keep both numeral and spelled-out form: "100,000 (one hundred thousand) rubles").
- **Party names and identifiers**: names of individuals/entities, INN/OGRN/EIN-type registration numbers, addresses — copy verbatim, do not transliterate inconsistently across the document.
- **Cross-references**: "as defined in Section 2", "в соответствии с п. 3.1 настоящего Договора" — make sure the reference still points to the correct renumbered-or-not location in your translation.

A useful gut check while translating: if you highlighted only the numbers, proper nouns, and quoted terms in the source and target side by side, they should match one-to-one.

## Workflow

1. **Read the whole source document first** before translating any of it. Note the legal system it comes from (e.g. Russian civil law vs. US/UK common law) — this determines which target-language legal vocabulary is appropriate and which concepts might not map cleanly.
2. **Build a mental (or written) glossary of defined terms** before translating the body, so the same term gets the same rendering everywhere it appears. For a long document, jot this down in a scratch file rather than trusting memory across many pages.
3. **Translate section by section**, keeping structural numbering intact. If the source uses "4.2.1", the translation uses "4.2.1" too — do not flatten or renumber even if the target language would naturally structure it differently.
4. **Flag anything without a clean equivalent** as you go, rather than silently picking a rendering and moving on. See below.
5. **Assemble the final document as .docx**, mirroring the source's structure (headings, numbered lists, tables, signature blocks). Use the `docx` skill for this — read it before generating the output file, since it has the correct approach for headings, page numbers, and formatting fidelity in Word documents.
6. **Append a flagged-terms section** at the end of the same .docx (or as a clearly separated final section) — see format below.

## Handling terms with no exact equivalent

Legal systems don't map onto each other one-to-one. Russian civil-law concepts like "юридическое лицо", "существенные условия договора", or "неустойка" don't have a single perfect English match; English common-law concepts like "consideration", "estoppel", or "fiduciary duty" don't have a single perfect Russian match either. When you hit one of these:

- Pick the closest functional equivalent for the main translation (so the document still reads naturally), rather than leaving it untranslated or inventing an awkward calque.
- Add it to the flagged-terms appendix with a one- or two-sentence translator's note explaining the gap — e.g. what the source term actually covers, why the target term is only approximate, and what a reader should watch out for if this distinction matters (e.g. in a dispute).
- Don't flag routine vocabulary just because it's legal jargon — only flag it when the *concept itself* doesn't map cleanly, not merely when the word is hard.

### Flagged-terms appendix format

Use this structure at the end of the document:

```
## Translator's Notes: Flagged Terms

1. **[Source term]** → translated as "[chosen rendering]"
   [1-2 sentence note on the gap and what to watch for.]

2. **[Source term]** → translated as "[chosen rendering]"
   [...]
```

If nothing genuinely warrants flagging, say so explicitly ("No terms required flagging in this document") rather than omitting the section — that omission should be a deliberate statement, not a gap the user has to wonder about.

## A note on scope

This skill is for producing a careful, review-ready translation — it is not a substitute for a licensed attorney's sign-off on a document that will actually be filed, executed, or relied on in a legal proceeding. If the user's document is going to be used in a real transaction or filing, mention that a qualified lawyer in the target jurisdiction should review it before use, especially the flagged terms.

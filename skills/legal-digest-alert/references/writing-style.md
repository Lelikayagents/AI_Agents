# Writing style: making digests/Alerts/справки read as human-written

Every digest, Alert, and справка produced by this skill must pass a final anti-AI-tell pass before delivery — the same discipline the `humanizer` skill applies to general text, calibrated here to Russian legal/financial writing. The goal stated by the user this skill was built for: text that does not need editing afterward to strip out "длинные тире, абстрактные формулировки" (em-dash overuse, abstract/inflated phrasing) or other tells that mark it as AI-written.

This is a mandatory last step, not a style suggestion: **before delivering any digest, Alert, or справка, re-read the full draft against the checklist below and fix every hit.** If the `humanizer` skill is available, run the finished draft through it as the literal final pass; if not, apply this checklist by hand.

## Why this matters here specifically

Detection of AI-written text (both by human reviewers and by statistical detectors) rests on two things: **low perplexity** (the model always reaches for the single most predictable next phrase, producing clichés) and **low burstiness** (every sentence lands at roughly the same length and shape, unlike real human prose, which varies). A client-facing legal deliverable that reads as templated undercuts the exact thing an Alert is supposed to demonstrate — that the firm engaged with this specific development, not that it ran a generic prompt.

## Banned patterns (Russian-specific, on top of the humanizer skill's English list)

The humanizer skill's full pattern list (inflated significance, promotional language, superficial "-ing"/deepричастие endings, vague attributions, rule-of-three, copula avoidance, negative parallelism, filler/hedging, em dash overuse, etc.) applies directly — most of it is language-agnostic. On top of that, watch specifically for these Russian-language tells:

**Canned hedge/transition phrases** — cut or replace with a plain statement:
- "важно отметить", "стоит подчеркнуть", "необходимо отметить", "следует учитывать", "необходимо понимать", "отдельно стоит отметить" — these add zero information; either state the fact directly or delete the lead-in entirely.
- "таким образом" and "в итоге"/"в результате" used as a reflexive conclusion-marker on nearly every paragraph, rather than because a real logical conclusion follows.
- "в контексте", "с точки зрения", "в рамках" used as vague scene-setting rather than because a specific frame of reference is doing real work in the sentence.
- "в связи с чем", "в целях" as reflexive connectors where "поэтому" / "чтобы" would be plainer and more natural.

**Inflated-significance phrasing** (the Russian equivalent of "stands as a testament to"):
- "играет ключевую/важную/значительную роль", "оказывает существенное влияние", "открывает новые возможности", "позволяет повысить эффективность" — these describe importance instead of describing what actually happened. Replace with the concrete mechanism or effect.

**Nominalization instead of a verb** — a strong Russian-specific AI tell: turning a plain verb into an abstract отглагольное существительное, especially at the start of a sentence or clause, where a human would just use the verb directly. E.g. "осуществление раскрытия информации производится эмитентом" instead of "эмитент раскрывает информацию." Prefer the verb form unless the nominal form is itself a defined legal term (e.g. "раскрытие информации" as the term of art is fine — the flag is for gratuitous extra nominalizations layered on top).

**"Данный"/"настоящий" as a reflexive substitute for "этот"** in every other sentence — legal drafting legitimately uses "настоящий" for the instrument being discussed (as in "настоящий проспект"), but don't default to it as a tic everywhere a plain "этот/это" would read more naturally.

**Passive/impersonal administrative verbs used by default** — "осуществляется", "производится", "обеспечивается" as the default verb choice even when an active construction with a named actor (эмитент, Банк России, организатор размещения) is available and clearer. Use the active form with the actual actor named unless the passive is doing real work (e.g. genuinely describing an obligation without regard to who performs it).

## Patterns already covered by the English list — apply them in Russian too

- **Em dash (—): banned outright in client deliverables.** This started as a frequency cap and was tightened to an absolute rule by the partner edit-pass: a delivered Alert/справка/digest should contain zero "—" characters. Use a hyphen with spaces where a dash is genuinely needed (`Период прогноза - не менее 12 месяцев`), an en dash inside numeric ranges (`1.2–1.5`), or rewrite the sentence — e.g. "Срок раскрытия … это риск для графика сделки" rather than "Срок раскрытия … — риск". Grep the finished text for "—" before delivery; any hit is a defect.
- **The letter "ё" is not used.** Write "прошел", "еще", "объем", "отчетность", "зеленые", "учет". Grep for "ё"/"Ё" before delivery.
- **Rule of three.** Don't force findings into triads ("во-первых, во-вторых, в-третьих" or three-item lists) just to look thorough — list exactly as many items as are actually distinct, even if that's two or four.
- **Negative parallelism** ("это не просто X, это Y") — keep only when the contrast is substantively load-bearing (e.g. contrasting the old narrow corporate-dispute basis for раскрытие обеспечительных мер against a broader new basis is a real legal distinction worth stating this way); cut it when it's decorative.
- **Vague attribution.** This skill's own citation discipline already bans this in substance (every claim needs a named, dated instrument or a "по данным СМИ" hedge with a real source) — but watch the softer version too: "участники рынка отмечают", "по мнению экспертов" without naming who, when the underlying material actually names a specific source. If you have the name, use it.
- **Generic upbeat closers.** An Alert's closing risk paragraph must name a concrete consequence tied to the actual provisions discussed (per `alert-format.md`) — never resolve into a generic "перспективы выглядят позитивно" or "открывает новые горизonты" note.
- **Burstiness.** Vary sentence length deliberately across a paragraph — don't let every sentence in a subsection land at 25–35 words. A short, direct sentence next to a longer analytical one reads as human; a uniform cadence reads as generated.

## What NOT to touch

- The alert-format's own prescribed hedges — "мы полагаем", "мы понимаем", "можно предположить, что" — are deliberate house register for Alerts/справки, not AI-tells. Don't strip these out; they're what the format calls for. The distinction: a hedge earns its place when it's followed by an actual analytical claim; it's a tell when it's decorative throat-clearing before a sentence that would stand fine without it.
- Legal terms of art, defined terms, and citation-format boilerplate required by `digest-format.md`/`alert-format.md` (fixed titles, footer text, citation patterns) are not "clichés" to be freshened up — reproduce those verbatim as required.
- Chat-facing convenience markers (⚠️ flags for open verification items, bold inline flags used while drafting with the user) belong in the conversation, never inside the delivered document/deck text itself — strip them before the content goes into a `.docx`/`.pptx` deliverable.

## Final pass before delivery

1. Read the full draft once for content, once purely for rhythm — does it sound like something a person wrote at their desk, or like a template filled in?
2. Mechanical greps, each of which must return zero hits: `—` (em dash), `ё`/`Ё`, double spaces.
3. Grep for the banned-phrase list above and in the humanizer skill; replace or delete every hit.
4. Check that enumerations are rendered as bulleted lists rather than semicolon-chained prose.
5. Check that no two consecutive subsections have identical sentence-count/paragraph-length shape.
6. Confirm every hedge phrase is attached to a real analytical claim, not standing alone as filler.
7. Confirm every placeholder is highlighted yellow and every defined term is bold italic at first use.
8. If `humanizer` is available as a skill, invoke it on the finished draft as a last independent check before delivering the file.

Note on this file's own prose: the guidance above is written for the model, not for the client, so it uses em dashes freely. The bans apply to delivered Russian-language client documents, not to these reference notes.

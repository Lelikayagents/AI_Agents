---
name: legal-re-reserch
description: Re-verify a legal or regulatory document — a legislative digest, client alert, newsletter, memo, or briefing note — against the primary sources it cites, before it goes out. Checks every act number, date, title, effective date, deadline, threshold, monetary amount, case number and cross-reference against the published text of the act itself (publication.pravo.gov.ru, cbr.ru, court records), never against a secondary summary; recomputes every arithmetic figure; and reports findings graded by what the editor has to do about them, with «В обзоре» vs «Фактически» and a link to the source for each. Use this whenever the user asks to fact-check, verify, re-check or proofread a document for factual accuracy, sends a digest/обзор/дайджест/алерт and asks whether it is correct, or says "перепроверь на фактическую информацию", "проверь по первоисточникам", "сверь с законом", "фактчек", "проверь цифры и даты" — and also whenever the user has set up a standing arrangement to check documents they send, so a bare document with no instructions still gets the full check.
---

# Legal Fact-Check (сверка по первоисточникам)

## What this is actually for

A legislative digest is not judged on prose. It is judged on whether a reader who acts on it ends up in the right place. The failure modes are narrow and specific: a date of entry into force that is off, an act number that doesn't resolve to a real document, a scope stated more narrowly than the act actually covers, a figure that doesn't reconcile with the other figures in the same paragraph. Any one of those quietly turns a useful document into a liability — a reader counts an 18-month deadline from the wrong date, or concludes a restriction doesn't apply to their subsidiary when it does.

So the job is not "read it and see if it sounds right." It is: take every checkable assertion, find the document it is about, read *that document*, and compare. Everything else in this skill exists to make that affordable.

## The one rule that matters most

**Verify against the act's own published text, never against a summary of it.** Secondary sources — news write-ups, aggregator "hot documents" pages, and especially the small-model summaries that URL-fetching tools return — get legal documents wrong constantly and confidently. They will tell you a decree is financed from the budget when the decree says it is financed from the income of the managed property; they will tell you there is no mention of drones in a decree whose operative paragraph turns on drones.

Treat every secondary source as a lead to the primary document, not as evidence. The only things they are genuinely good for are (a) finding the document, and (b) court decisions whose texts are not publicly posted, where a reputable outlet reporting specifics — a date, a case number, an amount — is the best available evidence and should be labelled as such in the report.

`references/ru-primary-sources.md` has the concrete retrieval recipes for Russian sources — URL patterns, the publication-number scheme, and the environment gotchas that will otherwise cost you an hour. Read it before starting retrieval; it is short.

## Workflow

**1. Extract the text.** `.docx` is a zip: pull `word/document.xml` and walk it for `w:t`, `w:tab`, `w:br` rather than trusting a converter to preserve paragraph breaks. `.pdf` — try the text layer first, and fall back to rendering pages if there isn't one.

**2. Build the claim inventory before checking anything.** Go through the document once and list every assertion that could be wrong in a way that matters:

- act identity — type, number, date, full title, issuing body
- entry into force, and any carve-outs ("за исключением отдельных положений")
- every deadline, period, threshold, percentage, monetary amount, area, headcount
- scope — who or what the rule covers, and whether the document says "only X" where the act says "X and Y"
- cross-references — the act being amended, the act being repealed, cited case law and constitutional-court positions
- consultation windows and planned adoption dates for draft regulations
- for court items: case number, court, date, parties, amounts, procedural posture

Do this as an explicit list. The point is that at the end you can say which claims you checked and which you couldn't — a fact-check report that silently omits an item reads to the editor as "checked and fine," which is the worst possible outcome if it wasn't.

**3. Resolve each act to its published text and read the operative part.** Not the headline, not the first page — the paragraph that carries the claim, plus the final article on entry into force, which is where errors cluster.

**4. Recompute every arithmetic figure.** If a paragraph contains a rate, a share, a period and a total, they must reconcile. When they don't, work backwards: what area, or what period, or what rate *would* produce the stated number? That reverse calculation is what makes the finding actionable — "either the area or the period is wrong" is far more useful to an editor than "this number looks odd." State the arithmetic explicitly in the report so the editor can check your check.

**5. Grade each finding by what the editor has to do**, and write it up. See the output section.

## Where errors actually hide

These are the checks with the highest yield. Run them deliberately rather than hoping they surface.

**Entry into force, and specifically its inversion.** Russian federal laws routinely say "вступает в силу со дня официального опубликования, за исключением статьи N" — and digests routinely flip this into "вступает в силу с [the date in article N], за исключением отдельных положений." That single flip moves the operative date of the main change by months. Read the final article of every law in full, and check which way round the exception runs.

**Scope narrowing.** A decree exempts two categories; the digest names one. An act applies to organisations *and* individuals; the digest says organisations. Read the enumeration in the act and count the limbs against the digest.

**A parenthetical promoted to a rule.** Statutes often give a broad ground and then illustrate it — "создание угрозы безопасности (в том числе в случае выявления неэффективности мероприятий против БПЛА)". Digests love the vivid example and drop the broad ground. Check whether each listed item is a limb of the enumeration or an illustration inside one.

**Transitional provisions.** The paragraph that says what happens to relations that arose before the act, or that lets someone recover money frozen during the gap, is usually the most practically important paragraph in the whole act and the one most often omitted.

**Terminology drift.** "Беспилотные воздушные суда" is not "беспилотные летательные аппараты"; "менее 50" is not "не более 50"; "невосстановление или несвоевременное восстановление" is not "затягивание сроков восстановления". These look like editing polish and are substantive.

**Legal conclusions presented as quotations.** "Вступает в силу по истечении 7 дней после опубликования" may be a correct inference from the general rule for government acts, even though the act itself says nothing about entry into force. The inference can be right and still needs to be marked as an inference, because the reader will otherwise go looking for a sentence that isn't there.

**Inherited errors.** Regulators put mistakes in their own explanatory notes. When the digest reproduces one, it is still an error in the digest — report it, and say where it came from, because that tells the editor the citation won't resolve for readers either.

**Staleness against the digest's own period.** If the document covers a period and mentions a hearing, deadline or effective date that falls *inside* that period, a future tense ("рассмотрит", "будет назначено") is already wrong on the day of publication.

## Output

Report in the language of the document under review. Group findings by the action required, not by the order they appear in the document — the editor is triaging:

1. **Ошибки** — contradicts the act. Fix before publication.
2. **Пропуски** — no false statement, but something material is missing (most often an effective date or a transitional rule) and its absence misleads.
3. **Требует сверки** — the numbers don't reconcile, or the primary source was unreachable and the claim rests on secondary reporting. Say which.
4. **Мелкие неточности** — wording, citation quality, an inference presented as a quotation. Editor's discretion.
5. **Подтверждено без замечаний** — an explicit list of what was checked and matched.

For each finding in groups 1–3, give: what the document says (quoted), what the source says (quoted, with the article or paragraph), why it matters in practice for a reader acting on it, and a link to the primary source. The "why it matters" line is what turns a list of corrections into something an editor can prioritise; without it every finding looks equally urgent.

Then close with **what could not be verified** and why — unreachable databases, unreadable text layers, claims with no public source. Be specific. This section is not an admission of failure; it is the part that tells the editor where their own residual risk is.

Group 5 matters more than it looks. Most of a competent digest is correct, and an editor who only sees a list of problems has no way to know whether you read the whole thing or skimmed three paragraphs.

## Delivering it

Match the medium to the size of the job. A handful of findings belongs in the chat reply. A full document review — a dozen findings across a dozen acts, each with quotations and links — is a reference the editor will work through and probably forward to the authors, so publish it as an artifact and hand over the link, with the headline findings summarised in the chat reply so the user gets the substance without opening anything.

Either way, lead with the count and the single most consequential finding. "Four errors, one of which moves an effective date by two months" is the sentence the user needs first.

## Scope

This is verification against published sources, not legal advice and not a substitute for a lawyer's review. Confirming that a digest accurately describes an act says nothing about whether the act was correctly interpreted for a particular client's situation — if the user is relying on the document for a transaction or a filing, say so plainly once and move on.

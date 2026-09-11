---
name: institution-history
description: Deliver a structured historical brief on one legal or economic institution per issue — genesis, evolution across legal systems, and how it took root in Russian law, closed with a short note on why it matters in practice today. Sources cited inline when found; nothing invented. Fires automatically via a Tue/Fri/Sun 14:00 Moscow routine, cycling through capital-markets, banking and corporate-law institutions without repeating one already covered; also usable on demand for "расскажи про историю [института]".
---

# Institution History Brief

## Purpose

One legal or economic institution per issue, researched properly and
written up as a piece worth reading — for a lawyer working in capital
markets, financial and banking law who wants the backstory behind the
tools they use, not a Wikipedia summary.

## Picking the institution

- Read `references/covered-institutes.md` in this skill folder first. It
  lists every institution already sent, with the date. Never repeat one
  that is already there, even under a different name for the same idea.
- Seed order for the first four issues, in this order:
  1. Право собственности на землю
  2. Биржа
  3. Право удержания
  4. Производный финансовый инструмент
- After the seed four are covered, keep going with institutions from the
  same neighborhood — capital markets, banking, corporate and secured
  transactions law. Examples, not a fixed list: вексель, ипотека,
  доверительное управление имуществом, депозитарная расписка, номинальный
  держатель ценных бумаг, договор репо, эскроу, независимая гарантия,
  синдицированный кредит, центральный контрагент и клиринг, конвертируемый
  заём или облигация, субординированный заём, институт делистинга и
  раскрытия информации на бирже. Use judgment: something the reader would
  recognize as "an institution," not a narrow procedural rule.
- After an issue goes out, append one line to
  `references/covered-institutes.md`: date, institution name, and a
  one-line note on what was actually covered, so a later issue does not
  retread the same ground under a different label.

## Researching it

- Search live in both directions: where the institution first took a
  recognizable legal shape (Roman law, English common law, lex mercatoria,
  a continental codification — whichever actually applies) and its
  specific path into Russian law (imperial, Soviet, post-1991
  codification). Never answer from memory alone — dates, which code first
  codified something, and which article says what are exactly the details
  that go quietly wrong when reconstructed from training data instead of
  checked.
- Never invent a source or a link. When a good article, essay, or academic
  piece turns up along the way, link it inline exactly where it supports
  the claim it backs. If nothing citable beyond an unlinkable textbook or
  commentary turns up, say so rather than forcing a link onto it.
- On Russian-law specifics — which code, which article, what year — check
  the primary text (`publication.pravo.gov.ru`, or a reputable digitized
  text for older acts), the same standard the rest of this repository
  holds itself to for current law.

## Writing it up

- Length: 1200-1800 words by default. Go longer when the institution's
  history genuinely earns it — real turning points, real controversy, real
  relevance to today. Don't pad a thin history to hit a word count, and
  don't cut a rich one short to stay under it.
- Structure: a short opening on what the institution is and why it's worth
  the next fifteen minutes, then its genesis, then its evolution — the
  turning points, not a bare timeline — then how and when it entered
  Russian law and what it looks like there today. Close with a short block
  (a paragraph or two) on why this matters for current practice: how the
  institution actually shows up in a capital-markets or banking lawyer's
  work now.
- Write in Russian regardless of the language of the sources; translate
  and adapt rather than leaving long quotes untranslated.
- This is a reading piece, not a client memo: no firm template, no
  numbered clauses, no citation apparatus beyond the inline links.

## Delivering it

Reply directly in the chat of the session this fires into. No separate
document.

## Cadence

Normally triggered by a Routine at 14:00 Moscow time on Tuesdays, Fridays
and Sundays, opening a fresh session each time. Also fine to run ad hoc
("расскажи про историю выкупа акций" and similar) at any other time — in
that case, still check and update `references/covered-institutes.md`
unless the user says the request is a one-off that shouldn't count toward
the cycle.

---
name: grilling
description: Interrogate the user relentlessly about a plan, a research brief, a deal, a document or an idea until nothing is left silently assumed. Maps the subject as a decision tree and works it in rounds, asking every question whose prerequisites are already settled, each with a recommended answer, so a round can be answered by number. Facts are the agent's job to find; decisions are the user's. Use when the user wants to stress-test their thinking, when a brief is too vague to research or draft against, or on any "grill" trigger phrase ("погоняй меня", "допроси", "grill me", "устрой допрос", "прожарь идею"). Other skills in this repository invoke it as their intake step.
---

# Grilling

Interview the user relentlessly until you reach a shared understanding. Map the subject as a **design tree**: every decision branches into the decisions that hang off it.

Adapted from Matt Pocock's `grilling` skill (github.com/mattpocock/skills, MIT). The round mechanic and the question format are his; the fact-finding rules and the seed axes below are this repository's.

## Rounds and the frontier

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask *now* without guessing at answers you have not heard yet.

Ask the whole frontier in one round. Number each question, give it a title, and state your own recommended answer. Then stop and wait for the user's answers before the next round.

A question whose answer depends on another question still open in this round belongs to a **later** round, not this one. Two questions never share a round if one settles the other.

Each set of answers reshapes the tree: settled decisions push the frontier outward and unblock what depended on them. Recompute the frontier and ask the next round.

Count rounds, not questions. Forty questions across four rounds is an ordinary session; forty questions across forty rounds means the tree was never built. There is deliberately **no cap** on the number of questions: some briefs need three, some need fifty. If a session is running very long, the cause is almost always that the scope is too big. Say so and propose splitting it, rather than truncating the interview.

## Question format

```
❓ **Q1** - **<заголовок вопроса>**: <тело вопроса, может быть несколько абзацев, может содержать варианты выбора>

➡️ <рекомендуемый ответ>

---

❓ **Q2** - **<заголовок вопроса>**: <тело вопроса>

➡️ <рекомендуемый ответ>
```

- **Ask in Russian** unless the user is writing in another language. The mechanics of this skill are language-neutral; the conversation is not.
- The `➡️` recommendation goes on its own line. It is what lets a busy user answer "1 да, 2 второй вариант, 3 нет, вот почему" instead of quoting questions back.
- **Word the question so that agreeing with the recommendation is not answering "no" to the question.** A recommendation that argues against its own question's wording is the known rough edge of this format; avoid creating it.
- **No em dashes in the questions.** Use colons or semicolons. This matches the house style of the client-facing skills in this repository.
- Separate consecutive questions with a horizontal rule.
- Give the recommendation honestly, including when it is "не делать этого". A recommendation you do not believe wastes the user's only real job here.

## Facts are yours, decisions are theirs

**Finding facts is your job, never the user's.** When a frontier question needs something the environment can settle, go and find it. In this repository that means, before asking:

- **Company facts** (выручка, численность, собственники, лицензии) come from ГИР БО, ЕГРЮЛ and Прозрачный бизнес, not from the user's memory. See `research-analyst/references/source-playbook.md`.
- **What a statute actually says** comes from `publication.pravo.gov.ru` or the regulator's own site, not from asking the user to recall it.
- **What is already in the repository or the working directory** comes from reading it.
- **Market and competitor facts** come from a search, dispatched as a sub-agent where the search is broad.

Do not block on fact-finding. A running exploration is an unsettled prerequisite, so only the questions downstream of it wait; ask the rest of the frontier now and fold the findings into the next round.

**Decisions are the user's.** Scope, budget, risk appetite, who the client is, what counts as good enough, what to cut: put each to them and wait. An agent running this skill that answers its own decision questions has broken the skill, not interpreted it liberally.

"Не знаю" is a real answer. Treat it as a signal that the question cannot be settled by talking, and say what would settle it: a document to pull, a number to look up, a prototype to build, a call to make. Do not rephrase the same question three ways to extract a guess.

## Seed axes for this repository

The tree is built from the subject, not from a checklist. These are starting branches that have proved load-bearing here, not a script, and most sessions will discover branches worth more than any of them:

**For research briefs** (`research-analyst`): which decision the research feeds; whose money and whose risk; geography and jurisdiction; segment and who signs; capital, horizon and hard no-go zones; what has already been read or tried; what result would change the user's mind.

**For client documents** (`legal-digest-alert`, `legal-opinion-ru`): who the reader is and what they will do with the document; deliverable type and register; the coverage period or the specific instrument; which practice areas matter to this client; what the client already knows; the deadline; what must not be said.

## Ending the session

The frontier being empty does not end the session. **Ask the user to confirm that you have reached a shared understanding, and wait.** Do not start researching, drafting or building until they say so.

When they confirm, hand over a compact summary of what was settled: the decisions, the assumptions that remain unresolved, and the facts you looked up along the way with their sources. That summary is what the next skill consumes, and it goes in the same conversation. Do not start a fresh session to use it: the context just built is the whole point.

## It is working if

- A round arrives as a numbered list, each question with its recommendation on its own line, answerable by number.
- Nothing in a round needs another question in the same round answered first.
- Later rounds ask things the first round could not have asked.
- You looked facts up instead of asking about them.
- The user disagrees with something. A session with no pushback is a session that was not needed.
- Question count stays high while round count stays low.
- It stops and asks for confirmation instead of starting the work.

## Note for skills that invoke this one

Naming a skill does not reliably load it. When another skill in this repository calls for a grilling session, read this file directly rather than assuming it is already in context. The tell that it was not loaded: an interview that arrives as one undifferentiated wall of questions with no recommendations attached.

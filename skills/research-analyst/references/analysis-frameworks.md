# Analysis frameworks

These are the methods that produce the parts of a report a reader cannot get from a search engine. Each one is here because it converts public information into a conclusion that is not publicly stated anywhere.

## Sizing: build it, don't cite it

A published market size is someone's marketing. Build the number instead, from quantities that can be observed:

```
Рынок = (носители проблемы) × (частота покупки в год) × (средний чек) × (доля, реально доступная к обслуживанию)
```

Each input gets its own source or its own explicit estimate. Then compare the result with any published figure and **explain the gap** — that explanation is usually the most interesting paragraph in the section. Published numbers run large for predictable reasons: they count an adjacent category, count revenue at retail prices where the operator sees wholesale, or project a CAGR off a base year that was an anomaly.

Sanity checks that cost nothing and catch most errors:

- **Cross-check from the supply side.** Number of operators × plausible revenue per operator should land near the demand-side number. In Russia this is directly checkable: count entities under the relevant ОКВЭД, pull revenue for a sample from ГИР БО, extrapolate. When the two methods disagree by more than about 2×, one of the assumptions is wrong and finding out which is the finding.
- **Per-capita reality test.** Divide by population or households. If the implied spend per household is implausible against known income levels, the number is wrong regardless of how it was derived.
- **Check the CAGR's arithmetic.** A stated "14% CAGR to 2030" implies a specific end value; if the source's own end value doesn't match its own base and rate, the report is unedited marketing and nothing in it should be cited.

Always distinguish **TAM / SAM / SOM** explicitly, because conflating them is the most common way a business case is inflated: everyone who has the problem, the subset reachable given geography, channel and regulation, and the share realistically winnable in three years.

## Where the money actually sits: the margin pool

Map every link between the end customer's wallet and the raw input, and estimate what share of the final price each link keeps. Filed accounts (ГИР БО, 10-K segment data) make this tractable for at least some links, and one known link often lets you back out the rest.

This is what answers the question the market-size number cannot: a category can grow 30% a year while every operator in one link earns nothing, because a single link — usually the one that owns the customer relationship or a scarce input — takes the margin. Enter the growing link, not the growing market.

Watch specifically for: who owns the customer relationship and the data; where switching costs actually bind; which link is a regulated bottleneck; and which link is a commodity with excess capacity.

## Audience psychology

Demographics describe who buys; they never explain why. Build the picture from four things instead:

1. **The job.** What is the customer trying to get done, stated as an outcome rather than a product category. The competition is whatever they currently hire for that job — often a spreadsheet, an in-house employee, or doing nothing at all, not the obvious rival.
2. **The triggering event.** Nobody buys because the problem exists; they buy because something happened. An audit, a hire, a breakdown, a regulation, a birth, a move, a bad quarter. Naming the trigger is what makes marketing targetable and what makes a sales motion timeable.
3. **The switching barrier.** What holds them where they are: contract, sunk data, retraining, internal politics, the risk that switching gets someone blamed. In B2B the barrier is usually career risk, not price — and a report that says "цена" when the answer is "никто не хочет отвечать за неудачное внедрение" is wrong in a way that costs the reader money.
4. **Their own words.** Harvest verbatim phrasing from reviews, complaints, forum threads and search queries. Customers describe problems in vocabulary that differs sharply from vendor vocabulary, and the customer phrasing is simultaneously the insight and the ad copy. Quote it directly in the report.

**Stated versus revealed preference.** People say they want privacy and click "accept all"; they say price is the deciding factor and buy the recognisable brand. Where survey data and behavioural data conflict, behaviour wins and the gap itself is worth a paragraph. Prefer sources that record what people did — transactions, search volumes, churn, review complaints — over sources that record what they said.

## Hidden patterns: the leading-indicator sweep

Run this list deliberately. It is where "impossible to find with a basic search" actually comes from — each item is public, dull to check, and months ahead of the reporting.

- **Hiring.** Roles, seniority, location and salary bands. A company hiring compliance officers is expecting regulation; hiring enterprise sales after years of self-serve is moving upmarket; posting the same role repeatedly is failing to retain.
- **Pricing and packaging archaeology.** Diff the pricing page across years in the Wayback Machine. A removed free tier, a new usage cap, a renamed plan, a price rise not announced anywhere — each is a margin decision with a date.
- **Terms of service and changelog diffs.** Where platform risk becomes visible before it hits partners.
- **Trademark and patent filings.** Names and claims filed six to eighteen months before launch.
- **Procurement records.** Who is buying, at what price, and whether they renewed with the same supplier.
- **Regulatory pipeline.** Draft acts in public consultation, enforcement patterns, licence-register churn. Enforcement priorities are a business model for compliance vendors and a mortal risk for someone else.
- **Financial-statement texture.** Not just revenue: receivables growing faster than revenue means the customers are struggling or the terms were loosened to hit a number; inventory building against flat sales means demand is softening; a jump in intangible assets means something was bought or capitalised.
- **Executive and ownership changes** in ЕГРЮЛ, and departures of CFOs and heads of a specific product line.
- **Capacity signals** — new capex, closed sites, leases taken or dropped.
- **Distribution changes** — a company that starts selling through a channel it previously refused is short of demand.
- **What everyone stopped saying.** Compare this year's messaging to last year's. A metric a company stopped reporting is a metric that got worse.

Then look for the **divergence**: the point where two of these indicators disagree with each other or with the public narrative. The narrative says consolidation while entity counts rise; the reports say demand is strong while the leader quietly cut prices. Divergences are where the report earns its fee.

## Competitive advantage: does the moat hold

For each advantage a player claims, force a verdict. Only a few things are actually defensible: economies of scale that bite at the relevant volume, network effects that are same-side or cross-side and actually observable, switching costs measured in time and risk rather than asserted, a regulatory or licence position that is hard to replicate, a scarce input under contract, and brand where it demonstrably supports a price premium.

Everything else — a feature, a head start, a partnership, "our team", a proprietary algorithm with no data advantage behind it — is a lead, not a moat, and should be labelled as one. The test: **if a well-funded competitor decided to copy this next quarter, what specifically stops them, and how long does it hold?** If the answer is "nothing, it just takes effort", say so.

Also examine the **incumbent's constraint**, which is often the real opportunity: what the leader cannot do without damaging its existing business — cannibalising its own margin, upsetting a channel, breaking a contract, or serving a segment its cost structure can't reach.

## Risks

Split them, because treating a fatal risk and an annoying one as the same kind of item is what makes risk sections unreadable.

- **Kill risks** — the thesis does not survive this. Regulatory prohibition or licensing you cannot obtain, dependence on one platform that can change its rules unilaterally, customer concentration, unit economics that never close because CAC exceeds lifetime margin, a single supplier or a single jurisdiction, a key-person dependency.
- **Manageable risks** — cost, timing, competitive response, execution.

For each: what specifically to watch (an observable), the rough probability, and what to do if it materialises. A risk without an observable trigger is decoration.

## Business ideas that survive contact

An idea in this report is not an idea until it has all four of these:

1. **Why now.** What changed in the last year or two that makes this possible or necessary and was not true before — a regulation, a price collapse, a platform opening, a behaviour shift, an incumbent's retreat. No "why now", no idea; the absence usually means it has been tried and failed.
2. **The first customer**, named specifically enough to contact — a segment, a role, a trigger, not "малый бизнес".
3. **The cheapest test that could kill it**, runnable in weeks, with what it costs and what result counts as a pass. Landing page plus paid traffic, ten sales calls, a manual concierge delivery for three customers, a pre-sale.
4. **Why it hasn't been done.** There is always a reason. Either it is a bad reason that has expired (that is the opportunity), or a good reason that still holds (that is the warning). Guessing "nobody thought of it" is almost always wrong.

## Predictions

A prediction that cannot be scored is not a prediction. Each one gets:

- a specific claim, in terms that will be unambiguously true or false;
- a **probability** — round numbers, no false precision;
- a **horizon** with a date;
- an **observable trigger**: the first thing that would appear if this is happening, and roughly when it should appear.

Anchor on base rates before reasoning from the specifics — how often does an entrant actually displace a leader in this kind of market, how often does a draft act pass in the same session, how long do these deployments typically take. The narrative reason for a forecast is worth less than the historical frequency of the outcome.

Close with **what would change my mind**: the two or three observations that would force a revision. That section is what makes the whole report credible, and it is the first thing an experienced reader looks for.

## Analyst anti-patterns

Delete on sight:

- A sentence equally true of any industry ("рынок фрагментирован", "растёт роль цифровизации").
- A trend claim with no series behind it — a direction with no numbers on either end.
- A conclusion resting on a single source, especially a vendor's.
- Precision that the inputs cannot support.
- A recommendation with no cost, no first step and no way to be wrong.
- Confusing correlation with mechanism: state the mechanism, or state that you only have the correlation.
- Survivorship bias — studying the winners and inferring what works, without looking at who did the same thing and died.

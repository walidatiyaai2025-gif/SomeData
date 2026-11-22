# v0.7 — Egypt & Arab Digital Products: Ads, Subscription, Hybrid
**22 November 2026 | status: DESK RESEARCH / VALIDATION DESIGN ONLY | Not an investment approval.**

## Executive decision
Expand the previous Egypt Micro-SaaS study **without resetting it**. The existing [v0.6 ranking](./Current-Ranking.md), [source of truth](./Idea-Registry.json) and v0.1–v0.6 history remain frozen. Add 14 candidates EG-049..EG-062 and non-destructive model-suitability overlays for eight existing ideas in [v0.7 JSON sidecar](./Monetization-Opportunity-Registry-v0.7.json). There are now **62 ideas considered across history**, but 48 retain their legacy classification (41 desk-scored + 7 archived), and 14 are **new unvalidated** candidates. Do not call 62 investment-grade scored ideas.

**Three distinct routes:** (A) Ad-first, (B) subscription-first, (C) hybrid ads + optional paid. No single numerical leaderboard combines different business models. All scores below are **analyst fit hypotheses under a new axis**, not the previous market scores, not Egypt eCPM benchmarks, not probability of success. Nobody has measured retention, CPM, CPI, payments, CAC, refunds, traffic or revenue for these candidates.

## 1. Investor constraints and where this differs from v0.6
- Egypt-first, Arabic-friendly; promotion, user onboarding, payments and support must operate remotely. Other Arab markets require per-country policy, payout, taxation and acquisition experiments.
- Functional proof with generated fixtures and known outputs before relying on client data. **Functional correctness cannot prove market demand**.
- Monetization choice follows frequency and customer segment. A rare-use PDF converter may work as organic search, yet have poor monthly subscription retention.
- Preserve historic exclusions **for the subscription thesis**; an archived entertainment/quiz idea can be tested under ad economics as a **new variant**, not silently un-archived or treated as previously validated.
- The old **90-day free full-feature** offer was a test hypothesis for SaaS; **not** mandatory for ad-first/hybrid, where it could suppress feedback on paid demand. Never charge without informed consent.
- Default campaign screening budget **USD 100 total** for initial tests, adjustable only after decision. Do not present the earlier $500 proposal as already spent.

## 2. Scoring model and reading the rankings
This is a qualitative desk scoring matrix on 0–10; weights are declared and preserved in the v0.7 JSON:
- **Ad-first:** 25% organic acquisition, 25% repeat usage, 15% ad inventory and policy safety, 15% competition defense, 10% operating margin, 10% remote execution.
- **Subscription-first:** 25% recurring paid value, 20% payment intent hypothesis, 20% remote acquisition, 15% competition defense, 10% unit economics, 10% independent testability.
- **Hybrid:** 20% free activation, 20% upgrade value, 20% repeat usage, 15% ad-policy safety, 15% unit economics, 10% remote execution.

No score >=9 because independent commercial verification is absent. The numbers are subjective judgments organized for falsifiable prioritization; do not read two-decimal precision as statistical measurement. Ties do not imply equivalence; ranking order is score then ID.

### A — Ad-first research shortlist (not investment ranking)
| Priority | ID | Idea | v0.7 ad-fit /10 | Winning *hypothesis* | Main blocker |
|---:|---|---|---:|---|---|
| 1 | EG-050 | Daily Arabic word puzzles (adult audience) | **6.8** | Repeated sessions + original puzzles | Very crowded games; cheap organic traffic not shown |
| 2 | EG-053 | Offline short logic puzzles | 6.5 | Casual repeat levels | D7/D30 and ad UX may collapse |
| 3 | EG-052 | Daily general-knowledge quiz for adults | 6.3 | Daily original content | Editorial load; retention unverified |
| 4 | EG-051 | Egypt household utilities calculator hub | 6.1 | Search demand by task | Many free apps; tariff maintenance |
| 5 | EG-055 | Arabic printable template library | 6.0 | Organic evergreen pages | AdSense quality/SEO and licensing |
| 6 | EG-059 | Home/car light maintenance reference | 5.9 | Search-driven tutorials | Accuracy, safety and trust |
| 7 | EG-060 | Five-minute English for adults | 5.8 | Daily micro-lessons | Duolingo-class competition |
| 8 | EG-042 | Existing Egyptian electricity calculator | 5.7 | Legacy idea gains ad-use case | Existing alternatives; one-off visits |

**Ad-only default outcome: HOLD** until a measurable organic channel and a realistic DAU/impressions yield are found; ads are not a substitute for distribution.

### B — Subscription-first research shortlist
| Priority | ID | Idea | v0.7 subscription-fit /10 | Status |
|---:|---|---|---:|---|
| 1 | EG-047 | Arabic agency release regression guard | **7.3** | **Carry forward v0.6 conditional experiment**, not production |
| 2 | EG-046 | Arabic i18n / RTL release checks | 7.1 | Conditional: same buyer and repeat CI usage |
| 3 | EG-044 | Arabic website RTL checks | 7.0 | Must outperform free alternatives in repeated work |
| 4 | EG-009 | Service handover proof | 6.9 | Stronger operational need, harder remote acquisition |
| 5 | EG-058 | Arabic/English job interview practice | 6.5 | New, job-search episodic; payment intent unknown |
| 6 | EG-040 | Arabic CSV/Excel quality checker | 6.3 | Free spreadsheet alternatives |
| 7 | EG-043 | Arabic field-service workflow | 6.2 | Human support can dominate margin |
| 8 | EG-057 | Microbusiness quote/invoice | 6.2 | Crowded and accounting-scope risk |

**Subscription decision: retain EG-047 as leading validation candidate.** v0.6 owner fit was 7.7 by a different weight method; v0.7 score 7.3 is not a retroactive score change. Test its value and willingness-to-pay before building.

### C — Hybrid research shortlist
| Priority | ID | Idea | v0.7 hybrid-fit /10 | Upsell assumption |
|---:|---|---|---:|---|
| 1 | EG-060 | Practical adult English micro-learning | **6.7** | Offline packs / personalized learning plan; free lessons remain useful |
| 2 | EG-058 | Job interview rehearsal | 6.6 | Extra practice sets/feedback without trapping job applications |
| 3 | EG-049 | **School PDF** | **6.4** | Organized subject library, batch ops, optional ad-free |
| 4 | EG-052 | Daily adult quiz | 6.3 | Optional themed packs and no ads |
| 5 | EG-057 | Quotes/invoices for freelancers | 6.1 | Pro templates / export history |
| 6 | EG-062 | University planner | 6.0 | Semester views / reminders, no required ads |
| 7 | EG-054 | Arabic PDF/image web toolbox | 5.5 | Batch/priority processing only if cost allows |
| 8 | EG-061 | Arabic CV builder | 5.3 | Original templates, one-off purchase may beat subscription |

**Hybrid default outcome: compare EG-060 / EG-058 / EG-049 with deliberately separate acquisition funnels.** High competitiveness and consumer churn mean none is approved for growth spending.

## 3. School PDF — special evaluation
**Scope already contemplated:** Flutter Android/iOS; capture camera/gallery to PDF, automatic edges/perspective, compression, ordering and sharing, plus organized study documents and optional notifications. Study-only here: no app changes and no release claims.

**Competitive evidence:** Google Drive scanning (M09), Adobe Scan (M10), vFlat book/scan/OCR (M11). This means **scan-to-PDF is table stakes**. Distinct proposal to test: homework submission that reliably fits upload-size limits, consistent file naming by course/date, high-quality page ordering, one-tap share, and an archive. Benchmark 20 mocked homework submissions against all three rivals on time, file size, legibility and errors.

**Ads restrictions:** children are part of a realistic School PDF audience. Implement neutral age-screening for mixed audiences and certified SDK/ad treatment for children on Google Play (M05), follow Apple's Kids Category and privacy/ad requirements when applicable (M06). No targeted advertising to children and no disruptive interstitial in an active scan/upload flow (M04). Do not require push permission to use core app; protect student documents and avoid ad data leaking from filenames/content. Treat an adult/university-only test cohort separately from minors. The safest initial test is **no ads to minors** while policy review and product age declaration remain open.

**Counterfactual:** a student taking one PDF per week can produce less ad inventory than a daily game. No economic projections based on downloads alone. No forced ad before document delivery; users must be able to finish urgent homework submissions.

## 4. Candidate coverage: every domain remains open
The new 14 span education (EG-049,052,060,062), games (050,053), websites/tools (051,054,055), household/finance (056), small business (057), career (058,061), and practical content (059). Existing v0.6 B2B utilities remain included in subscription research. See the complete JSON register for scores under all three models.

**Not currently eligible:** gambling, deceptive financial offers, copyright scraping, adult content, restricted youth targeting, unlicensed regulated advice, user-upload monetization without consent, intrusive notifications. These are restrictions, not new revenue ideas.

## 5. First experiments and gates
1. **Proof before traffic:** For shortlisted products, construct 30 representative fixtures with expected results and 10 adversarial cases (offline, Arabic RTL, malformed files, age gates, disabled ads, duplicate events); compare with at least 3 incumbents. Record PASS/FAIL and test artifacts.
2. **Distribution pre-check:** Make one demo/landing page per concept with a truthful value proposition and price/ad disclosure; test 3 search or store keywords with current measurements; no claims of demand before real impressions and conversion.
3. **USD 100 exploration** (hypothetical): $30 adult puzzles, $30 adult hybrid learning, $30 School PDF **adult-only cohort**, $10 reserve. Compare qualified visits and first core action; do not automatically spend the reserve. For minors do not target age-restricted marketing segments without compliance review.
4. **Retention/payment gate:** Run limited pilot cohorts to collect activation, D1/D7/D30 (games) or W1/W4/semester (School PDF) and organic share. For paid: real checkout eligible for seller/country and clear consent, free→paid, 2nd paid renewal, refunds. For ads: realized impressions, match rate, eCPM, ARPDAU, and net cash.
5. **Kill:** zero defensible advantage over top free alternative, ads breach policy or impede task, no measurable repeat use, or real acquisition cost exceeds conservative realized LTV.
6. **Investment GO:** technical correctness + independently observed demand + compliant payout + measurable margin + valid second renewal (subscriptions) or realized ad cohort with cost-aware payback (ads). Else HOLD / PIVOT / STOP.

All thresholds in the [validation plan](./Monetization-Validation-Plan-2026-11-22-v0.7.md) are pre-registered research heuristics, **not proof**. The companion [economics](./Monetization-Unit-Economics-2026-11-22-v0.7.md) demonstrates why low country CPMs make ad-only paid traffic particularly vulnerable.

## 6. Data ethics, cross-border rollout and financial caveats
- Do not equate internet users or mobile connections (M01/M02) to addressable active users, distinct paying buyers, or advertisers.
- Local currency payments and IAP policies vary. Google Play requires its billing system for covered digital features, with exceptions (M15); Apple subscriptions have StoreKit requirements (M16). A website may have different payment rails than an app.
- App AdMob eCPM and web page RPM are different metrics. Conversion from USD to EGP requires an observed FX rate at reporting time; never silently add currencies.
- An ad partner account being pending/declined means **zero guaranteed ad delivery**, even if the app works. Test eligible account access before factoring earnings.
- Keep ad identifiers and user content separate. For students and personal documents, privacy notices, deletion/export, permissions and country-specific legal checks are gating requirements.

## 7. Record of recommendation
**v0.7 decision:** RESEARCH EXPANSION ACCEPTED, PRODUCT BUILD NOT AUTHORIZED. Subscription path: validate EG-047. Ad path: compare EG-050 and EG-052 plus EG-055 organic SEO, not a game studio commitment. Hybrid: compare EG-060, EG-058 and School PDF (EG-049). No investor-grade rating ≥9, no earned revenue, and no actual campaigns were executed in this research deliverable.

**Read:** [evidence](./Monetization-Evidence-2026-11-22-v0.7.md) · [economics](./Monetization-Unit-Economics-2026-11-22-v0.7.md) · [validation plan](./Monetization-Validation-Plan-2026-11-22-v0.7.md) · [machine-readable overlay](./Monetization-Opportunity-Registry-v0.7.json) · [legacy v0.6 ranking](./Current-Ranking.md).

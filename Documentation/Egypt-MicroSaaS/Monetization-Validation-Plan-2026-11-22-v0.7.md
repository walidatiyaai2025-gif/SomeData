# v0.7 — Validation program before investment
**2026-11-22 | planned, NOT STARTED.** This document is a preregistration of experiments; it does not record users, campaigns, reviews, payments or successful releases.

## 0. Baseline (zero is not a guessed metric)
| Evidence | Current |
|---|---|
| Products built for EG-049..062 | NOT BUILT / not evaluated here |
| Customer interviews and qualified intent | NOT MEASURED |
| Campaign spend | $0 recorded in this study |
| Store downloads / app installs | NOT MEASURED |
| Active users / ad impressions / country eCPM | NOT MEASURED |
| Paid customers / second renewal / refunds | NOT MEASURED |
| Ad partner account eligibility / payouts | NOT VERIFIED |
| Technical fixture tests (products) | NOT RUN |
| Documentation schema/arithmetic CI | Separate automated check when PR runs |

## Stage 1 — 7 days technical proof, without customers
- **EG-049 School PDF**: 20 synthetic homework sets in Arabic/English, 10 negative cases (angled pages, glare, low-light, RTL, offline, PDF compression threshold, missing permission, cancel during export, large file, user-content leakage); define expected PDF page count/size/visual reading results. Benchmark Drive/Adobe/vFlat for same tasks. Demonstrate no forced ads during task and no noncompliant minor targeting.
- **EG-050/053 puzzles**: 100 unique original levels, deterministic solver answer, offline mode, ad disabled and network failure tests, no misleading reward; compare daily play friction with 3 actual Google Play competitors.
- **EG-052/060 adult learning**: 100 original questions/lessons and reference answers; check Arabic RTL, progress and content licensing; limit adult age segmentation.
- **EG-055 web templates**: 30 original printable files with clear reuse permissions and correct output; audit 20 high-intent search phrases and 3 competing sites.
- **EG-047/046**: keep existing simulated agency release-check proof from v0.6; do not replace required accuracy benchmarks with a new monetization score.
- Test gate: >=95% of declared deterministic functional fixtures match expected outputs, **zero critical privacy, safety, children-ads or billing violations**, and honest parity/advantage table against three rivals. Threshold is an internal experiment heuristic, not a market benchmark.

## Stage 2 — 14 days remote demand discovery (separate audiences)
Run **3 separate landing/demo funnels**, adult Arabic word puzzle, adult English practice, and School PDF university 18+ (never merge ages, channels or countries). Keep v0.6 Agency EG-047 as its own B2B experiment. Channels: permissible SEO content, Google Play store-listing experiment if product exists, controlled social/video creative where permitted, approved communities. Claims must describe a demo accurately; no fake waitlist metrics.

Budget cap total: **$100**: $30 puzzles, $30 English, $30 university School PDF, $10 contingency. Hold spending if privacy/policy/payout prerequisites incomplete. Track campaign/ad set, reach, clicks, landing conversions, qualified intent and first real feature use. Never infer true CAC from CPC alone.

Pre-registration hypothesis for moving to pilot: at least **10 qualified discovery conversations per shortlisted niche**, at least 5 independently expressed strong willingness-to-pay indications for paid features, or 5 meaningful sessions showing self-initiated repeat use for ad-first. If unattainable, record the shortfall; do not declare success from likes or downloads.

## Stage 3 — 30+ days real product pilot (after technical and policy clearance)
- **Ad-first metrics:** activated installs, DAU/MAU, D1/D7/D30 retention by *acquisition cohort*, sessions, valid realized ad impressions/DAU-day, match rate, eCPM by format/country, gross revenue, reconciled net payouts, app crashes and support.
- **Subscription metrics:** trial→paid rate with real collected payments, first and second paid renewal, churn, refunds, chargeback rate, net ARPPU, contribution margin, actual CAC and payback. Allow time for the second renewal; cannot compress it into 7 days.
- **Hybrid:** free vs paid cohort; removing ads from paid; impact of ad experiment on first task completion and D7; display ads only at policy-compliant breaks, optional rewards and premium use-value. Avoid intrusive tests on children's cohorts.
- **School PDF guard:** measure W1/W4 repeat scan & homework submission success during school term AND an out-of-term cohort; distinct minors/parents/university groups only with justified consent and declarations.
- Pilot thresholds as *hypotheses* for next round: D7 >=15% for adult casual category, W4 >=15% for university document workflow **only as internal screening**, not external benchmarks; sufficient sampled paying second renewals and ad revenue with positive unit contribution needed before investing. Do not promote a score to 9/10 from small-cohort noise.

## Stage 4 — decision table
| Gate | GO only if… | PIVOT / STOP if… |
|---|---|---|
| Compliance | Required store/age/payment and privacy checks signed off | Children's targeting/ad policy failure, no lawful ad access |
| Technical | Correctness and security fixtures independently reproducible | Core task fails or outputs cannot beat free rivals |
| Acquisition | Qualified activated users acquired at measured cost | Ads spend buys only clicks or one-time installs |
| Ad economics | Reconciled realized cohort LTV contribution plausibly covers CAC/variable cost | Required DAU and frequency unattainable |
| Paid economics | Real paid renewals, net contribution and payback in acceptable range | Willingness-to-pay absent or high refund/churn |
| Growth | Measured return use and no ad-induced drop in completion | Session gaming, invasive prompts or holiday collapse |

**No investment authorization** until each relevant gate is documented with signed/linked data. No "9/10" without source-based observed numbers and retention across renewal cycles.

## Required experiment recording
One row per channel + audience + country + cohort + period, storing: cohort_start, idea_id, product_version, age_group, channel, spend_currency, spend, qualified_leads, activated, DAU/MAU, D1/D7/D30, W1/W4, ad_impressions, realized_ecpm_currency, ad_revenue, processor_fees, premium_gross, refunds, second_renewals, net_contribution, evidence_link, approval_or_risk, STOP/PIVOT/GO.
Do not collect child identifiers or upload private School PDF files for analytics; aggregate and minimize data.

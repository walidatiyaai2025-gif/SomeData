# v0.7 — Monetization unit economics and cash limits
**22 November 2026. USD unless EGP explicitly named. Every eCPM, RPM, CPI, impression frequency, retention, conversion and cost below is a fictional sensitivity input — NEVER a published Egypt benchmark or achieved performance.** Definitions: [AdMob eCPM](https://support.google.com/admob/answer/15337570?hl=en) and [AdMob user metrics](https://support.google.com/admob/answer/10200963?hl=en-KW).

## 1. Ads: count realized impressions, never installs
Ad revenue = realized impressions / 1,000 × realized eCPM.
For a steady-state scenario: monthly realized impressions = daily active users (DAU) × **actual valid impressions per DAU per day** × days. In a simulation 30 days is conventional; actual reporting month may differ. If impression rate is already realized, do **not** multiply by fill/match rate again. Ad impressions depend on eligible geography, ads served, policy compliance, network, SDK, abandonment and frequency caps.

| Scenario (NOT forecast) | DAU | Realized impressions / DAU-day | eCPM USD | 30-day gross ad earnings USD |
|---|---:|---:|---:|---:|
| Constrained | 1,000 | 0.6 | $0.15 | **$2.70** |
| Illustrative base | 10,000 | 1.5 | $0.50 | **$225.00** |
| High-reach/high-yield stress | 50,000 | 2.5 | $1.50 | **$5,625.00** |
| School PDF low-frequency scenario | 10,000 | 0.8 | $0.50 | **$120.00** |

**Sensitivity:** at 1.5 impressions/DAU-day and $0.50 realized eCPM, $1,000/mo needs approximately **44,445 DAU throughout 30 days**. It is *not* 44,445 installs or MAU. Never count student age-ineligible impressions. Keep site traffic out of mobile ad math.

**CPI break-even proof:** Hypothetical paid CPI $0.10. If the acquired user produces 1.5 valid impressions on each of 20 **actual active days** over their lifetime, and eCPM is $0.50: gross ad contribution = 20 × 1.5 × 0.50 / 1,000 = **$0.015 per acquired user**. Paying $0.10 to acquire a $0.015 gross ad cohort destroys $0.085 before operating costs. At the same rate, **134 active days** would be required merely to exceed $0.10 gross, without discounting or churn. This illustrates why ads-first with paid acquisition is difficult in low-yield scenarios, not a prediction that Egyptian CPI is $0.10.

## 2. Web tools: do not reuse AdMob eCPM as page RPM
Web ad revenue = eligible monetized pageviews / 1,000 × achieved page RPM (USD).
For **30,000 monetized pageviews** at hypothetical RPM $0.30 / $1.00 / $2.00: gross revenue **$9 / $30 / $60**. Real organic traffic, AdSense approval and content differentiation must precede claims of monetization. See [AdSense account disapproval](https://support.google.com/adsense/answer/81904?hl=en) and [ad placement rules](https://support.google.com/adsense/answer/1346295?hl=en).
An AI/PDF tool with processing cost per request may lose money even when page RPM is nonzero. Include file bandwidth, OCR CPU, storage and support in per-request margin; do not monetize users' private document contents.

## 3. Subscription: distinguish pricing intent and revenue
**Hypothesis only:** 10,000 monthly active users; 3% pay EGP 79 / month = 300 paid accounts and **EGP 23,700 monthly gross**, before app-store charges, payment fees, taxes, refunds and variable service costs. This does *not* establish a 3% conversion in Egypt, and not all 10,000 MAU need be 10,000 trial signups. Verify policy and seller account:
- [Google Play Payments](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en)
- [Apple subscriptions](https://developer.apple.com/app-store/subscriptions/)
- Existing research [Paddle/90-day trial model](./Investor-Unit-Economics-2026-11-18-v0.6.md) retains its own hypothetical fees and cannot be pasted into store billing.

Retention drives paid LTV. A simplified monthly contribution of EGP 60 and churn 10% would imply EGP 600 un-discounted contribution LTV **if** stable churn / margins hold; neither is measured. Never invent MAU, renewal, refunds or foreign exchange.

## 4. Hybrid: remove paid users from ad-eligible cohort
Combined monthly gross in native currencies = **ads from ad-eligible free users** + gross premium revenue. Example separate assumptions: 9,700 free MAU, 300 paid MAU, unknown DAU-to-MAU ratio for free cohort; therefore **do not compute ad revenue from MAU**. Measure free DAU, valid ads/DAU, net premium ARPPU and payment-provider fees separately, then reconcile to bank deposits. An ad-free paid user contributes zero ads if the product promise removes ads.

If an optional rewarded ad unlocks content, it must be genuinely optional, never the only way to complete essential School PDF homework, and compliant with the user's age category and store policies.

## 5. USD 100 acquisition test — decision boundaries
Experimental budget: three channels/cohorts with $30+$30+$30, remaining $10 reserve. At a **fictional** CPI $0.10, $30 could acquire 300 installs **only** if such CPI can actually be purchased; installs can be non-active/fraudulent. At $1 CPI, the same $30 buys 30 installs. **Neither illustrates observed Egypt ad costs.**
Capture impressions, CTR, CPC, installs, activated users, D1/D7/D30 or W1/W4, actual ad revenue, paid conversion and refunded net. Estimate:
- CAC_paid = all attributable acquisition+free-trial costs / actual paying conversions.
- Contribution_ltv_ads = sum across lifetime days (valid impressions per user-day × realized eCPM/1,000) − attributable incremental costs.
- Contribution_ltv_paid = sum of net collected recurring payments − processor fees − refunds − variable product/support costs.
- Payback = acquisition spend / verified cohort contribution per period, only when positive and measured.
Use confidence bounds for small cohorts, and avoid declaring 0% churn when fewer than a meaningful cohort renewed.

## 6. Gate vs presentation: stop when numbers fail
**Ad-only:** if measured acquired-user contribution is less than CPI and organic acquisition cannot be demonstrated, stop paid acquisition. **Subscriptions:** verify paid second renewal and observed costs; do not interpret a 90-day free signup as a paid conversion. **Hybrid:** only proceed if total net contribution improves over an ad-free control cohort without harming task completion or violating youth policies.

The script [validate_monetization_study.py](./tools/validate_monetization_study.py) includes deterministic arithmetic regression checks for the documented calculations. This is a **documentation/model validation**, not live revenue verification.

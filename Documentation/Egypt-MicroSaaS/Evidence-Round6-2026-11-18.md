# سجل الأدلة — v0.6 مراجعة المستثمر والوكالات
**2026-11-18.** المصدر الرسمي أو إعلان المنافس يثبت وجود الميزة/السعر المذكور وقت الفحص، **لا يثبت عدد المشترين أو حجم السوق أو أن منتجنا يستطيع المنافسة**.

| ID | النوع | الادعاء المحدود المؤكد | المصدر |
|---|---|---|---|
| E01 | COMPETITOR | Arablyzer يعرض مجموعة أدوات مجانية واسعة للمواقع العربية (RTL/forms/SEO/structured data وغيرها) | https://arablyzer.com/tools |
| E02 | COMPETITOR | MizanRTL آلية فحص RTL للمواقع مع CI/API | https://mizanrtl.com/ |
| E03 | COMPETITOR | Burhan QA فحص رحلات عربية/EN ويعتمد على حسابات اختبار للعمق | https://www.useburhan.com/arabic-rtl-testing |
| E04 | COMPETITOR | SEOptimer يقدم White-label SEO reporting ونموذج التقاط عملاء للوكالات مدفوعاً، وليس فكرة جديدة نختلقها | https://www.seoptimer.com/pricing/ |
| E05 | COMPETITOR | MetricSpot لديه تقارير White-label وتجربة مجانية محدودة | https://metricspot.com/features/white-label-seo-tools/ |
| E06 | OFFICIAL | Google Search Console/Lighthouse/Core Web Vitals ومراجع صفحة الموقع مجانية لكن لا تعطي "جودة RTL بعد الإصدار" جاهزة تماماً | https://developers.google.com/search/docs/appearance/core-web-vitals |
| E07 | PAYMENT PROVIDER | Paddle 5% + $0.50 لكل Checkout، وأهلية المورد/بلد البيع/العقد تحتاج تحققًا مستقلًا قبل التعاقد | https://www.paddle.com/pricing |
| E08 | RESEARCH / SURVEY | ChartMogul/ProductLed 2026 بيانات 200 منتج، المعتاد $50–249/mo، فلا ننقل free-to-paid حرفياً لمشروع 1–5 دولارات | https://chartmogul.com/reports/saas-conversion-report/ |
| E09 | W3C / OFFICIAL | أدوات اختبار الوصول الآلية تساعد لكنها لا تحدد الامتثال بالكامل؛ لا شهادة WCAG تلقائية | https://www.w3.org/WAI/test-evaluate/tools/selecting/ |
| E10 | GOOGLE / OFFICIAL | SEO may take hours to several months؛ لا وعد ظهور خلال 30 يوماً | https://developers.google.com/search/docs/fundamentals/seo-starter-guide |
| E11 | GOOGLE / OFFICIAL | Keyword Planner يقدم volume/forecasts/competition بشروطه؛ لم نستخرج **أي بيانات كلمات/نقرات حقيقية** للحساب المستهدف | https://support.google.com/google-ads/answer/7337243?hl=en |
| E12 | SALLA / OFFICIAL | سلة لديها منظومة شراكات ومتجر تطبيقات مع آلاف التجار؛ الرقم المنشور 60k+ من ناشر المنصة لا TAM عملاء لمنتجنا | https://partners.salla.com/en/apps |
| E13 | ZID / OFFICIAL | زد توفر development/demo stores لتجربة التطبيقات قبل المراجعة، دون الحاجة لعميل خاص | https://docs.zid.sa/create-first-app |
| E14 | SALLA / OFFICIAL | سلة توفر أداة «محلل المتاجر» ضمن أدوات مجانية، مما يضعف EG-048 | https://salla.com/tools |
| E15 | OWASP / OFFICIAL | URL-scanning endpoint يعرض SSRF وبالتحديد private/meta IPs/redirect/DNS dangers؛ يجب حجبها | https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html |
| E16 | CLOUDFLARE / OFFICIAL | Browser Run 10h شهرياً ضمن Workers Paid ثم $0.09 لكل browser hour، مع قيود أخرى؛ لا إجمالي فاتورة | https://developers.cloudflare.com/browser-run/pricing/ |
| E17 | W3C / OFFICIAL | RTL/Bidi Arabic mixed script principles، الأرقام وعناصر واجهة تشمل مشاكل مرجعية يمكن صنع Fixtures لها | https://www.w3.org/International/docs/bp-html-bidi/ |
| E18 | SALLA APP MARKET | Wasfi/RankX وأدوات مجانية وSEO كثيرة لفحص المتاجر؛ لا مساحة لتكرار checker مجاني | https://apps.salla.sa/en/app/377162786 ; https://apps.salla.sa/en/app/418994099 |
| E19 | OFFICIAL STRIPE | بلد تسجيل التاجر وليس بلد المستخدم وحده هو قيد الأهلية؛ تأسيس في بلد آخر يحتاج كياناً وبنكاً وعنواناً وشروطاً | https://support.stripe.com/questions/requirements-to-open-a-stripe-account-in-another-country |
| E20 | CHARTMOGUL HELP | Conversion cohort بحسب نهاية الفترة، لا تنقل نتائج دفع قبل انتهاء التجربة، وينبغي تعريف denominator بوضوح | https://help.chartmogul.com/article/219-chart-trial-to-paid-conversion-rate |

## فجوات يجب ألّا يخفيها أي تقرير لاحق
- **لا توجد Keyword Planner export** ولا أحجام بحث عربية/بلد ولا تكلفة نقرة ولا leads فعلية.
- **لا توجد مقابلات عملاء ولا وكالات مؤكدة** أو أي اشتراك مدفوع أو متوسط churn/retention.
- **لا توجد اختبارات technical product** أو screenshots بعيوب مصطنعة قورنت فعلاً بأدوات Arablyzer/SEOptimer/MizanRTL.
- كل قيم CAC/$29/free-to-paid هنا محاكاة وليست نتائج تحصيل.
- الدفع في مصر/السعودية/الإمارات/الكويت والأردن يحتاج فحص حساب/كيان صاحب المشروع؛ التوسع العربي ليس ضمان تقنياً للتاجر.

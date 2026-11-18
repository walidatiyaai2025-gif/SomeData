# مصادر الجولة الرابعة — دراسة الأفكار القابلة للتحقق المستقل
**التاريخ:** 18 نوفمبر 2026 | **منهجية:** صفحات رسمية/منافسين، والتحقق من وجود oracle عام أو عينات اختبار صناعية مستقلة. ما زال فحص المنتج العملي **غير منفّذ**، ولم تحدث تجارب مستخدمين.

| المرجع | المصدر ودرجة الاعتماد | ما يدعمه |
|---|---|---|
| I01 | **OFFICIAL ETA:** https://sdk.invoicing.eta.gov.eg/document-validation-rules/ | أنواع فحص هيكل/حقول/توقيع/أكواد/قيم ومعادلات الفاتورة؛ لا يعني أن كل فحص يمكن تنفيذه دون الهيئة |
| I02 | **OFFICIAL ETA:** https://sdk.invoicing.eta.gov.eg/api/04-get-document-type-version/ | API وصف إصدار المستند يتضمن JSON schema / XML schema ويتطلب authentication؛ يمكن استخدام النسخ المنشورة ضمن شروطها |
| I03 | **COMPETITOR:** https://einvoicelab.com/eg/en/validation/ | EInvoiceLab يوفر بالفعل preflight محلياً؛ ويوضح أن local pass ليس قبولاً من ETA |
| I04 | **OFFICIAL MSMEDA:** https://www.msme.eg/MappedFolder/ar/Lists/Documentaries/SMEs%20Guide.pdf | بوابة التعاقدات العامة في مصر قناة رسمية لفرص حكومية، والقراءة العامة المجانية مثبتة بدليل قديم؛ الوصول الحي مشروط |
| I05 | **COMPETITOR:** https://apps.apple.com/eg/app/fieldproof-job-photo-report/id6791702124 | FieldProof أداة توثيق تقارير توقيع وصور بخطة/حد مجاني؛ مراجعة المواصفات قبل الاستثمار |
| I06 | **COMPETITOR:** https://apps.apple.com/eg/app/vericlean-cleaning-inspection/id6831389990 | VeriClean يفحص المواقع ويحتوي قوائم وصور |
| I07 | **COMPETITOR:** https://apps.apple.com/eg/app/swept-mobile/id1049960164 | Swept حلول فرق التنظيف |
| I08 | **GENERIC ALTERNATIVE:** https://support.microsoft.com/en-us/excel | Excel وPower Query بدائل عامة؛ لا دليل أن أداة أخرى بمهمة الاستيراد متمايزة |
| I09 | **COMPETITOR:** https://www.amcham.org.eg/tas | AmCham Egypt Tenders Alert Service لديه بحث/تنبيهات مجانية لخمس قطاعات وباقات مدفوعة أوسع |
| I10 | **COMPETITOR:** https://bidanga.com/country/EG | Bidanga يعلن تنبيهات مناقصات مجانية؛ جودة وتغطية البيانات تحتاج تحقق قبل الاستناد إليها |
| I11 | **COMPETITOR DIRECT:** https://help.uptimerobot.com/en/articles/11604710-who-should-use-uptimerobot-s-free-plan | UptimeRobot يسمح بـ50 monitor مجاني و5 دقائق، ومراقبة HTTP/keyword، فيضعف بيع نفس الخاصية |
| I12 | **COMPETITOR:** https://needmytools.com/en/pdf-to-excel | محول PDF إلى Excel مجاني محلي بالمتصفح ويدعم OCR عربي |
| I13 | **COMPETITOR:** https://nilepdf.com/en/pdf-to-excel | تحويل PDF إلى Excel محلي ومجاني |
| I14 | **OFFICIAL:** https://egyptera.org/en/TarrifApril2026.aspx | أسعار شرائح كهرباء مصر المعلنة بدء أبريل 2026 يمكن استعمالها مرجعاً حسابياً، لا لإصدار فواتير معتمدة |
| I15 | **OFFICIAL:** https://assets.eehc.gov.eg/files/%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%85%D9%88%D8%A7%D8%B7%D9%86%20%D9%84%D9%84%D8%AA%D8%B9%D8%A7%D9%85%D9%84%20%D9%85%D8%B9%20%D8%AE%D8%AF%D9%85%D8%A7%D8%AA%20%D8%A7%D9%84%D9%85%D9%86%D8%B5%D8%A9.pdf | المنصة الموحدة للكهرباء توفر «احسب فاتورتك»، فتقل الميزة المدفوعة لفكرة تطبيق مستقل |
| I16 | **COMPETITOR:** https://proceny.com/tools/price-list-comparison | مقارنة قوائم الأسعار مجاناً، رغم أن صحتها قابلة للفحص بملفات مصطنعة |

## مصدر لم يمكن فحصه في هذا البحث
- `https://etenders.gov.eg` — انتهى الوصول بطلب فاشل/timeout، **لا نقدم ضماناً أن المصدر قابل لجمع بيانات آلياً أو يسمح بذلك**. دراسة مناقصات لا تجتاز بوابة التنفيذ قبل إثبات مصدر مشروع ومستقر.

## ماذا لا نستنتج من الأدلة؟
- عمل برنامج لكشف ملفات JSON صحيح محلياً لا يثبت قبول ETA ولا امتثال المؤسسة.
- إثبات صحة PDF بالإقرار لا يساوي أهلية التوقيع الإلكتروني القانوني ولا يثبت تقليل نزاعات حقيقة.
- بيانات تجريبية مصطنعة لا تبرهن demand/MRR/conversion. لا تُمنح درجة 9 تجارية دون تجربة سوق.
- ادعاءات منافسين ليست تحققاً مستقلاً للخواص/الأسعار؛ قد تتغير باقاتهم.

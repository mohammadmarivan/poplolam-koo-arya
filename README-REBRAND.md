# poolamkoo

فورک ریبرندشده از [doxigo/muchToman](https://github.com/doxigo/muchToman)
لایسنس اصلی: **MIT** — این لایسنس حفظ شده است.

An android app for our moms and dads who can't keep track of their assets besides their active bank account.

## ساخت APK

### روش ۱ — گیت‌هاب اکشن (پیشنهادی، بدون نصب Android SDK)

1. این ریپو را روی گیت‌هاب پوش کن.
2. تب **Actions** را باز کن.
3. ورک‌فلو **Build poolamkoo APK** را Run workflow بزن.
4. بعد از اتمام، از Artifacts فایل APK را دانلود کن.

> APK دیباگ برای تست است. برای انتشار در فروشگاه باید keystore بسازی و assembleRelease را امضا کنی.

### روش ۲ — لوکال (لینوکس/مک/WSL)

پیش‌نیاز: JDK 17، Android SDK

```bash
git clone https://github.com/mohammadmarivan/poplolam-koo-arya.git
cd poplolam-koo-arya
chmod +x rebrand.sh gradlew
bash rebrand.sh
./gradlew assembleDebug
```

خروجی معمولاً اینجاست:

app/build/outputs/apk/debug/app-debug.apk

### روش ۳ — اندروید استودیو

ریپو را Open کن، صبر کن Gradle سینک شود، سپس Build > Build Bundle(s) / APK(s) > Build APK(s).

## هویت این نسخه

| فیلد | مقدار |
| --- | --- |
| نام | poolamkoo |
| پکیج | com.poolamkoo |
| نویسنده ریبرند | mohammadmarivan |
| نسخه | 1.0.0 (1) |
| رنگ تاکید | #c47a32 |

## احترام به لایسنس

این پروژه اثر اصلی را دزدی نمی‌کند؛ یک فورک قانونی است.
- فایل LICENSE را پاک نکن.
- NOTICE را نگه دار.
- اگر GPL است، سورس همین ریپو را عمومی بگذار.
- علامت تجاری پروژه اصلی را روی فروشگاه با همان نام نگذار.

---
تولیدشده با AppForge

# 📘 FreeTube Saver – සම්පූර්ණ සිංහල මාර්ගෝපදේශය

## කොටස 1: GitHub එකට files දාන විදිය

1. **github.com** එකට ගිහින් **Sign up** ඔබලා email එකකින් account එකක් හදාගන්න.
2. උඩ දකුණු පැත්තේ **+** ලකුණ ඔබලා **New repository** තෝරන්න.
3. **Repository name** එකට `freetube-saver` කියලා දාන්න.
4. **Public** තෝරලා **Create repository** ඔබන්න.
5. ඊළඟ පිටුවේ **"uploading an existing file"** කියන link එක ඔබන්න.
6. `freetube-saver.zip` එක ඔබේ computer එකේ **unzip (Extract)** කරන්න.
7. `ytdownloader` folder එක **ඇතුළේ** තියෙන හැම දෙයක්ම select කරලා GitHub පිටුවට drag කරලා දාන්න:
   `app.py`, `requirements.txt`, `render.yaml`, `Procfile`, `Dockerfile`, `templates` folder එක
   > ⚠️ zip file එකම upload කරන්න එපා. `templates` folder එකත් අනිවාර්යයෙන්ම දාන්න.
   > Phone එකෙන් කරනවා නම් Chrome එකේ **Desktop site** mode එක on කරන්න.
8. පහළ තියෙන **Commit changes** බොත්තම ඔබන්න.

## කොටස 2: Render එකේ site එක online දාන විදිය

1. **render.com** එකට ගිහින් **Get Started** ඔබලා **GitHub** එකෙන් sign up වෙන්න.
2. Dashboard එකේ **New +** ඔබලා **Blueprint** තෝරන්න.
3. ඔබේ `freetube-saver` repository එක **Connect** කරන්න.
4. **Apply / Deploy Blueprint** ඔබන්න.
5. විනාඩි 3–5ක් ඉන්න. Logs වල **"Your service is live 🎉"** කියලා පෙන්නයි.
6. උඩ තියෙන `https://freetube-saver-xxxx.onrender.com` link එක ඔබේ ස්ථිර website එක. 🎉

> Blueprint එක වැඩ නැත්නම්: **New + → Web Service** තෝරලා මේ විදියට පුරවන්න:
> - Build Command: `pip install -r requirements.txt`
> - Start Command: `gunicorn -w 2 --threads 4 --timeout 600 -b 0.0.0.0:$PORT app:app`
> - Instance Type: **Free**

## කොටස 3: Monetag දාලා සල්ලි හොයන විදිය 💰

### 3.1 Account එකක් හදාගන්න
1. **monetag.com** එකට ගිහින් **Sign up** ඔබලා **Publisher** විදියට register වෙන්න.
2. Email එක verify කරන්න.

### 3.2 Website එක add කරලා verify කරන්න
1. Monetag dashboard එකේ **Websites / Sites** කොටසට ගිහින් **Add website** ඔබන්න.
2. ඔබේ Render link එක දාන්න (උදා: `freetube-saver-xxxx.onrender.com`).
3. **Meta tag** verification ක්‍රමය තෝරලා ඒ code එක copy කරගන්න
   (`<meta name="monetag" content="...">` වගේ එකක්).
4. **Render** dashboard එකට ගිහින් ඔබේ service එක ඔබලා **Environment** තෝරන්න.
5. **Add Environment Variable** ඔබලා මෙහෙම පුරවන්න:
   - **Key:** `MONETAG_META`
   - **Value:** Monetag එකෙන් copy කරපු meta tag එක
6. **Save Changes** ඔබන්න. විනාඩි 2–3කින් site එක ආයෙත් deploy වෙනවා.
7. Monetag එකට ආපහු ගිහින් **Verify** ඔබන්න. ✅

> **වෙනත් ක්‍රමයක් (sw.js file එක):** Monetag එකෙන් `sw.js` file එක download කරලා GitHub repository එකට upload කරන්න (`app.py` තියෙන තැනටම). Render එක ඉබේම update වෙනවා. ඊට පස්සේ **Verify** ඔබන්න.
> (Push notification ads වලටත් මේ `sw.js` file එක ඕනේ.)

### 3.3 Ads දාන්න
1. Monetag එකේ ad format එකක් තෝරන්න:
   - **MultiTag** – ලේසියි, ආදායම හොඳයි ⭐ (ආරම්භයට හොඳම එක)
   - **OnClick (Popunder)** – වැඩි ආදායමක්, හැබැයි users ලට ටිකක් කරදරයි
   - **In-Page Push / Vignette** – මධ්‍යස්ථයි
2. **Get code** ඔබලා `<script ...></script>` code එක copy කරගන්න.
3. Render → **Environment** → **Add Environment Variable**:
   - **Key:** `AD_CODE`
   - **Value:** copy කරපු script code එක
4. **Save Changes** ඔබන්න. ඊට පස්සේ ads පෙන්නන්න පටන් ගන්නවා. 🎉

### 3.4 සල්ලි ගන්න
- **Statistics** කොටසේ ඔබේ ආදායම බලාගන්න පුළුවන්.
- **Payments** කොටසේ ගෙවීම් ලබාගන්න ක්‍රමයක් එකතු කරන්න (Payoneer, crypto වගේ). අවම ගෙවීම් ප්‍රමාණය සහ ලබාගන්න පුළුවන් ක්‍රම dashboard එකේ බලාගන්න.

### 3.5 ආදායම වැඩි කරගන්න tips
- ✅ Visitors (traffic) තමයි වැදගත්ම දේ. Facebook, TikTok, YouTube, Telegram වල site එක share කරන්න.
- ✅ Google search වලින් visitors එන්න site එකට "How to download" වගේ articles එකතු කරන්න.
- ❌ **ඔබේම ads ඔබම click කරන්න එපා.** යාළුවන්ට click කරන්න කියන්නත් එපා. එහෙම කළොත් account එක ban වෙනවා.
- ❌ Ads ගොඩක් දාන්න එපා. Users ලා ආයෙත් එන්නේ නැතිව යනවා.

## ⚠️ වැදගත් අවවාද
1. **YouTube block කිරීම:** Render වගේ hosting servers වලින් එන requests YouTube බොහෝ වෙලාවට block කරනවා (*"Sign in to confirm you're not a bot"*). එහෙම වුණොත් cookies හෝ proxy එකක් සකස් කරන්න වෙනවා.
2. **Domain:** Monetag එක `onrender.com` වගේ subdomain එකක් පිළිගත්තේ නැත්නම්, `.com` domain එකක් මිලදී අරන් (අවුරුද්දකට ආසන්න වශයෙන් $10) Render → **Settings → Custom Domain** එකට එකතු කරන්න.
3. **නීතිමය අවදානම:** අවසර නැතිව YouTube videos download කිරීම YouTube නීති රීති වලට පටහැනියි. Ads දාලා සල්ලි හොයද්දී copyright පැමිණිලි (DMCA) එන්න පුළුවන්, hosting account එක suspend වෙන්නත් පුළුවන්. Site එකේ footer එකේ තියෙන copyright notice එක අයින් කරන්න එපා.
4. **Google AdSense:** YouTube downloader sites වලට AdSense දෙන්නේ නැහැ. ඒ නිසා තමයි Monetag වගේ network එකක් පාවිච්චි කරන්නේ.

<p align="center">
  <img src="https://i.ibb.co/dJ0gpJf1/photo-2025-06-16-12-07-05-7516517596376596504.jpg" alt="VJ-COURSE-EXTRACTOR-BOT Logo" width="300">
</p>

<h1 align="center">
  🎓 RJ / VJ COURSE EXTRACTOR BOT
</h1>

<p align="center">
  <b>Fast, automated Telegram Bot to extract course contents, videos, PDFs & materials from Physics Wallah (PW), Classplus (CP), and Appx.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python 3.12">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker" alt="Docker Ready">
  <img src="https://img.shields.io/badge/Coolify-Compatible-6366f1" alt="Coolify Ready">
  <img src="https://img.shields.io/badge/License-Protected-red" alt="License">
</p>

---

## 🌟 Features

- 🚀 **Physics Wallah (PW) Extractor:** Extract free preview batches and purchased batch content directly to formatted `.txt` files with streaming links.
- 📘 **Classplus (CP) Extractor:** Supports store preview courses, batch previews, and purchased courses using Org Code + Phone/OTP or Access Token.
- 📒 **Appx Extractor:** Scrapes demo lectures, previews, and user batches via Appx APIs with decryptor support.
- 🐳 **100% Docker & Coolify Compatible:** Built-in web health-check server (`PORT 8080`) so Coolify detects healthy status immediately without extra configuration.
- 🛡️ **Authorized Access:** Secure `AUTH_USERS` restriction so only authorized Telegram accounts can use the bot.

---

## ⚙️ Environment Variables (Required)

Ye bot chalane ke liye aapko neeche diye gaye Environment Variables Coolify ya `.env` file mein daalne honge:

| Variable | Description | Example / Kahan se milega? |
| :--- | :--- | :--- |
| `API_ID` | Telegram API ID | [my.telegram.org](https://my.telegram.org) se lein (e.g. `12345678`) |
| `API_HASH` | Telegram API Hash | [my.telegram.org](https://my.telegram.org) se lein (e.g. `966261d7f23f48f776...`) |
| `BOT_TOKEN` | Telegram Bot Token | Telegram par [@BotFather](https://t.me/BotFather) se naya bot banakar lein |
| `AUTH_USERS` | Allowed User IDs | Aapka Telegram User ID ([@userinfobot](https://t.me/userinfobot) se lein). Multiple IDs ke liye comma lagayein: `12345678,98765432` |
| `PORT` | Healthcheck Web Port | Optional (Default: `8080`). Coolify ke internal health check ke liye use hota hai. |

---

## 🚀 Coolify Deployment Guide (Step-by-Step)

Coolify par ye bot ek baar mein deploy hoke turant live ho jayega:

### Step 1: Coolify Dashboard Kholein
1. Apne Coolify panel mein login karein.
2. Apne **Project** aur **Environment** mein jayein.
3. **+ New Resource** button par click karein.

### Step 2: Git Repository Select Karein
1. **Public Repository** ya **GitHub / Private Repository** select karein.
2. Apne is repo ka URL enter karein:
   ```text
   https://github.com/<your-username>/RJ-Course-Extractor-Bot
   ```
3. Branch select karein (e.g., `main` ya `master`).
4. **Build Pack**: Coolify automatically `Dockerfile` detect kar lega. (Agar na kare to **Dockerfile** choose karein).

### Step 3: Environment Variables Set Karein
Coolify ke resource dashboard mein **Environment Variables** tab par jayein aur ye add karein:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token_from_botfather
AUTH_USERS=your_telegram_numeric_id
PORT=8080
```

> 💡 **Tip:** Values ke aas-paas quotes (`"`) lagane ki zaroorat nahi hai. Agar multiple users hain to comma lagayein: `12345678,98765432`.

### Step 4: General Settings Check Karein
- **Port:** `8080` (Coolify usually reads this from `EXPOSE 8080`).
- **Domain:** Telegram bots polling mode me kaam karte hain, isliye public domain assign karna zaroori nahi hai. Agar aap domain assign karenge to web browser me `Bot running` dikhayega.
- **Health Check Path:** `/` (Default port 8080 par 200 OK deta hai).

### Step 5: Deploy Par Click Karein
1. Upar right corner par **Deploy** button click karein.
2. Build logs mein:
   - Python dependencies install hongi.
   - Container start hoga.
   - Healthcheck `/` pass ho jayega (Healthy ✅).
3. Apne Telegram bot par jakar `/start` send karein! Bot turant reply karega! 🎉

---

## 🐳 Docker / Docker Compose Deployment (VPS ya Local)

Agar aap apne VPS par directly Docker ya Docker Compose se chalana chahte hain:

### Method 1: Docker Compose (Sabse Asan)
1. Repository clone karein:
   ```bash
   git clone https://github.com/<your-username>/RJ-Course-Extractor-Bot.git
   cd RJ-Course-Extractor-Bot
   ```

2. `.env` file banayein:
   ```bash
   cp .env.example .env
   nano .env
   ```
   (Apne `API_ID`, `API_HASH`, `BOT_TOKEN`, aur `AUTH_USERS` fill karein).

3. Container start karein:
   ```bash
   docker compose up -d --build
   ```

4. Logs dekhne ke liye:
   ```bash
   docker compose logs -f
   ```

5. Stop karne ke liye:
   ```bash
   docker compose down
   ```

---

### Method 2: Pure Docker CLI

```bash
# 1. Image Build karein
docker build -t rj-course-extractor-bot .

# 2. Container Run karein
docker run -d \
  --name rj-course-extractor-bot \
  --restart unless-stopped \
  -p 8080:8080 \
  -e API_ID=12345678 \
  -e API_HASH="your_api_hash" \
  -e BOT_TOKEN="your_bot_token" \
  -e AUTH_USERS="12345678" \
  rj-course-extractor-bot
```

---

## 🚂 Railway / Render Deployment

Agar aap Railway ya Render par deploy karna chahte hain:
- **Railway:** Is repo me `railway.json` already shamil hai. Railway par connect karte hi automatic build ho jayega.
- **Render:** Render par **Web Service** ya **Background Worker** choose karein. Build command: `pip install -r requirements.txt`, Start command: `python main.py`.

---

## 📖 Bot Commands & Usage

- `/start` - Check bot status (Shows "Bot Is Running").
- `/help` - Opens the interactive menu for:
  - 🚀 **Physics Wallah (PW)**
  - 📘 **Classplus (CP)**
  - 📒 **Appx**
- Bot will prompt you step-by-step for login tokens, batch selections, and automatically send you the extracted course content list (`.txt` / `.json`).

---

## 🛠️ Project Structure

```text
├── Dockerfile              # Production-ready Docker container file (Python 3.12-slim)
├── docker-compose.yml      # Docker Compose configuration
├── .dockerignore           # Excludes unnecessary files from Docker image
├── .env.example            # Sample environment variables file
├── main.py                 # Bot initialization, command routing & health server
├── config.py               # Environment variables handler with auto-sanitization
├── helpers.py              # User authentication, crypto, and listener helpers
├── one.py                  # Physics Wallah extractor logic
├── two.py                  # Classplus extractor logic
├── three.py                # Appx extractor logic
├── threeapis.json          # Appx API repository
├── requirements.txt        # Python package dependencies
├── Procfile                # Heroku / Render support
└── railway.json            # Railway deployment configuration
```

---

## ❓ Troubleshooting (Aam Samasyayein)

1. **"ValueError: Set API_ID env var!" ya Bot crash ho raha hai:**
   - Check karein ki Coolify ke Environment Variables tab mein `API_ID`, `API_HASH`, `BOT_TOKEN`, aur `AUTH_USERS` theek se set hain.
2. **Bot reply nahi kar raha:**
   - Confirm karein ki aapka user ID `AUTH_USERS` me added hai. Dusre unauthorized users ko bot ignore karega.
   - Coolify ke "Logs" tab mein check karein koi error to nahi hai.
3. **Port conflict:**
   - By default container port `8080` use karta hai. Agar VPS par port 8080 already busy hai, to host port change karein (e.g. `8085:8080`).

---

## 💝 Credits

<b><details><summary>Tap To See Credits</summary>

- 💝 Credit Goes To [Tech VJ](https://telegram.me/VJ_Bots)
- 💖 Thank You So Much To All Who Helped In This Journey 💕
- Copyright ©️ [Tech VJ](https://youtube.com/@Tech_VJ)
- Contact Link: [King VJ](https://telegram.me/Kingvj01)

</details></b>

---
*Selling this repo or code of this repo for money is strictly prohibited 🚫*

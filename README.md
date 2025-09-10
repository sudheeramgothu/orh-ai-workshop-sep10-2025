# Automate & Integrate: Python Bots with Free Public APIs

Welcome! This starter repo is for the ORH Research AI Workshop (Sept 10, 2025).  
You’ll build two tiny bots that call real-world APIs and expose them via a simple web server.

## What you’ll build
1. **Weather Bot** using the free [Open‑Meteo API](https://open-meteo.com) (no API key required).
2. **News Bot** using [NewsAPI](https://newsapi.org) (free plan requires an API key).

Both are served through a minimal **Flask** app, so you can run them locally and hit endpoints from a browser or `curl`.

---

## 1) Prerequisites
- Python **3.8+**
- A code editor (VS Code recommended)
- Optional: Git
- Optional: a NewsAPI API key (free) from https://newsapi.org

> We’ll still be able to do the Weather Bot even if you don’t get a NewsAPI key in time.

---

## 2) Quick Start

### A) Clone or download
If you downloaded a ZIP, extract it. If you’re using Git:
```bash
git clone <your-fork-or-repo-url>
cd orh-ai-workshop-starter
```

### B) Create a virtual environment (recommended)
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

### C) Install dependencies
```bash
pip install -r requirements.txt
```

### D) (Optional) Configure environment variables
Copy `.env.example` to `.env` and add your **NEWSAPI_KEY** if you have one:
```env
NEWSAPI_KEY=replace_me
```

### E) Run the app
```bash
python app.py
```
You should see output similar to:
```
 * Running on http://127.0.0.1:5000
```

---

## 3) Use the Bots

### Weather Bot (no key needed)
**GET** `http://127.0.0.1:5000/api/weather?city=Atlanta`
- Query param: `city` (required). Examples: `Atlanta`, `New York`, `London`.
- Returns: basic forecast (temperature, winds, etc.)

### News Bot (requires NEWSAPI_KEY)
**GET** `http://127.0.0.1:5000/api/news?q=ai`
- Query param: `q` (required): keyword to search for news (e.g., `ai`, `python`, `cloud`).
- Set your key in `.env` before using.

> Tip: Try different queries and see how the JSON changes.

---

## 4) Files Overview
```
orh-ai-workshop-starter/
├─ app.py                 # Flask app with two endpoints: /api/weather and /api/news
├─ requirements.txt       # Python dependencies
├─ .env.example           # Sample environment variables (copy to .env)
├─ services/
│  ├─ open_meteo.py       # Weather bot logic (Open-Meteo API)
│  └─ newsapi.py          # News bot logic (NewsAPI)
└─ README.md              # This file
```

---

## 5) Stretch Goals (post‑workshop)
- Add caching (e.g., in-memory or Redis) to reduce API calls.
- Build a simple HTML page that calls these endpoints for a nicer UI.
- Deploy to a free tier (e.g., Render, Railway) or containerize with Docker.
- Swap in other free APIs (jokes, trivia, crypto prices) and add new endpoints.

---

## 6) Troubleshooting
- **Port already in use**: Stop other apps or change port in `app.py`.
- **Module not found**: Make sure your virtual environment is activated and you ran `pip install -r requirements.txt`.
- **News endpoint errors**: Ensure you created `.env` with a valid `NEWSAPI_KEY`.

Happy building!


---

## 7) UI (Optional)
A minimal web UI is available at **/ui** once the app is running:
- Open http://127.0.0.1:5000/ui
- Try the Weather, News, Joke, and Crypto sections.

---

## 8) Extra Endpoints
### Jokes (no key needed)
**GET** `http://127.0.0.1:5000/api/joke`  
Returns a random dad joke from icanhazdadjoke.

### Crypto Price (no key needed)
**GET** `http://127.0.0.1:5000/api/crypto?symbol=bitcoin&vs=usd`  
Retrieves current price from CoinGecko. Try `symbol=ethereum&vs=usd`.

---

## 9) Docker (Optional)
Build and run using Docker:
```bash
docker build -t orh-bot .
docker run --rm -p 5000:5000 --env-file .env orh-bot
```
> Tip: Put your `NEWSAPI_KEY` in a local `.env` and pass it with `--env-file`.

---

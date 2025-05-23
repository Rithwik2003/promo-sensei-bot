# 🧠 Promo Sensei - Smart Shopping Assistant

Promo Sensei is an intelligent Slack-integrated assistant that scrapes live e-commerce deals, stores them in a vector database, and answers natural language queries using Retrieval-Augmented Generation (RAG) via LLMs.

---

## ✨ Features

- 🔎 Search offers like “flat 50% off shoes” or “lipsticks under ₹300”
- 🛒 Scrapes deals from **Nykaa**, **Puma** and **Ajio**
- 🧠 Uses **FAISS + SentenceTransformers** to store offers
- 💬 Integrated with **Slack** via `/promosensei` command
- 🤖 Answers powered by OpenRouter (GPT-based)

---

## 📁 Project Structure

| File | Purpose |
|------|---------|
| `scraper.py` | Scrapes offers from supported e-commerce sites |
| `ingest_to_vector_db.py` | Embeds offer data and stores in FAISS |
| `rag_query.py` | Accepts user queries, fetches relevant context, and calls LLM |
| `slackbot.py` | Integrates with Slack to support `/promosensei` command |
| `offers.json` | Stores latest scraped offers |
| `offers_index.faiss` | FAISS index of embedded offers |
| `offers_meta.json` | Metadata used to return results |
| `.env` | Environment variables (API keys etc.) |

---

### ⚙️ Setup Instructions

🔧 1. Clone the Repo

```bash
git clone https://github.com/your-username/promo-sensei-bot.git
cd promo-sensei-bot

📦 2. Install Dependencies

pip install -r requirements.txt

playwright install

🔐 3. Create .env File

OPENROUTER_API_KEY=sk-your-openrouter-key

SLACK_BOT_TOKEN=xoxb-your-slack-bot-token

SLACK_APP_TOKEN=xapp-your-slack-app-token

✅ 4. Scrape + Index Offers

python scraper.py

python ingest_to_vector_db.py

🧠 5. Ask via CLI

python rag_query.py

# Enter your query: "Type your query here"

### 💬 Slack Integration

▶️ Run Slack Bot

python slackbot.py

✅ Slash Commands Supported in Slack

/promosensei search <query>

e.g.,

Command:


Output:

c:\Pictures\Screenshots\Screenshot 2025-05-24 013203.png

/promosensei brand <name>

e.g.,



/promosensei summary
→ Summarizes all indexed offers

/promosensei refresh
→ Re-scrapes all websites and updates the database
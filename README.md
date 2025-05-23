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
```

📦 2. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

🔐 3. Create .env File

```bash
OPENROUTER_API_KEY=sk-your-openrouter-key
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_APP_TOKEN=xapp-your-slack-app-token
```

✅ 4. Scrape + Index Offers

```bash
python scraper.py
python ingest_to_vector_db.py
```

🧠 5. Ask via CLI

```bash
python rag_query.py
```

Output > Enter your query: "Type your query here"

💬 Slack Integration

▶️ Run Slack Bot

```bash
python slackbot.py
```

✅ Slash Commands Supported in Slack


1.
```bash
/promosensei search <query>
```

e.g.,
Command:
![Screenshot 2025-05-24 013129](https://github.com/user-attachments/assets/60bee441-b9d6-4ec5-9a93-825f3644f639)

Output:
![Screenshot 2025-05-24 013203](https://github.com/user-attachments/assets/2488c0a7-aaad-4035-95bd-043c2e1116e7)


2.
```bash
/promosensei brand <name>
```

e.g.,
Command:
![Screenshot 2025-05-24 015316](https://github.com/user-attachments/assets/5aa164cf-d02b-4a34-ac3f-16157ffd2e2a)

Output:
![Screenshot 2025-05-24 015332](https://github.com/user-attachments/assets/7e70795a-1205-486d-b07f-cd9f1b82292e)
![Screenshot 2025-05-24 015410](https://github.com/user-attachments/assets/b7824f15-7b7f-4a64-9162-ec7071b557c6)


3.
```bash
/promosensei summary
```

e.g.,
Command:
![Screenshot 2025-05-24 014517](https://github.com/user-attachments/assets/a6cdc48f-1c70-4209-a5f1-7fb74e418e88)

Output:
![Screenshot 2025-05-24 014824](https://github.com/user-attachments/assets/29e8c5d0-70c2-4eae-a5fe-09b97b08d891)
![Screenshot 2025-05-24 014838](https://github.com/user-attachments/assets/ed726051-5716-4fa1-8aa8-21a0d19c4908)
![Screenshot 2025-05-24 014903](https://github.com/user-attachments/assets/7eb58742-7e53-42a4-9eda-b90cb707ca69)

→ Summarizes all indexed offers


4.
```bash
/promosensei refresh
```

e.g.,
Command:
![Screenshot 2025-05-24 015550](https://github.com/user-attachments/assets/0e7b23f7-30df-4e64-a35e-3edde9719505)

Output:
![image](https://github.com/user-attachments/assets/58959b10-480e-463c-9fe7-b9f4485893e0)

→ Re-scrapes all websites and updates the database

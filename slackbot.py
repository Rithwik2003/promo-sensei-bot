import os
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import os

load_dotenv()

from rag_query import get_top_k, ask_llm_context
import ingest_to_vector_db
import scraper 

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
app = App(token=SLACK_BOT_TOKEN)

@app.command("/promosensei")
def handle_command(ack, respond, command):
    ack()
    text = command.get("text", "").strip()

    if text.startswith("search "):
        query = text.replace("search ", "").strip()
        context = get_top_k(query, k=20)
        answer = ask_llm_context(query, context)
        respond(answer)

    elif text == "summary":
        query = "Summarize the best current deals"
        context = get_top_k(query, k=20)
        answer = ask_llm_context(query, context)
        respond(answer)

    elif text.startswith("brand "):
        brand = text.replace("brand ", "").strip().lower()
        context = get_top_k(brand, k=20)
        filtered = [x for x in context if brand in x["brand"].lower()]
        if not filtered:
            respond(f"No deals found for brand: {brand}")
        else:
            message = "\n\n".join([
                f"🛍️ {x['title']}\n💰 {x['sale_price']} (MRP: {x['mrp']})\n🔖 {x['discount']}\n🔗 {x['offer_link']}"
                for x in filtered
            ])
            respond(message)

    elif text == "refresh":
        respond("🔄 Refreshing offers... This may take a minute.")
        offers = scraper.scrape_nykaa_all_offers()
        ingest_to_vector_db.ingest(offers)
        respond(f"✅ Refreshed")

    else:
        respond("❓ Invalid command. Try `/promosensei search [query]`, `/promosensei summary`, `/promosensei brand [name]`, or `/promosensei refresh`.")

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

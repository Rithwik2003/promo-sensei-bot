import faiss
import json
import requests
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os


model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.read_index("offers_index.faiss")

with open("offers_meta.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

def get_top_k(query, k=10):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, k)
    return [metadata[i] for i in I[0]]

def ask_llm_context(query, context):
    context_str = "\n".join([f"Title - {x['title']} , Discount Percentage - {x.get('discount', 'N/A')}% , Price - {x.get('sale_price', 'N/A')} , MRP - {x.get('mrp', 'N/A')} , Description - {x['description']} , Link - {x['offer_link']}"
    for x in context])
    prompt = f"""
    You are Promo Sensei — a smart assistant that helps users find and summarize promotional offers from e-commerce sites.

    You are given a list of product offers. Each offer includes:
    - Title
    - Description
    - Price
    - MRP (original price)
    - Discount percentage
    - Offer link

    Your job is to:
    1. Analyze each offer based on the user's query.
    2. Apply any numeric conditions (like price < 2000 or discount > 10%) precisely.
    3. Return only the matching offers.
    4. Format your answer in a clear and helpful way (bulleted list preferred).

    Deals:
    {context_str}

    Now answer this user query:
    {query}

    Only return relevant offers. If no matching offer is found, respond politely but don't suggest external links or guess.
    """

    headers = {
        "Authorization": os.getenv("OPENROUTER_API_KEY"),  
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct:free", 
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
    result = response.json()

    try:
        return result['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ Failed to get response from OpenRouter: {e}\nRaw response: {result}"

if __name__ == "__main__":
    query = input("Enter your query: ")
    context = get_top_k(query)
    print("\n🤖 Promo Sensei's Answer:\n")
    print(ask_llm_context(query, context))

from playwright.sync_api import sync_playwright
import time
import json

def auto_scroll(page, scrolls=10, delay=1.0):
    for _ in range(scrolls):
        page.mouse.wheel(0, 5000)
        time.sleep(delay)

def scrape_puma_offers():
    from playwright.sync_api import sync_playwright
    import time

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://in.puma.com/in/en/deals", wait_until="domcontentloaded")
        time.sleep(5)

        auto_scroll(page, scrolls=15, delay=1.5)

        offers = []

        cards = page.query_selector_all("li[data-test-id='product-list-item']")

        print(f"🧾 Found {len(cards)} Puma product cards.")

        for card in cards:
            try:
                title_el = card.query_selector("h3.w-full")
                desc_el = card.query_selector("p[data-test-id='promotion-callout-message']")
                mrp_el = card.query_selector("span[data-test-id='sale-price']")
                sale_price_el = card.query_selector("span[data-test-id='price']")
                discount_el = card.query_selector("span[data-test-id='product-badge-sale']")
                link_el = card.query_selector("a[href]")

                
                title = title_el.inner_text().strip() if title_el else "No Title"
                desc = desc_el.inner_text().strip() if desc_el else "No Description"
                sale_price = sale_price_el.inner_text().strip() if sale_price_el else "No Sale Price"
                sale_price = sale_price.replace("₹", "Rs. ")
                mrp = mrp_el.inner_text().strip() if mrp_el else sale_price
                mrp = mrp.replace("₹", "Rs. ")
                discount = discount_el.inner_text().strip()[1:] if discount_el else "No Discount"
                link = "https://in.puma.com" + link_el.get_attribute("href") if link_el else "https://in.puma.com/in/en/deals"

                offers.append({
                    "title": title,
                    "description": desc,
                    "brand": "Puma",
                    "mrp" : mrp,
                    "sale_price" : sale_price, 
                    "discount" : discount,
                    "offer_link": link,
                    "expiry_date": "N/A"  # Not visible on Puma offers page
                })
            except Exception as e:
                print("⚠️ Error while parsing an offer:", e)
                continue
        
        browser.close()
        print(f"✅ Scraped {len(offers)} total offers from Puma.")
        return offers



def scrape_ajio_offers():
    from playwright.sync_api import sync_playwright
    import time

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.ajio.com/s/offer-deals-03022021", wait_until="domcontentloaded")
        time.sleep(5)

        auto_scroll(page, scrolls=15, delay=1.5)
        offers = []

        cards = page.query_selector_all("div.item.rilrtl-products-list__item.item")

        print(f"🧾 Found {len(cards)} Puma product cards.")

        for card in cards:
            try:
                title_el = card.query_selector("div.nameCls")
                brand_el = card.query_selector("div.brand > strong")
                desc_el = card.query_selector("div.exclusive-new")
                mrp_el = card.query_selector("span.orginal-price")
                sale_price_el = card.query_selector("span.price > strong")
                discount_el = card.query_selector("span.discount")
                link_el = card.query_selector("a.rilrtl-products-list__link desktop")

                
                title = title_el.inner_text().strip() if title_el else "No Title"
                desc = desc_el.inner_text().strip() if desc_el else "No Description"
                brand = brand_el.inner_text().strip() if brand_el else "No Brand"
                sale_price = sale_price_el.inner_text().strip() if sale_price_el else "No Sale Price"
                sale_price = sale_price.replace("₹", "Rs. ")
                mrp = mrp_el.inner_text().strip() if mrp_el else sale_price
                mrp = mrp.replace("₹", "Rs. ")
                discount = discount_el.inner_text().strip() if discount_el else "No Discount"
                link = "https://www.ajio.com/" + link_el.get_attribute("href") if link_el else "https://www.ajio.com/s/offer-deals-03022021"

                offers.append({
                    "title": title,
                    "description": desc,
                    "brand": brand,
                    "mrp" : mrp,
                    "sale_price" : sale_price, 
                    "discount" : discount,
                    "offer_link": link,
                    "expiry_date": "N/A"  # Not visible on Ajio offers page
                })
                print(title)
            except Exception as e:
                print("⚠️ Error while parsing an offer:", e)
                continue
        
        browser.close()
        print(f"✅ Scraped {len(offers)} total offers from Ajio.")
        return offers


def scrape_nykaa_offers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.nykaa.com/sp/offers-native/offers", wait_until="domcontentloaded")
        time.sleep(5)  

        auto_scroll(page, scrolls=15, delay=1.5)

        offers = []

        sections = page.query_selector_all("div.css-13ev4jt")  
        for section in sections:
            try:
                title_el = section.query_selector_all("p.product-name")
                desc_el = section.query_selector_all("div.css-1dl97id")
                mrp_el = section.query_selector_all("div.mrp-price")
                sale_price_el = section.query_selector_all("div.sale-price")
                discount_el = section.query_selector_all("div.discounted-price")
                link_el = section.query_selector_all("a")

                for i in range(len(title_el)):
                    title = title_el[i].inner_text().strip() if title_el else "No Title"
                    desc = desc_el[i].inner_text().strip() if desc_el else "No Description"
                    sale_price = sale_price_el[i].inner_text().strip() if sale_price_el else "No Sale Price"
                    sale_price = sale_price.replace("₹", "Rs. ")
                    mrp = mrp_el[i].inner_text().strip() if mrp_el else sale_price
                    mrp = mrp.replace("₹", "Rs. ")
                    discount = discount_el[i].inner_text().strip() if discount_el else "No Discount"
                    link = link_el[i].get_attribute("href") if link_el else "https://www.nykaa.com/sp/offers-native/offers"

                    offers.append({
                        "title": title,
                        "description": desc,
                        "brand": "Nykaa",
                        "mrp" : mrp,
                        "sale_price" : sale_price, 
                        "discount" : discount,
                        "offer_link": link,
                        "expiry_date": "N/A"  # Not visible on Nykaa offers page
                    })
            except Exception as e:
                print("⚠️ Error while parsing an offer:", e)
                continue

        browser.close()


        print(f"✅ Scraped {len(offers)} total offers from Nykaa.")
        return offers

def scrape_all_offers():
    
    nykaa = scrape_nykaa_offers()
    puma = scrape_puma_offers()
    ajio = scrape_ajio_offers()

    all_offers = ajio + nykaa + puma

    with open("offers.json", "w", encoding="utf-8") as f:
        json.dump(all_offers, f, indent=2, ensure_ascii=False)

    print(f"✅ Scraped {len(all_offers)} total offers from all sources.")
    return all_offers


if __name__ == "__main__":
    scrape_all_offers()
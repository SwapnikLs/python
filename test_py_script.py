import requests
from bs4 import BeautifulSoup

def fetch_usd_inr_rate():
    url = "https://in.investing.com/currencies/usd-inr"  # The URL of the page to scrape
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send an HTTP GET request to the webpage
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Parse the webpage content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the exchange rate on the page
        rate_tag = soup.find("span", {"data-test": "instrument-price-last"})
        if rate_tag:
            exchange_rate = rate_tag.text
            print(f"Current USD to INR Exchange Rate: {exchange_rate}")
            return float(exchange_rate)
        else:
            print("Exchange rate not found on the page.")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

    return None
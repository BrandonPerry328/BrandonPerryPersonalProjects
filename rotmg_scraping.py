from bs4 import BeautifulSoup
import requests

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36' }

URL = "https://www.realmeye.com/offers-to/sell/2990/9070"
req = requests.get(URL, headers=headers)
market = BeautifulSoup(req.content, 'html.parser')

data = market.prettify("utf-8")
with open("scrapetest.txt", "w") as f:
    f.write(str(data))
# with open('scrapetest.txt', 'w') as f:
#     offers = market.find('a')
#     refined_offers = ""
#     for i in range(10):
#         refined_offers = f"{offers[i]}\n\n"
#         f.write(refined_offers)

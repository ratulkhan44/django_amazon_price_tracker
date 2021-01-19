import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.amazon.com/DualSense-Wireless-Controller-PlayStation-5/dp/B08FC6C75Y/ref=sr_1_1?crid=3DHRREZH2SLK8&dchild=1&keywords=play+station.+5&qid=1610860531&sprefix=play+sta%2Caps%2C416&sr=8-1"


def get_link_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Accept-Language": "en"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    name = list(name.split(","))[0]

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = price.strip()[1:]

    return name, price


print(get_link_url(url))

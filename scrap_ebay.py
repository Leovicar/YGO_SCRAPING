import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=ddk-f001&_sacat=0"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="srp-river-main")
items = results.find_all("li", class_="s-item")

titles = []
prices = []

for item in items:
    title = item.find(class_="s-item__title").text
    price = item.find(class_="s-item__price").text
    titles.append(title)
    prices.append(price)

# Create a DataFrame from the lists of titles and prices
df = pd.DataFrame({"Title": titles, "Price": prices})


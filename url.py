from bs4 import BeautifulSoup
import requests

url = "https://www.snapdeal.com/product/6-pcs-reusable-air-fryer/674544559160#bcrumbSearch:kitchen%20product"

headers = {"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}

response = requests.get(url, headers = headers )
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h1", itemprop="name")
print("content: ", title.text)

price = soup.find("span", class_="pdp-final-price")
print("price of item: ", price.text)

discount = soup.find("span", class_="pdpDiscount")
print("price of item: ", discount.text)

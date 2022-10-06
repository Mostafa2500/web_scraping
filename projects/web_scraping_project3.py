from bs4 import BeautifulSoup as bs
import requests
import csv

r=requests.get("https://www.pararius.com/apartments/amsterdam").text
soup=bs(r, "lxml")
items= soup.find_all("li", class_="search-list__item search-list__item--listing")

with open("housing.csv", "w", newline="") as f:
    thewriter=csv.writer(f)
    header=["titel", "address", "price", "area"]
    thewriter.writerow(header)

    for item in items:
        header=item.find("h2", class_="listing-search-item__title").text.replace("\n","").strip()
        address=item.find("div", class_="listing-search-item__sub-title").text.replace("\n","").strip()
        price=item.find("div", class_="listing-search-item__price").text.replace("\n","").strip()
        area=item.find("li", class_="illustrated-features__item illustrated-features__item--surface-area").text.replace("\n","").strip()
        info=[header,address,price,area]
        thewriter.writerow(info)


#web scrapping

import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.w3schools.com/")

soup=BeautifulSoup(req.content,"html.parser")

print(soup.prettify())

# print(soup.title)

# print(soup.get_text())
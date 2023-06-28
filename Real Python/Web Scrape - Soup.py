from bs4 import BeautifulSoup as bs
import requests as url
import re

home = "http://olympus.realpython.org/profiles"
base = re.findall('(http.?://[\w.]+)/', home)[0]
page = bs(url.get(home).text, "html.parser")

for x in page.find_all("a"): print(base + x["href"])

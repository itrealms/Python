import requests as url
import re

urls = [
    "http://olympus.realpython.org/profiles/aphrodite",
    "http://olympus.realpython.org/profiles/poseidon",
    "http://olympus.realpython.org/profiles/dionysus"
]

for x in urls:
    page = url.get(x)
    try:
        title = re.findall('<.*title.*>(.+)</.*title.*>', page.text, re.IGNORECASE)[0]
        print(title)
    finally:
        print(page.text)
        print(f"Crap. {x} doesn't have a title")

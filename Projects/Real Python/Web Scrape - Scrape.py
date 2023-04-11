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
        name = re.sub('\s*|<.*>', "", re.findall('Name:(.+)', page.text, re.IGNORECASE)[0])
        color = re.sub('\s*|<.*>', "", re.findall('Favorite Color:(.+)', page.text, re.IGNORECASE)[0])
        print(name + "\n" + color +"\n")
    except:
        print(page.text)
        print(f"Crap. Failure with : {x}")

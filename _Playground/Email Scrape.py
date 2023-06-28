import mechanicalsoup
import re

home = input('Page to scrape for emails: ')
base = re.findall('(http.?://[\w.]+)/', home)[0]
browser = mechanicalsoup.StatefulBrowser()
browser.open(home)
print(f'Current page: {browser.url}')
print('Grabbing emails...')

links = browser.page.find_all('a')
emails = []
for link in links:
    if re.search('^.+@.+\..+$', link.text): emails.append(link.text)

if not emails:
    print("No emails found")
else:
    for email in emails: print(email)

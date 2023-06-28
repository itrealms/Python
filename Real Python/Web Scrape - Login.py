import mechanicalsoup
import re

home = "http://olympus.realpython.org/login"
base = re.findall('(http.?://[\w.]+)/', home)[0]
browser = mechanicalsoup.StatefulBrowser()
browser.open(home)
print(f'Home page: {browser.url}')
print('Logging in...\n')
browser.select_form('form[name="login"]')

username = "zeus"
password = "ThunderDude"

print(f'Username: {username}')
print(f'Password: {password}')

browser['user'] = username
browser['pwd'] = password

print('Submitting credentials...\n')
browser.submit_selected()

print(f'Current page: {browser.url}')
print('Printing all links on page...\n')

for link in browser.page.find_all("a"):
    print(f'{link.text}: {base + link["href"]}')

import mechanicalsoup
from time import sleep

home = "https://www.random.org/integers/?num=2&min=1&max=6&col=2&base=10&format=html&rnd=new"
browser = mechanicalsoup.StatefulBrowser()
browser.open(home)


def rolls():
    browser.select_form(browser.page.find_all('form')[1])
    dice = browser.submit_selected().soup.select(".data")[0].text.split()
    die1, die2 = int(dice[0]), int(dice[1])
    return die1, die2, die1 + die2


def winner(status):
    match status:
        case True:
            print("Winner")
        case False:
            print("Loser")
    exit()


come_win = (7, 11)
come_loss = (2, 3, 12)

roll = rolls()
print(f'You rolled a {roll[0]} and a {roll[1]} for a total of {roll[2]}')
sleep(.01)

if roll[2] in come_win: winner(True)
if roll[2] in come_loss: winner(False)

point = roll[2]
print(f'Your point is {point}')
while 1:
    point_roll = rolls()
    sleep(.01)
    print(f'You rolled a {point_roll[0]} and a {point_roll[1]} for a total of {point_roll[2]}')
    if point_roll[2] == point: winner(True)
    if point_roll[2] == 7: winner(False)
    sleep(.5)

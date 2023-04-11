from rich.progress import track
from rich.console import Console
from rich.table import Table
import random as rd

if (door_count := int(input('How many doors?: '))) < 2: exit()

prizes = ['car']
for x in range(int(door_count) - 1):
	prizes.append('goat')

wins = losses = 0
rounds = 100_000_000
for x in track(range(rounds), description='Working...'):
	rd.shuffle(prizes)
	if prizes[rd.randrange(0, door_count)] == 'car':
		wins += 1
	else:
		losses += 1

print('\n')
rounds_l = len(str(rounds))
win_p = wins / rounds
loss_p = losses / rounds

print(f'You played {rounds:,} rounds!')

table = Table()
table.add_row('', 'Percentage', '', 'Totals')
table.add_row('Results if stay:')
table.add_row('Wins', f'{win_p:>3.0%}', 'Total', f'{wins:>{rounds_l},}')
table.add_row('Losses', f'{loss_p:>3.0%}', 'Total', f'{losses:>{rounds_l},}')

table.add_row('\nResults if switch:')
table.add_row('Wins', f'{loss_p:>3.0%}', 'Total', f'{losses:>{rounds_l},}')
table.add_row('Losses', f'{win_p:>3.0%}', 'Total', f'{wins:>{rounds_l},}')

console = Console()
console.print(table)

# Code here is always executed
# from _imports.timer import timer
# from _imports.debug import debug
# from rich.traceback import install
#
# install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import random
	import statistics

	turns_count_random = []
	turns_count_middle = []
	low_init = 0
	high_init = 1_000

	def play_rand():
		guesses_rand = 0
		low_rand = low_init
		high_rand = high_init
		while True:
			# Check Random Guess
			guess_rand = random.randrange(low_rand, high_rand)
			guesses_rand += 1
			if guess_rand == your_number:
				turns_count_random.append(guesses_rand)
				break
			if guess_rand < your_number:
				low_rand = guess_rand + 1
			if guess_rand > your_number:
				high_rand = guess_rand

	def play_mid():
		guesses_mid = 0
		low_mid = low_init
		high_mid = high_init
		while True:
			# Check Middle Guess
			guess_mid = int((high_mid - low_mid) / 2 + low_mid)
			guesses_mid += 1
			if guess_mid == your_number:
				turns_count_middle.append(guesses_mid)
				break
			if guess_mid < your_number:
				low_mid = guess_mid + 1
			if guess_mid > your_number:
				high_mid = guess_mid

	print('What is the best way to guess a number? Random or middle?')
	print('Running 1,000,000 simulations...')
	for _ in range(1_000_000):
		your_number = random.randrange(low_init, high_init)
		play_rand()
		play_mid()

	print('After 1,000,000 rounds here is the average turns taken by each method:')
	print(f'Random guessing took an average of {statistics.mean(turns_count_random)}')
	print(f'Guessing the middle took an average of {statistics.mean(turns_count_middle)}')

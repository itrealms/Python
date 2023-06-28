# Always executed here
# from _imports.timer import timer
# from _imports.debug import debug
# from rich.traceback import install
# install()

if __name__ == '__main__':
	# Executed when invoked directly (Not a module)
	import random
	import os
	from rich.prompt import IntPrompt

	def gen_pass():
		word_count = len(word_list)
		word1 = word_list[random.randrange(0, word_count)].capitalize()
		word2 = word_list[random.randrange(0, word_count)].capitalize()
		spec = ('!', '@', '#', '$', '%', '^', '&', '*')[random.randrange(0, 8)]
		num = str(random.randrange(0, 10))
		return "".join([word1, word2, spec, num])

# Main Code
	with open('files/wordlist.txt') as wl:
		word_list = [line.rstrip() for line in wl.readlines()]
	max_passes = len(word_list) * len(word_list) * 80

	if (password_count := IntPrompt.ask('Number of passwords to generate')) not in range(1, max_passes):
		print(f'Invalid number of passwords. Please enter a number between 1 and {max_passes}')
		exit()

	num_generated = 0
	passwords = set()
	print('Generating passwords. Please wait...')
	while len(passwords) < password_count:
		passwords.add(gen_pass())
		num_generated += 1

	print(f'Generated {num_generated:,} passwords.')
	print(f'Resulting in {password_count:,} non-duplicate passwords')

	with open('./passwords.txt', "w") as pl:
		for password in passwords:
			pl.write(password + '\n')
	os.system('start ./passwords.txt')

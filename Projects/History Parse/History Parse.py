# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import glob
	import re
	import os


	def parse_files():
		base_path = 'G:/My Drive/Python/Projects/History Parse'
		logs_path = f'{base_path}/logs'
		file_list = [file for file in glob.glob(f'{logs_path}\\*')]
		for log_file in file_list:
			urls = set()
			full_urls = set()
			with open(log_file, "r") as log:
				lines = [line.rstrip() for line in log.readlines()]
				for line in lines:
					find_student = re.search(r'Student: (.+)', line)
					if find_student:
						student_name = find_student.group(1)

					url = re.search(r'https?://(?:\S*\.)*(\S+\.\w+)/', line)
					if url and url.group(1) not in url_whitelist:
						urls.add(url.group(1))

					find_url = re.search(r'URL: (.+)', line)
					if find_url:
						full_urls.add(find_url.group(1))

			with open(f'{base_path}/parsed/{student_name}.txt', "w") as nl:
				nl.write(f'Username: {student_name}\n')
				for url in urls:
					nl.write(f'\n{url}')

				nl.write(f'\n')

				for full_url in full_urls:
					nl.write(f'\nURL: {full_url}')

			os.system(f'start G:/"My Drive"/Python/Projects/"History Parse"/parsed/{student_name}.txt')

		return


	with open('G:/My Drive/Python/Projects/History Parse/whitelist.txt', "r") as wl:
		url_whitelist = [line.rstrip() for line in wl.readlines()]

	parse_files()

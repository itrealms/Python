# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import glob
	import re
	import os

	try:
		os.mkdir(f'New')
	except FileExistsError:
		pass
	with open('file name.txt', 'w') as blank_file:
		pass
	file_list = [file for file in glob.glob(f'./Clips/*.avi')]
	for file_path in file_list:
		dir_name = re.search(r'(\d{4}.\d{2}.\d{2}\s)(\d)(.\d{2}).([A|P]M\s-\s)(.*)\.avi', file_path)
		try:
			path = f'{dir_name[1]}0{dir_name[2]}{dir_name[3]} {dir_name[4]}{dir_name[5].lower()}'
		except TypeError:
			continue
		os.mkdir(f'New/{path}')
		os.rename(file_path, f'New/{path}.avi')

	file_list = [file for file in glob.glob(f'./Clips/*.avi')]
	for file_path in file_list:
		with open('file name.txt', 'a') as files:
			files.write(f'{file_path}\n')

else:
	# Code here executed when imported (As a module)
	pass

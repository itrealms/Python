# Code here is always executed

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import glob
	import re

	file_list = [file for file in glob.glob(f'*')]
	for file_path in file_list:
		if re.search(r'\.py', file_path):
			bat_file = re.sub(r'\.py', '.bat', file_path)
			with open(bat_file, 'w') as new_bat:
				new_bat.write(f'@echo off\n')
				new_bat.write(f'py "{file_path}"')

else:
	# Code here executed when imported (As a module))
	pass

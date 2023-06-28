# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	with open("test.exe", "rb") as bin_file:
		file_contents = bin_file.read()
	print(file_contents)

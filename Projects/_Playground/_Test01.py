# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	from datetime import date

	def check_date():
		print(date.today())
		return

	check_date()

else:
	# Code here executed when imported (As a module)
	pass

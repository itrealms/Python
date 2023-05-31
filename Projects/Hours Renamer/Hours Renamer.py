# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import datetime
	import os

	today = datetime.date.today()
	period_start = today - datetime.timedelta(days=today.weekday()+1, weeks=2)
	period_end = today - datetime.timedelta(days=today.weekday()+2,)

	file_name_old = 'Pay Checker - Google Sheets.pdf'
	file_name_new = f'[Hours] - {period_start} - {period_end}.pdf'

	try:
		os.rename(file_name_old, file_name_new)
	except FileNotFoundError:
		print('File Not Found')
	except FileExistsError:
		os.remove(file_name_new)
		print('Please run the program again')

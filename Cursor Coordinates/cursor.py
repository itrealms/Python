# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here executed when invoked directly (Not a module)
	import pyautogui as pui
	import time

	def print_coordinates():
		while True:
			x, y = pui.position()
			print(f'Cursor Position: x = {x}, y = {y}')
			time.sleep(0.5)

	try:
		print_coordinates()
	except KeyboardInterrupt:
		print('Script Terminated')

else:
	# Code here executed when imported (As a module)
	pass

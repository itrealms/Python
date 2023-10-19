# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here executed when invoked directly (Not a module)
	import cv2
	import numpy as np
	import pyautogui
	import time

	# Load image to match
	image = cv2.imread('./sample.png')

	# Define match threshold. Adjust as needed
	threshold = 0.95

	while True:
		# Set screen region for snapshot
		screen_w, screen_h = pyautogui.size()
		x_start, y_start = 0, 0
		x_end, y_end = screen_w, screen_h

		# Take snapshot of region
		screenshot = pyautogui.screenshot(region=(x_start, y_start, x_end, y_end))
		screenshot = np.array(screenshot)
		screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)




else:
	# Code here executed when imported (As a module)
	pass

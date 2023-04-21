from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import date
import os.path

# Set user's name and elements path
user_name = input('Name for the certificate?: ')
cert_check = False
cert_file = f'{user_name} - SB 1343v16 Sexual Harassment Prevention Training - {date.today()}.png'

xpath_base = '/html/body/div[2]/div[3]/div/div[5]/main/div/div/div/div[1]/div/div[2]'
test_true_path = f'{xpath_base}/form/div[1]/input'
test_confirm_path = f'{xpath_base}/button'
cert_path = f'{xpath_base}/button[3]'

# Set up chrome driver
options = Options()
options.add_argument("start-maximized")
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
action = ActionChains(chrome)

# And... GO!
chrome.get('https://sexual-harassment-prevention-training.dfeh.ca.gov/NonSupervisoryEnglish/story.html')

# Wait 5 minutes for slide show to be ready
WebDriverWait(chrome, 300).until(
	expected_conditions.element_to_be_clickable((By.ID, 'mobile-start-button'))
).click()

# Toggle Mute
WebDriverWait(chrome, 300).until(
	expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="volume"]'))
).click()

while True:
	if len(chrome.find_elements(By.XPATH, test_true_path)) > 0:
		try:
			action.click(chrome.find_element(By.XPATH, test_true_path)).perform()
			action.click(chrome.find_element(By.ID, 'submit')).perform()
			action.click(chrome.find_element(By.XPATH, test_confirm_path)).perform()
		except:
			time.sleep(.01)
			continue
	elif len(chrome.find_elements(By.CSS_SELECTOR, 'input[type="text"]')) > 0:
		cert_name = chrome.find_element(By.TAG_NAME, 'input')
		try:
			action.move_to_element(cert_name).perform()
			action.click(cert_name).perform()
			cert_name.clear()
			cert_name.send_keys(user_name)
			WebDriverWait(chrome, 300).until(
				expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#next'))
			).click()
		except:
			time.sleep(.01)
			continue
		else:
			cert_check = True
	elif cert_check and len(chrome.find_elements(By.XPATH, cert_path)) > 0:
		chrome.get_screenshot_as_file(cert_file)
		while not os.path.exists(cert_file):
			pass
		else:
			exit()
	else:
		try:
			action.click(chrome.find_element(By.CSS_SELECTOR, '#next')).perform()
		except:
			continue

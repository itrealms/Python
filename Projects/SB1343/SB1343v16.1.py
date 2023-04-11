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

user_name = input('Name for the certificate?: ')

options = Options()
options.add_argument("start-maximized")
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
action = ActionChains(chrome)

chrome.get('https://sexual-harassment-prevention-training.dfeh.ca.gov/NonSupervisoryEnglish/story.html')

WebDriverWait(chrome, 30).until(
	expected_conditions.presence_of_element_located((By.ID, 'mobile-start-button'))
).click()

# Toggle Mute
WebDriverWait(chrome, 10).until(
	expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="volume"]'))
).click()

while True:
	time.sleep(.01)

	xpath_base = '/html/body/div[2]/div[3]/div/div[5]/main/div/div/div/div[1]/div/div[2]'
	test_question_path = f'{xpath_base}/div[2]/div/div[1]/p/span'
	test_true_path = f'{xpath_base}/form/div[1]/input'
	test_confirm_path = f'{xpath_base}/button'

	next_button = chrome.find_element(By.CSS_SELECTOR, '#next')

	if len(chrome.find_elements(By.XPATH, test_true_path)) > 0:
		question = chrome.find_element(By.XPATH, test_question_path).get_attribute("innerHTML")
		print(f'Question: {question}')
		print('Answer: True\n')
		action.click(chrome.find_element(By.XPATH, test_true_path)).perform()
		action.click(chrome.find_element(By.ID, 'submit')).perform()
		action.click(chrome.find_element(By.XPATH, test_confirm_path)).perform()
		time.sleep(.25)
	elif len(chrome.find_elements(By.CSS_SELECTOR, 'input[type="text"]')) > 0:
		cert_name = chrome.find_element(By.TAG_NAME, 'input')
		action.move_to_element(cert_name).perform()
		action.click(cert_name).perform()
		cert_name.send_keys(user_name)
		time.sleep(.25)
		WebDriverWait(chrome, 300).until(
			expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#next[aria-disabled="false"]'))
		).click()
		time.sleep(.5)
		WebDriverWait(chrome, 300).until(
			expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#next[aria-disabled="false"]'))
		).click()
		print('Certificate ready')
		today = date.today().strftime("%Y-%m-%d")
		chrome.get_screenshot_as_file(f'{user_name} - SB 1343v16 Sexual Harassment Prevention Training - {today}.png')
		exit()
	else:
		action.click(next_button).perform()

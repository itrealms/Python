# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	from concurrent import futures
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.chrome.service import Service
	from webdriver_manager.chrome import ChromeDriverManager
	import datetime
	import json
	import requests
	import time
	import os

	def get_status(site_info):
		status_response = [site_info["Category"], site_info['Clean_Name']]

		try:
			page_head = requests.head(site_info['Address'], headers={'User-Agent': 'Chrome'})
		except:
			if os.path.exists(f'{sites_index[site_info["Clean_Name"]]}.png'):
				os.remove(f'{sites_index[site_info["Clean_Name"]]}.png')
			return [site_info["Category"], site_info['Clean_Name'], 'Error', 'Unknown', 'Error', 'Unknown', site_info['Address']]
		else:
			status_response.append(page_head.status_code)
			status_response.append(page_head.reason)

		try:
			page_full = requests.get(site_info['Address'], headers={'User-Agent': 'Chrome'})
		except:
			status_response.append('Error')
			status_response.append('Unknown')
		else:
			status_response.append(page_full.status_code)
			status_response.append(page_full.reason)

		options = Options()
		options.add_argument("start-maximized")
		chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
		time.sleep(1)
		try:
			chrome.get(site_info['Address'])
		except:
			if os.path.exists(f'{sites_index[site_info["Clean_Name"]]}.png'):
				os.remove(f'{sites_index[site_info["Clean_Name"]]}.png')
		time.sleep(.5)
		chrome.get_screenshot_as_file(f'{sites_index[site_info["Clean_Name"]]}.png')
		chrome.quit()

		status_response.append(site_info['Address'])
		return status_response

	while True:
		with open('sites.json') as sites:
			urls = [json.loads(url.rstrip()) for url in sites.readlines()]
		sites_status = urls
		sites_index = {urls[x]["Clean_Name"]: x for x in range(len(urls))}

		with futures.ThreadPoolExecutor() as exe:
			my_threads = {exe.submit(get_status, site): site for site in urls}
			for completed in futures.as_completed(my_threads):
				get_status_completed = completed.result()
				time_stamp = str(datetime.datetime.now().strftime('%Y-%m-%d %X'))
				site_result = {
					'Category': str(get_status_completed[0]),
					'Clean_Name': str(get_status_completed[1]),
					'H_Code': str(get_status_completed[2]),
					'H_Response': str(get_status_completed[3]),
					'Code': str(get_status_completed[4]),
					'Response': str(get_status_completed[5]),
					'Address': str(get_status_completed[6]),
					'Last_Checked': time_stamp
				}

				if site_result['H_Code'] == '200':
					site_result['H_Response'] = 'OK'
				else:
					if not site_result['H_Response']:
						site_result['H_Response'] = 'Unknown'

				if site_result['Code'] == '200':
					site_result['Response'] = 'OK'
				else:
					if not site_result['Response']:
						site_result['Response'] = 'Unknown'

				sites_status[sites_index[site_result["Clean_Name"]]] = site_result

			with open('resp0.html', "w") as resp0:
				resp0.write('''<tr class="subhead">
<td>Site URL:</td>
<td>Header Code:</td>
<td>Header Response:</td>
<td>Code:</td>
<td>Response:</td>
<td>Last Checked:</td>
<td>Screenshot:</td>
</tr>
''')
			with open('resp1.html', "w") as resp1:
				resp1.write('''<tr class="subhead">
<td>Site URL:</td>
<td>Header Code:</td>
<td>Header Response:</td>
<td>Code:</td>
<td>Response:</td>
<td>Last Checked:</td>
<td>Screenshot:</td>
</tr>
''')
			for x in range(len(sites_status)):
				if sites_status[x]["Category"] == "MISC":
					file = 'resp0.html'
				else:
					file = 'resp1.html'
				with open(file, "a") as resp:
					resp.write('<tr>\n')
					resp.write(
						f'<td><a href="{sites_status[x]["Address"]}" target="_blank">{sites_status[x]["Address"]}</a></td>\n')
					if sites_status[x]["H_Code"] == "200":
						resp.write(f'<td style="color: green;">{sites_status[x]["H_Code"]}</td>\n')
						resp.write(f'<td style="color: green;">{sites_status[x]["H_Response"]}</td>\n')
					elif sites_status[x]["H_Code"] == "301":
						resp.write(f'<td>{sites_status[x]["H_Code"]}</td>\n')
						resp.write(f'<td>{sites_status[x]["H_Response"]}</td>\n')
					else:
						resp.write(f'<td style="color: red;">{sites_status[x]["H_Code"]}</td>\n')
						resp.write(f'<td style="color: red;">{sites_status[x]["H_Response"]}</td>\n')

					if sites_status[x]["Code"] == "200":
						resp.write(f'<td style="color: green;">{sites_status[x]["Code"]}</td>\n')
						resp.write(f'<td style="color: green;">{sites_status[x]["Response"]}</td>\n')
					else:
						resp.write(f'<td style="color: red;">{sites_status[x]["Code"]}</td>\n')
						resp.write(f'<td style="color: red;">{sites_status[x]["Response"]}</td>\n')
					resp.write(f'<td>{sites_status[x]["Last_Checked"]}</td>\n')
					if os.path.exists(f'{x}.png'):
						resp.write(f'<td><a href="{x}.png" target="_blank"><img src="{x}.png" width="125px"></a></td>\n')
					else:
						resp.write(f'<td>No Screenshot Available</td>\n')
					resp.write('</tr>\n')

		sleep_time = 300
		while sleep_time > 0:
			print(f'Sleeping. {int(sleep_time/60)} minutes remaining.')
			time.sleep(60)
			sleep_time -= 60

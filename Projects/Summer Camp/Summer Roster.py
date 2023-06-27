# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import glob
	import csv
	import os
	import os.path
	import re

	classes = [file for file in glob.glob(f'./Classes/*.csv')]
	for _ in classes:
		os.remove(_)

	june_kids = dict()
	july_kids = dict()

	june_count = dict()
	july_count = dict()
	session_list = [file for file in glob.glob(f'./*.csv')]
	for session in session_list:
		with open(session, 'r', newline='') as file:
			session_data = csv.DictReader(file)
			for session_row in session_data:
				class_name = session_row["Class"].split("/")[0].strip()
				session_name = session_row["Session"].split("/")[0].strip()
				child_name = session_row["Child Name"].strip()

				june_count[class_name] = 0
				july_count[class_name] = 0

				if "June" in session_name:
					june_kids.update({f'{child_name}_{class_name}': session_row})

				if "July" in session_name:
					july_kids.update({f'{child_name}_{class_name}': session_row})

				if "Both" in session_name:
					june_kids.update({f'{child_name}_{class_name}': session_row})
					july_kids.update({f'{child_name}_{class_name}': session_row})

				if not os.path.isfile(f'./Classes/{class_name}.csv'):
					with open(f'./Classes/{class_name}.csv', 'w', newline='') as class_file:
						for _ in session_row:
							class_file.write(f'{_},')
						class_file.write(f'\n')

	for sign_up in june_kids.values():
		class_name = sign_up["Class"].split("/")[0].strip()
		if class_name in june_count:
			june_count[class_name] += 1
		else:
			june_count[class_name] = 1

	for sign_up in july_kids.values():
		class_name = sign_up["Class"].split("/")[0].strip()
		if class_name in july_count:
			july_count[class_name] += 1
		else:
			july_count[class_name] = 1

	for sign_up in june_kids.values():
		class_name = sign_up["Class"].split("/")[0].strip()
		session_name = sign_up["Session"].split("/")[0].strip()
		child_name = sign_up["Child Name"].strip()
		with open(f'./Classes/{class_name}.csv', 'a', newline='') as class_file:
			class_file.write(f'{sign_up["Timestamp"]},')
			class_file.write(f'{sign_up["Email Address"]},')
			class_file.write(f'{sign_up["Parent Name"]},')
			class_file.write(f'{sign_up["Phone Number"]},')
			class_file.write(f'{child_name},')
			class_file.write(f'{class_name},')
			class_file.write(f'{session_name},')
			class_file.write(f'{sign_up["Meals?"]},')
			class_file.write(f'{sign_up["Age"]}\n')

	class_list = [file for file in glob.glob(f'./Classes/*.csv')]
	for class_file in class_list:
		class_name = re.match(r'\.\/Classes\\(.+)\.csv',class_file )
		with open(class_file, 'a', newline='') as classes:
			classes.write(f'Total:,')
			classes.write(f'{june_count[class_name[1]]}')
			classes.write(f'\n\n')

	for sign_up in july_kids.values():
		class_name = sign_up["Class"].split("/")[0].strip()
		session_name = sign_up["Session"].split("/")[0].strip()
		child_name = sign_up["Child Name"].strip()
		with open(f'./Classes/{class_name}.csv', 'a', newline='') as class_file:
			class_file.write(f'{sign_up["Timestamp"]},')
			class_file.write(f'{sign_up["Email Address"]},')
			class_file.write(f'{sign_up["Parent Name"]},')
			class_file.write(f'{sign_up["Phone Number"]},')
			class_file.write(f'{child_name},')
			class_file.write(f'{class_name},')
			class_file.write(f'{session_name},')
			class_file.write(f'{sign_up["Meals?"]},')
			class_file.write(f'{sign_up["Age"]}\n')

	class_list = [file for file in glob.glob(f'./Classes/*.csv')]
	for class_file in class_list:
		class_name = re.match(r'\.\/Classes\\(.+)\.csv', class_file)
		with open(class_file, 'a', newline='') as classes:
			classes.write(f'Total:,')
			classes.write(f'{july_count[class_name[1]]}')

else:
	# Code here executed when imported (As a module)
	pass
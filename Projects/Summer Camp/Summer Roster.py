# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import glob
	import csv
	import os
	import os.path

	class_list = [file for file in glob.glob(f'./Classes/*.csv')]
	for class_file in class_list:
		os.remove(class_file)

	file_list = [file for file in glob.glob(f'./*.csv')]
	for file in file_list:
		with open(file, 'r', newline='') as current_file:
			sign_ups = csv.DictReader(current_file)
			june_kids = dict()
			june_count = 0
			july_kids = dict()
			july_count = 0
			for row in sign_ups:
				if "June" in row["Session"]:
					june_kids.update({f'{row["Child Name"]}_{row["Class"].split("/")[0].strip()}': row})
					june_count += 1

				if "July" in row["Session"]:
					july_kids.update({f'{row["Child Name"]}_{row["Class"].split("/")[0].strip()}': row})
					july_count += 1

				if "Both" in row["Session"]:
					june_kids.update({f'{row["Child Name"]}_{row["Class"].split("/")[0].strip()}': row})
					june_count += 1
					july_kids.update({f'{row["Child Name"]}_{row["Class"].split("/")[0].strip()}': row})
					july_count += 1

				class_name = row['Class'].split('/')[0].strip()
				if not os.path.isfile(f'./Classes/{class_name}.csv'):
					with open(f'./Classes/{class_name}.csv', 'w', newline='') as class_file:
						for _ in row:
							class_file.write(f'{_},')
						class_file.write(f'\n')

			for _ in june_kids.values():
				with open(f'./Classes/{_["Class"].split("/")[0].strip()}.csv', 'a', newline='') as class_file:
					class_file.write(f'{_["Timestamp"]},')
					class_file.write(f'{_["Email Address"]},')
					class_file.write(f'{_["Parent Name"]},')
					class_file.write(f'{_["Phone Number"]},')
					class_file.write(f'{_["Child Name"]},')
					class_file.write(f'{_["Class"].split("/")[0].strip()},')
					class_file.write(f'{_["Session"].split("/")[0].strip()},')
					class_file.write(f'{_["Meals?"]}\n')

			class_list = [file for file in glob.glob(f'./Classes/*.csv')]
			for class_file in class_list:
				with open(class_file, 'a', newline='') as classes:
					classes.write(f'Total: ,')
					classes.write(f'{len(june_kids)},')
					classes.write(f'\n')
					classes.write(f'\n\n')

			for _ in july_kids.values():
				with open(f'./Classes/{_["Class"].split("/")[0].strip()}.csv', 'a', newline='') as class_file:
					class_file.write(f'{_["Timestamp"]},')
					class_file.write(f'{_["Email Address"]},')
					class_file.write(f'{_["Parent Name"]},')
					class_file.write(f'{_["Phone Number"]},')
					class_file.write(f'{_["Child Name"]},')
					class_file.write(f'{_["Class"].split("/")[0].strip()},')
					class_file.write(f'{_["Session"].split("/")[0].strip()},')
					class_file.write(f'{_["Meals?"]}\n')
					class_file.write(f'Total: ,')
					class_file.write(f'{len(july_kids)},')
					class_file.write(f'\n')

else:
	# Code here executed when imported (As a module)
	pass

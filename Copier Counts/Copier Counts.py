# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here executed when invoked directly (Not a module)
	import csv


	def create_code_name_pair(csv_file):
		code_name_pair = {}
		with open(csv_file, 'r', newline='') as file:
			reader = csv.reader(file)
			next(reader)  # Skip the first line
			for column in reader:
				if len(column) >= 2:  # Ensure there are at least 2 columns
					code, name = column[1], column[0]
					code_name_pair[code] = name
		return code_name_pair


	def read_column_from_csv(csv_file, column_index):
		column_values = set()
		with open(csv_file, 'r', newline='') as file:
			reader = csv.reader(file)
			next(reader)  # Skip the first line
			for row in reader:
				if len(row) > column_index:
					column_values.add(row[column_index])
		return column_values


	def create_code_count_pair(csv_file):
		code_count_pair = {}
		with open(csv_file, 'r', newline='') as file:
			reader = csv.reader(file)
			next(reader)  # Skip the first line
			for column in reader:
				if len(column) >= 3:  # Ensure there are at least 2 columns
					code, count = column[0], column[2]
					code_count_pair[code] = count
		return code_count_pair


	def write_to_csv(codes_tuple, code_name_dict, lounge_code_count_dict, workroom_code_count_dict, copy_counts_csv):
		with open(copy_counts_csv, 'w', newline='') as outfile:
			writer = csv.writer(outfile)
			writer.writerow(["ID", "Name", "Count"])
			for code in codes_tuple:
				name = code_name_dict.get(code)
				if not name:
					continue
				try:
					lounge_count = int(lounge_code_count_dict[code])
				except KeyError:
					lounge_count = 0

				try:
					workroom_count = int(workroom_code_count_dict[code])
				except KeyError:
					workroom_count = 0

				count_total = lounge_count + workroom_count
				writer.writerow([code, name, count_total])


	# Code/Name pairs
	code_names_csv = 'Access Control List - Copier Codes.csv'
	code_name_dict = create_code_name_pair(code_names_csv)

	# Create active codes tuple, dictionary of lounge and workroom code/count pairs
	lounge_code_counts_csv = 'lounge.csv'
	lounge_codes = read_column_from_csv(lounge_code_counts_csv, 0)
	lounge_code_count_dict = create_code_count_pair(lounge_code_counts_csv)

	workroom_code_counts_csv = 'workroom.csv'
	workroom_codes = read_column_from_csv(workroom_code_counts_csv, 0)
	workroom_code_count_dict = create_code_count_pair(workroom_code_counts_csv)

	codes_tuple = tuple(lounge_codes.union(workroom_codes))

	# Write matching information to the output CSV file
	copy_counts_csv = 'Copy Counts.csv'
	write_to_csv(codes_tuple, code_name_dict, lounge_code_count_dict, workroom_code_count_dict, copy_counts_csv)

else:
	# Code here executed when imported (As a module)
	pass

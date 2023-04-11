# Code here is always executed
# from rich.traceback import install

# install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import glob
	import csv
	from datetime import date

	def report_gen():
		report_names = dict()
		report_path = '.\\Put_TimeTrax_Exports_Here'
		report_list = [file for file in glob.glob(f'{report_path}\\*')]

		for report_name in report_list:
			print(f'Report name: {report_name}')
			with open(report_name, newline='') as current_report:
				report_lines = csv.reader(current_report)
				for row in report_lines:
					if len(row) == 3:
						if "Missed Out" in row:
							staff_names = report_names.get(row[1])
							try:
								staff_names.add(row[0].strip())
							except AttributeError:
								staff_names = {row[0].strip()}

							report_names.update({row[1]: staff_names})

		for date_k, name_v in report_names.items():
			date_nice = "-".join((date_k[6:], date_k[0:2], date_k[3:5]))
			if date_nice == str(date.today()):
				continue
			with open(f'.\\Reports\\{date_nice}.txt', 'w', newline='') as output_report:
				for employee in name_v:
					output_report.write(f'{employee}\n')
			print(f'Output name, data: {date_k}, {name_v}')

	def offense_count():
		offenders = dict()
		output_path = '.\\Reports'
		output_list = [file for file in glob.glob(f'{output_path}\\*')]
		report_date = []

		if not output_list:
			return

		for output_name in output_list:
			report_date.append("".join((output_name[10:14], output_name[15:17], output_name[18:20])))
			with open(output_name, newline='') as output_report:
				output_lines = csv.reader(output_report)
				for row in output_lines:
					offender = ",".join(row)
					try:
						offenders.update({offender: offenders.get(offender)+1})
					except TypeError:
						offenders.update({offender: 1})

		offenders = dict(sorted(offenders.items(), key=lambda x: x[1], reverse=True))

		report_date_min = min(report_date)
		report_date_min = "-".join((report_date_min[:4], report_date_min[4:6], report_date_min[6:]))
		report_date_max = max(report_date)
		report_date_max = "-".join((report_date_max[:4], report_date_max[4:6], report_date_max[6:]))

		with open(f'.\\Count_Report.csv', 'w', newline='') as count_report:
			count_report.write(f'Report Start Date:,Report End Date:\n')
			count_report.write(f'{report_date_min},{report_date_max}\n\n')
			count_report.write(f'Name,Offense Count\n')
			for offender_k, count_v in offenders.items():
				count_report.write(f'"{offender_k}",{count_v}\n')
				print(f'Sorted offender counts: {offender_k}, {count_v}')

	report_gen()
	offense_count()

else:
	# Code here executed when imported (As a module))
	pass

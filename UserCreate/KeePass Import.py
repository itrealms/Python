# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here executed when invoked directly (Not a module)
	from pykeepass import PyKeePass

	def read_pass():
		pass_path = 'C:/Users/jason.swing/IT/Scripts/REALMS_DB.pass'
		with open(pass_path) as pass_file:
			return pass_file.readline().rstrip()

	# Open Password DB
	kp = PyKeePass('I:/REALMS_DB.kdbx', password=read_pass())
	group = kp.find_groups(name='Staff & Student Logins', first=True)

	# Read bulk user entries
	with open('C:/Users/jason.swing/IT/Scripts/Data Files/Add User.csv', "r") as au:
		next(au)
		users = [user.rstrip() for user in au.readlines()]

	for user in users:
		user = user.split(',')
		name = f'{user[2]} {user[3]}'
		username = user[5]
		password = user[6]
		if user[7] == '0000':
			notes = ''
		else:
			notes = user[7]

		try:
			kp.add_entry(group, name, username, password, notes=notes)
		except Exception:
			entry = kp.find_entries(title=name, first=True)
			notes = entry.notes + f'\n{notes}'
			entry.username = username
			entry.notes = notes
		finally:
			kp.save()

else:
	# Code here executed when imported (As a module)
	pass

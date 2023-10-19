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

	title = 'test 01'
	username = 'myusername'
	password = 'mypass'
	notes = '1234'

	kp = PyKeePass('I:/REALMS_DB.kdbx', password=read_pass())
	group = kp.find_groups(name='Staff & Student Logins', first=True)
	kp.add_entry(group, title, username, password, notes=notes)
	kp.save()

else:
	# Code here executed when imported (As a module)
	pass

# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here executed when invoked directly (Not a module)
	from pykeepass import PyKeePass

	kp = PyKeePass('C:/Users/jason.swing/IT/Test_DB.kdbx', password='12345')
	group = kp.find_groups(name='General', first=True)

	title = 'test 01'
	username = 'username'
	password = 'password'
	notes = 'notes 4'

	try:
		kp.add_entry(group, title, username, password, notes=notes)
	except Exception as error:
		entry = kp.find_entries(title=title, first=True)
		notes = entry.notes + f'\n{notes}'
		entry.username = username
		entry.password = password
		entry.notes = notes
	finally:
		kp.save()

else:
	# Code here executed when imported (As a module)
	pass

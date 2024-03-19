import datetime
import random
import re
import pykeepass
from pykeepass import PyKeePass


def read_pass():
	if not (keepass := input('Password to open database: ')):
		exit('Password required')
	else:
		return keepass


def add_keepass(ent_title, ent_username, ent_password, ent_notes):
	kp = PyKeePass('I:/REALMS_DB.kdbx', password=read_pass())
	group = kp.find_groups(name='Staff & Student Logins', first=True)

	if ent_notes == '0000':
		ent_notes = ''

	try:
		kp.add_entry(group, ent_title, ent_username, ent_password, notes=ent_notes)
	except Exception:
		entry = kp.find_entries(title=ent_title, first=True)
		ent_notes = entry.notes + f'\n{ent_notes}'
		entry.username = ent_username
		entry.password = ent_password
		entry.notes = ent_notes
	finally:
		kp.save()


def clean_name(n):
	n = n.strip()
	n = re.sub(r"[^a-zA-Z0-9'é]+", "-", n)
	return n


def clean_uname(n):
	n = re.sub(r"['\"]", "", n)
	n = re.sub(r"[ -]+", "-", n)
	n = re.sub(r"é", "e", n)
	return n.lower()


def gen_copy_code():
	return str(random.randrange(1111, 10000))


def gen_pass():
	word_count = len(word_list)
	word1 = word_list[random.randrange(0, word_count)].capitalize()
	word2 = word_list[random.randrange(0, word_count)].capitalize()
	spec = ("!", "@", "#", "$", "%", "^", "&", "*")[random.randrange(0, 8)]
	num = str(random.randrange(0, 10))
	return "".join([word1, word2, spec, num])


with open('./wordlist.txt') as wl:
	word_list = [word.rstrip() for word in wl.readlines()]

with open('./Add User.csv', "w") as au:
	au.write('Timestamp,Grade,First,Last,Email,Username,Password,Copier\n')

while True:
	time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")

	if not (first_name := clean_name(input('First Name: '))):
		break
	if not (last_name := clean_name(input('Last Name: '))):
		break
	if not (grade := input('Grade/Description: ')):
		break

	name = f'{first_name} {last_name}'

	first_uname = re.search(r"\w+", clean_uname(first_name)).group()
	last_uname = clean_uname(last_name)
	email = f'{first_uname}.{last_uname}@rcrealms.org'

	if len(first_uname) + len(last_uname) >= 20:
		last_uname = re.search(r"\w+", last_uname).group()
	username = ".".join([first_uname, last_uname])[:20]
	email = f'{username}@rcrealms.org'

	password = gen_pass()

	if grade not in str([-1, 0, 1, 2, 3, 4, 5, 6]):
		copier = gen_copy_code()
	else:
		copier = '0000'

	# Add entry to keepass
	add_keepass(name, username, password, copier)

	# Add user info to .csv for secondary script
	user_data = ",".join([time_stamp, grade, first_name, last_name, email, username, password, copier])
	with open('./Add User.csv', "a") as nu:
		nu.write(f'{user_data}\n')
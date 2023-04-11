import datetime
import random
import re
import os


def clean_name(n):
	n = n.strip()
	n = re.sub(r"\s+", " ", n)
	n = re.sub(r"-+", "-", n)
	n = re.sub(r" - ", "-", n)
	n = re.sub(r"-+", "-", n)
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


with open('../PassGen/files/wordlist.txt') as wl:
	word_list = [word.rstrip() for word in wl.readlines()]

with open('C:/Users/jason.swing/IT/Scripts/Data Files/Add User.csv', "w") as au:
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

	password = gen_pass()

	if grade not in str([-1, 0, 1, 2, 3, 4, 5, 6]):
		with open('C:/Users/jason.swing/IT/Scripts/Data Files/copy_codes.txt') as cl:
			copier_list = [code.rstrip() for code in cl.readlines()]

		with open('C:/Users/jason.swing/IT/Scripts/Data Files/copy_codes.txt', "a") as cl:
			while (copier := gen_copy_code()) in copier_list:
				copier = gen_copy_code()
			cl.write(f'\n{copier}')
	else:
		copier = '0000'

	user_data = ",".join([time_stamp, grade, first_name, last_name, email, username, password, copier])

	with open('C:/Users/jason.swing/IT/Scripts/Data Files/Add User.csv', "a") as nu:
		nu.write(f'{user_data}\n')

	with open('C:/Users/jason.swing/IT/Scripts/Data Files/User Creation Log.csv', "a") as nu:
		nu.write(f'{user_data}\n')

	with open(f'C:/Users/jason.swing/IT/Scripts/Data Files/Users/{username}.txt', "w") as nu:
		nu.write(name)
		nu.write(f'\n{email}')
		nu.write(f'\n{password}')
		nu.write(f'\n{copier}\n')

		nu.write(f'\n{grade}\t{first_name}\t{last_name}\n')

		nu.write(f'\nAdded: {name}\n')

		nu.write(f'\nUsername: {username}')
		nu.write(f'\nEmail: {email}')
		nu.write(f'\nPassword: {password}')

	os.system(f'start C:/Users/jason.swing/IT/Scripts/"Data Files"/Users/{username}.txt')

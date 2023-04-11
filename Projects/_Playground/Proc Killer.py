# import wmi library
import wmi

# This variable ti would be used
# as a parity and counter for the
# terminating processes
ti = 0

# This variable stores the name
# of the process we are terminating
# The extension should also be
# included in the name
name = 'chromedriver.exe'

# Initializing the wmi object
f = wmi.WMI()

# Iterating through all the
# running processes
for process in f.Win32_Process():

	# Checking whether the process
	# name matches our specified name
	if process.name == name:
		# If the name matches,
		# terminate the process
		process.Terminate()

		# This increment would acknowledge
		# about the termination of the
		# Processes, and would serve as
		# a counter of the number of processes
		# terminated under the same name
		ti += 1

# True only if the value of
# ti didn't get incremented
# Therefore implying the
# process under the given
# name is not found
if ti == 0:
	# An output to inform the
	# user about the error
	print("Process not found!!!")

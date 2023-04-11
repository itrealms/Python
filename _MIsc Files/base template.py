# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)

	def hello_world():
		print('Hello World')
		return

	hello_world()

else:
	# Code here executed when imported (As a module))
	pass

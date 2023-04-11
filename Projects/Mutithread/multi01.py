# Code here is always executed
import random
import time
from concurrent import futures
from rich.traceback import install
install()


def waste_time(thread_count):
	wait_time = random.randrange(10)
	print(f'wait_time={wait_time}')
	time.sleep(wait_time)

	return thread_count


with futures.ThreadPoolExecutor() as exe:
	_threads = []
	for x in range(10):
		_threads.append(exe.submit(waste_time, x))
	for _threads_completed in futures.as_completed(_threads):
		print(f'Thread number = {_threads_completed.result()}')

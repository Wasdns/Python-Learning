#!/usr/bin/env python3

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('wasdns')
def now():
	print('2017/2/19')

def main():
	f = now
	f()
	print(now.__name__)
	print(f.__name__)	

if __name__ == '__main__':
	main()
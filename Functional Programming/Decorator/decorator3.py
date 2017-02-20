#!/usr/bin/env python3

import functools

def log1(func):
	print('begin call')
	func()
	def wrapper(*args, **kw):
		print('end call')
	
	return wrapper

@log1
def func():
	print('Hey Girl')

def main():
	func()

if __name__ == '__main__':
	main()
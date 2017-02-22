#!/usr/bin/env python3

import sys

def _func1(name):
	print('Hello, %s' % name)

def _func2(name):
	# do no thing
	return

def main():
	args = sys.argv

	if len(args) == 1:
		print('Error: miss args')
	elif len(args) == 2:
		_func1(args[1])
	else :
		_func2(args[1])


if __name__ == '__main__':
	main()
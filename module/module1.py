#!/usr/bin/env python3

import sys

'a test module'

__author__ = 'wasdns'

def main():
	args = sys.argv
	if len(args) == 1:
		print('Hello')
	elif len(args) == 2:
		print('Hello, %s' % args[1])
	else :
		print('Your network has some problem.\n')
		print('Please change your network environment')

if __name__ == '__main__':
	main()
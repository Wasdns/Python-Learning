#!/usr/bin/env python3

import os

def main():
	print(os.name) # print the name of OS
	print(os.uname) # print the details

	print(os.environ) # print the environment variables of OS
	print(os.environ.get('PATH')) # get the PATH env variable 

if __name__ == '__main__':
	main()

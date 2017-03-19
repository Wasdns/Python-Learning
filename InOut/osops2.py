#!/usr/bin/env python3

import os

def main():
	# 当前目录的绝对路径
	print(os.path.abspath('.'))

	path = os.path.abspath('.')

	# 加入目录'Hi'
	os.path.join(path, 'Hi')

	# mkdir
	os.mkdir(path+'/Hi')

	# rm -rf
	os.rmdir(path+'/Hi')

	l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
	print(l)

if __name__ == '__main__':
	main()

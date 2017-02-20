#!/usr/bin/env python3

import functools

def int2(a, b):
	return int(a, b)

def main():

	int_2 = functools.partial(int, base=2) # int函数, 固定参数base=2

	print(int_2('10001'))
	# print(int_2('100'))

	# print(int(input(), base=2))
	# print(int(input(), base=16))

	# print(int2(input(), 2))

	max_2 = functools.partial(max, 10)
	print(max_2(5, 6, 7))

if __name__ == '__main__':
	main()
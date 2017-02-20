#!/usr/bin/env python3

def func(x, y):
	return lambda: x*y

def main():
	f = lambda x: x*x
	print(f(int(input())))

	# no sense
	f1 = func(int(input()), int(input()))
	print(f1)

if __name__ == '__main__':
	main()
#!/usr/bin/env python3

def func(x):
	return x*x

def main():
	lis = list(map(lambda x: x*x, [1, 2, 3, 4, 5]))
	print(lis)

if __name__ == '__main__':
	main()
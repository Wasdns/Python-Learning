#!/usr/bin/env python3

def addtwonums(a, b) :
	return a+b

def func(a, b, f) :
	return f(a, b)

def main() :
	a = int(input())
	b = int(input())
	f = addtwonums

	print(func(a, b, f))

if __name__ == '__main__':
	main()
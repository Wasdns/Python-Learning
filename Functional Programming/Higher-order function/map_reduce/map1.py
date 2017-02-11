#!/usr/bin/env python3

from functools import reduce

def f(x) :
	return x*x

l = map(f, [1, 2, 3, 4, 5, 6, 7])

print(list(l))

l1 = map(str, [1, 2, 3, 4, 5, 6, 7])

print(l1)

print(list(l1))

def f1(x, y) :
	return x+y

l2 = reduce(f1, [1, 2, 3, 4, 5])

print(l2)

l3 = reduce(f1, 'string')

print(list(l3))

def f2(x, y) :
	return x*10 + y

l4 = reduce(f2, [1, 2, 3, 4, 5])

print(l4)

def func(s) :
	def func1(x) :
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x]
	def func2(x, y) :
		return x*10 + y

	return reduce(func2, map(func1, s))

s = input()

print(func(s))

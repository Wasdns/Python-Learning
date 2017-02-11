#!/usr/bin/env python3

from functools import reduce

def prod(l) :

	def func(x, y) :
		return x*y

	return reduce(func, l)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
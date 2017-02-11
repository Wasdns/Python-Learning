#!/usr/bin/env python3

from functools import reduce

def str2float(s) :
	floatlen = 0
	s1 = ''
	flag = True
	
	for i in s :
		if i == '.' :
			flag = False
			continue
		else :
			s1 = s1+i

		if flag :
			floatlen = floatlen+1

	floatlen = len(s)-floatlen-1

	def mapfunc(s) :
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
		# return {}[]
	
	def reductfunc(x, y) :
		return x*10+y

	return reduce(reductfunc, map(mapfunc, s1)) / (10 ** floatlen)

print('str2float(\'123.456\') =', str2float('123.456'))

print('str2float(\'123.978\') =', str2float('123.978'))

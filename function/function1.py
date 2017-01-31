#!/usr/bin/env python3

import math

def my_function(age, x) :

	if age < 0:
		raise RuntimeError('age < 0')
	else :
		pass

	if not isinstance(x, (str)) :
		raise TypeError('bad operand type') 
	else :
		pass

	if str(x) == 'Chen' :
		b = 'Good'
	elif str(x) == 'Li' :
		b = 'Better'
	else :
		b = 'Best'

	print(b)

	return b

def quadratic(a, b, c) :

	q = b*b - 4*a*c

	if q > 0 :
		x1 = -b + math.sqrt(q)
		x2 = -b - math.sqrt(q)
		return x1/(2*a), x2/(2*a)
	else :
		print('No solutions')
 







#!/usr/bin/env python3

def my_func(name, age, **kw) :
	
	if 'prof' in kw :
		print('prof in')

	if 'city' in kw :
		print('city in')

	print('name:', name, 'age:', age, 'else:', kw)

def my_func2(name, age, *, prof, city) :

	print(name, age, prof, city)

def my_func3(a, b, c=0, *d, **e) :
	print(a, b, c, d, e)

	


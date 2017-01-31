#!/usr/bin/env python3

def power(x, n=2) :
	i = 1
	a = 1
	
	while i <= n :
		a = a * x
		i = i + 1

	return a

def my_function(name, age, 
	prof = 'Student', city = 'FuZhou') :
	
	print(name, age, prof, city)

	return

def function3(L=[]) :
	
	L.append('EOF')

	return L

def function4(*number) :
	
	res = 0

	for i in number :
		res += i*i

	print(res)

	return





#!/usr/bin/env python3

def my_func(n) :
	if n == 1 :
		return 1
	return n * my_func(n-1)

def my_func_2(num, product) :
	if num == 1 :
		return product
	return my_func_2(num-1, num*product)

def move(n, a, b, c) :
	if (n == 1) :			# A move last one to C
		print(a, '=>', c)
		return
	else :
		move(n-1, a, c, b)	# from A move n-1 to B 
		move(1, a, b, c)	# A move last one to C
		move(n-1, b, a, c)	# from B move n-1 to C


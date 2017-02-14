#!/usr/bin/env python3

L = []

# input 10 integers
for i in range(10) :
	L.append(int(input()))

# define filter function => bool judge
def filter_func(x) :
	return x%2 == 1

print(list(filter(filter_func, L)))
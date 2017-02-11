#!/usr/bin/env python3

def func(name) :
	return name.title()

l = ['adam', 'LISA', 'barT']

itor_l = map(func, l)

print(list(itor_l))

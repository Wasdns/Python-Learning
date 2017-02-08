#!/usr/bin/env python3

for i in [1, 2, 3, 4, 5]:
    print(i)

it = iter([1, 2, 3, 4, 5]) # get iterator

while True :
	try :
		x = next(it)
		print(x)
	except StopIteration :
		break


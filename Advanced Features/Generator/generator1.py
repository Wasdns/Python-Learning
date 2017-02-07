#!/usr/bin/env python3

L = [i*i for i in range(1, 11)]

G = (i*i for i in range(1, 11))

print(L)

print(G)

for i in G :
	print(i)

# maxn = int(input())

def fib(maxn) :
	i, a, b = 1, 1, 1
	print(1)
	while i < maxn:
		print(b)
		a, b = b, a+b
		i = i+1

def fib1(maxn) :
	i, a, b = 0, 0, 1
	while i < maxn:
		yield(b)
		a, b = b, a+b
		i = i+1

def exp():
	print('step 1:')
	yield(1)
	
	print('step 2:')
	yield(3)

	print('step 3:')
	yield(5)

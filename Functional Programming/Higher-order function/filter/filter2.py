#!/usr/bin/env python3

# define a filter function
def filter_func(x) :
	return lambda i: i%x > 0

# Iterator A: Initial Array
def creater() :
	n = 1
	while True:
		n = n+2
		yield(n)

def E_primes() :
	yield(2)
	it = creater() # Initial array
	while True:
		n = next(it) # iterator => next()
		yield(n) 
		it = filter(filter_func(n), it) # creat new array

def main() :
	primes = []
	for i in E_primes() :
		if i <= 1000 :
			primes.append(i)
		else :
			break
	print(primes)

if __name__ == '__main__':
	main()
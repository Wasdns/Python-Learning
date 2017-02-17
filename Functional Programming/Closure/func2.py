#!/usr/bin/env python

def count():
	ans = []
	for i in range(1, 4):
		def f():
			return i*i
		ans.append(f)
	return ans

def count1():
	ans = []
	def f():
		for i in xrange(1, 4):
			ans.append(i)
		return ans
	return f

def main():

	a1, a2, a3 = count1(), count1(), count1()
	print(a1())
	print(a2())
	print(a3())

	f1, f2, f3 = count() 
	print(f1())
	print(f2())
	print(f3())

"""
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
9
9
9
"""

if __name__ == '__main__':
	main()
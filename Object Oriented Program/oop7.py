#!/usr/bin/env python3

from types import MethodType

class MyClass(object):
	def __init__(self):
		pass

def f(self):
	print('I\'m new here!')

def func(obj):
	print(obj.name, obj.age)

def main():
	h = MyClass()
	h.name = 'Chen'
	h.age = '20'
	func(h)

	h.f = MethodType(f, h)
	h.f()

	MyClass.f = f

	h1 = MyClass()
	h1.f()

if __name__ == '__main__':
	main()
#!/usr/bin/env python3

class Myclass(object):
	"""docstring for Myclass"""
	def __init__(self):
		super(Myclass, self).__init__()

	def func(self):
		pass

def run(self):
	print("running")

def main():
	h = Myclass()
	print(type(h))

	NewClass = type('NewClass', (Myclass,), dict(func=run))
	h1 = NewClass()
	h1.func()

if __name__ == '__main__':
	main()

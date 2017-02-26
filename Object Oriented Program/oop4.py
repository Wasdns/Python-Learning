#!/usr/bin/env python3

class Animal(object):
	"""docstring for Animal"""
	def __init__(self):
		pass
	def run(self):
		print('Animal is running.')
	def printname(self):
		print('Animal')

class Dog(Animal):
	"""docstring for Dog"""
	def run(self):
		print('Dog is running')
	def printname(self):
		print('Dog')

class Cat(object):
	"""docstring for Cat"""
	def run(self):
		print('Cat is running')
	def printname(self):
		print('Cat')

def Animal_func(obj):
	obj.run()

def main():
	a = Animal()
	b = Dog()
	c = Cat()
	a.run()
	b.run()
	c.run()

	Animal_func(a)
	Animal_func(b)
	Animal_func(c)

if __name__ == '__main__':
	main()
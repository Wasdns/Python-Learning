#!/usr/bin/env python3

class Animal(object):
	"""docstring for Animal"""
	def __init__(self):
		self.name = 'animal'
	def run(self):
		print('animal run')
	def getname(self):
		print(self.name)

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		self.name = 'Dog'
	def run(self):
		print('dog run')
	def getname(self):
		print(self.name)

def main():
	a = Animal()
	b = Dog()

	if isinstance(a, Animal):
		print('a is animal')
	if isinstance(b, Animal):
		print('b is animal')
	if isinstance(a, Dog):
		print('a is dog')
	if isinstance(b, Dog):
		print('b is dog')

if __name__ == '__main__':
	main()


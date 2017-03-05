#!/usr/bin/env python3

class Animal(object):
	def __init__(self, name):
		self.name = name
	def getname(self):
		print(self.name)

class Fly(object):
	def __init__(self):
		pass
	def getfly(self):
		print('could fly')

class Bird(Animal, Fly):
	pass

def main():
	b = Bird('bird')
	b.getname()
	b.getfly()

if __name__ == '__main__':
	main()
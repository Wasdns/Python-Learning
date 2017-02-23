#!/usr/bin/env python3

class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def PrintINFO(self):
		print(self.name)
		print(self.score)

class Man(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

def fuck():
	print('Sleep with my girlfriend')

def main():
	bart = Student('Bart Simpson', 59)
	lisa = Student('Lisa Simpson', 87)
	bart.PrintINFO()
	lisa.PrintINFO()

	I = Man('chen', 20)
	You = Man('xx', 20)

	I.havegirlfriend = True

	if I.havegirlfriend == True:
		fuck()
	
	if You.havegirlfriend == True:
		print('error')

if __name__ == '__main__':
	main()
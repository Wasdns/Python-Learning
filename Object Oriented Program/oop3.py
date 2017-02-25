#!/usr/bin/env python3

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, city):
		self.__name = name
		self.__age = age
		self.__city = city

	def print_info(self):
		print(self.__name, self.__age, self.__city)

	def changeinfo(self, option, value):
		if option == 'name':
			self.__name = value
		elif option == 'age':
			self.__age = value
		elif option == 'city':
			self.__city = value

def main():
	stu_a = Student('antonin', 20, 'SA')
	stu_a.__name = 'Chen'
	stu_a.print_info()

if __name__ == '__main__':
	main()
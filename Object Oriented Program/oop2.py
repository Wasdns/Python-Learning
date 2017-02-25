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
	student = Student('Chen', 20, 'FuZhou')
	student.print_info()
	cg = int(input())
	if cg == 0:
		student.changeinfo('name', input())
	elif cg == 1:
		student.changeinfo('age', int(input()))
	elif cg == 2:
		student.changeinfo('city', input())
	student.print_info()

if __name__ == '__main__':
	main()
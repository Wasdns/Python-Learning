#!/usr/bin/env python3

class MyClass(object):
	"""docstring for MyClass"""
	__slots__ = ('name', 'age')
	def __init__(self):
		super(MyClass, self).__init__()
		pass

class Student(MyClass):
	"""docstring for Student"""
	def __init__(self):
		super(Student, self).__init__()
		pass
		

def main():
	h = MyClass()
	h.name = 'Chen'
	h.age = 20
	# h.city = 'FuZhou'

	h1 = Student()
	h1.name = 'Chen'
	h1.age = 20
	h1.city = 'FuZhou'

	print(h1.name, h1.age, h1.city)

if __name__ == '__main__':
	main()
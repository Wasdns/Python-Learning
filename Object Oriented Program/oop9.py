#!/usr/bin/env python3

class MyClass(object):
	"""docstring for MyClass"""
	def __init__(self):
		super(MyClass, self).__init__()

	def set_Attr(self, score):
		if score >= 0 and score <= 100:
			self.score = score
		else:
			raise ValueError('Attribute Setting Error')

	def get_Attr(self):
		return self.score

class Student(object):
	"""docstring for Student"""
	def __init__(self):
		super(Student, self).__init__()
	
	@property
	def score(self): # turn into an attribute
		return self.score

	@score.setter
	def score(self, val):
		if val >= 0 and val <= 100:
			self.score = val
		else:
			raise ValueError('Attribute Setting Error')

def main():
	A = MyClass()
	A.score = 59
	print(A.get_Attr())

	# A.set_Attr(101)
	# print(A.get_Attr())

	B = Student()
	B.score = 59
	print(B.score)
	print('I am angry!')
	
	B.score = 999
	print(B.score)

if __name__ == '__main__':
	main()


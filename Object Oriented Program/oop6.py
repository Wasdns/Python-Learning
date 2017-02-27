#!/usr/bin/env python3

class MyClass(object):
	"""docstring for MyClass"""
	def __init__(self, name):
		super(MyClass, self).__init__()
		self.name = name
	def getname(self):
		print(self.name)

def main():
	me = MyClass('chen')
	me.getname()

	# get object attribute

	if hasattr(me, 'name'):
		print('me have attr name')
		getattr(me, 'name')
	if hasattr(me, 'age'):
		print('me have attr age')
		getattr(me, 'age')
	print('first judge finished')
	
	setattr(me, 'age', 20)

	if hasattr(me, 'age'):
		print('me have attr age')
		getattr(me, 'age')
	print('second judge finished')

	# get object function
	f = getattr(me, 'getname')
	f()

if __name__ == '__main__':
	main()
#!/usr/bin/env python3

class Listmetaclass(type):
	"""docstring for Listmetaclass"""
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class NewClass(list, metaclass=Listmetaclass):
	pass

def main():
	#NewClass = type('NewClass', (Listmetaclass,), dict())
	h = NewClass()
	h.add(1)
	print(h)

if __name__ == '__main__':
	main()

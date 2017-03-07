#!/usr/bin/env python3

from enum import Enum, unique

@unique
class Week(Enum):
	"""docstring for Week"""
	Sun = 0
	Mon = 1
	Tue = 2
	Thu = 3
	Wed = 4
	Fri = 5
	Sat = 6

def main():
	Mouth = Enum('Mouth', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
	for name, attr in Mouth.__members__.items():
		print(name, '=>', attr, '=>', attr.value)

	print(Week.Sun)
	print(Week['Tue'])
	print(Week.Fri.value)

if __name__ == '__main__':
	main()
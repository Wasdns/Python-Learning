#!/usr/bin/env python3

def main():
	"""
	try:
		file = open('/Users/wasdns/Desktop/Python-Learning/InOut/data.txt', 'r')
		print(file.read())
	finally:
		if file:
			file.close()
	
	"""

	with open('/Users/wasdns/Desktop/Python-Learning/InOut/data.txt', 'r') as file:
		print(file.read())
	
	file = open('/Users/wasdns/Desktop/Python-Learning/InOut/data.txt', 'r')
	for line in file.readlines():
		print(line.strip())
	file.close()
	
	with open('/Users/wasdns/Desktop/Python-Learning/InOut/data2.txt', 'w') as file:
		file.write('\nSee you next time~')
	with open('/Users/wasdns/Desktop/Python-Learning/InOut/data2.txt', 'r') as file:
		print(file.read())

if __name__ == '__main__':
	main()
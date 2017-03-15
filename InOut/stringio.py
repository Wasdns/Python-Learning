#!/usr/bin/env python

from io import BytesIO as StringIO

def main():
	f = StringIO()
	f.write('Hi')
	f.write(' ')
	f.write('all')
	print(f.getvalue())

	f1 = StringIO('Hi I am wasdns')
	s = f1.readline()
	print(s.strip())

if __name__ == '__main__':
	main()

#!/usr/bin/env python3

from io import BytesIO

def main():
	f = BytesIO()
	f.write('中文'.encode('utf-8'))
	print(f.getvalue())

	f1 = BytesIO('中文'.encode('utf-8'))
	print(f1.read())

if __name__ == '__main__':
	main()

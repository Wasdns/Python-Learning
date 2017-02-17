#!/usr/bin/env python3

def calsums(*args):
	ans = 0
	for i in args:
		ans = ans+i
	return ans

def slowcalsums(*args):
	def cal():
		ans = 0
		for i in args:
			ans = ans+i
		return ans
	return cal

def main():
	resf = slowcalsums(1, 2, 3, 4, 5)
	print(resf)
	print(resf())
	newresf = slowcalsums(1, 2, 3, 4, 5)
	if resf == newresf :
		print('Yeah')
	else :
		print('Noop')

if __name__ == '__main__':
	main()

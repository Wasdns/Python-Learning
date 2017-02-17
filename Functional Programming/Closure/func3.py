#!/usr/bin/env python

def slowfuck(args):
	pep = []
	def func():
		for i in args:
			pep.append(i)
		return pep
	return func

def main():
	L = ['Li', 'Wang', 'Huang', 'Cai', 'Chen']
	f1, f2, f3 = slowfuck(L), slowfuck(L), slowfuck(L)
	print(f1())
	print(f2())
	print(f3())

if __name__ == '__main__':
	main()
#!/usr/bin/env python3

"""
	Name: Python Calculator 1.0

	Support: add minus

	Created by Chen. 2017/2/8
"""

def calculator(stack):
	s1, s2 = [], []
	
	# handle the stack
	for i in stack:
		if i == '+' or i == '-' :
			s1.append(i)
		else :
			s2.append(int(i))
	
	s3, s4 = [], []

	# turn the list
	while len(s1) > 0 :
		s3.append(s1[-1])
		s1.pop()
	while len(s2) > 0 :
		s4.append(s2[-1])
		s2.pop()

	# calculate the result
	while len(s3) > 0 :
		cal, mid = s3[-1], 0
		
		if cal == '+' :
			mid = s4[-1]+s4[-2]
			s4.pop()
			s4.pop()
			s4.append(mid)
		
		elif cal == '-' :
			mid = s4[-1]-s4[-2]
			s4.pop()
			s4.pop()
			s4.append(mid)

		s3.pop()
	
	return s4[-1]

def main():
	print('Python Calculator 1.0')
	calstr = input()
	
	mid, s1 = '', []
	for i in range(len(calstr)) :
		if (calstr[i] == '+' or calstr[i] == '-' or calstr[i] == '=') and i != 0:
			if mid != '' :
				s1.append(mid)
				mid = ''
			s1.append(calstr[i])
		else :
			mid = mid + calstr[i]
	if mid != '' :
		s1.append(mid)

	if s1[-1] == '=' : # delete '='
		s1.pop() 

	res = calculator(s1)
	print(res)


if __name__ == '__main__':
	main()
#!/usr/bin/env python3

def triangles():
	i = 1
	L = []
	while i <= 10:
		L1 = []
		L1.append(1)
		
		if i > 1 :
			for j in range(1, i-1):
				# print('i', i, 'j', j)
				a, b = int(L[j]), int(L[j-1])
				# print(a, b)
				L1.append(a+b)

		if i > 1 : 
			L1.append(1)
		
		yield(L1)
		i = i+1
		L = L1

n = 0

for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

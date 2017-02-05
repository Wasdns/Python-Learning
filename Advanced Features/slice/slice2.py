#!/usr/bin/env python3

L = []

for i in range(100) :
	L.append(i)

print(L)

a = L[0:10] # L[:10]

print(a)

b = L[-10:] 

print(b)

c = L[10:20]

print(c)

d = L[:10:2] # 0 2 4 ...

print(d)

e = L[::5] # 0 5 10 15 ...

print(e)

strs = 'WhenProgrammingFeelingHappy'

strs1 = strs[:15]

print(strs1)

strs2 = strs[-12:]

print(strs2)


#!/usr/bin/env python3

L = ['Chen', 20, '952693358', 'cnblogs', 'Github']

newL1 = [L[0], L[1], L[2]]

print(newL1)

newL2 = []

for i in range(3) :
	newL2.append(L[i])

print(newL2)

slice1 = L[0:3]	# L[:3]

print(slice1)

slice1 = L[1:3]

print(slice1)

slice1 = L[-3:]

print(slice1)

slice1 = L[-3:-1]

print(slice1)


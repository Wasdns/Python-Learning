#!/usr/bin/env python3

L = []

for i in range(10):
	L.append(int(input()))

SortedL = sorted(L)

print(SortedL)

absortL = sorted(L, key=abs)

print(absortL)

L1 = []

for i in range(5):
	L1.append(input())

print(sorted(L1))

print(sorted(L1, key=str.lower))

print(sorted(L1, key=str.lower, reverse=True))



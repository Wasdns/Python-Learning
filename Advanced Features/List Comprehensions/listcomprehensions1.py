#!/usr/bin/env python3

import os

L1 = []

for i in range(1, 11) :
	L1.append(i*i)

print(L1)

L2 = [i*i for i in range(1, 11)]

print(L2)

L3 = [i*i for i in range(1, 11) if (i*i)%2 == 0]

print(L3)

L4 = [i+j for i in range(1, 11) for j in range(1, 11)]

print(L4)

L5 = [i+j for i in 'ABC' for j in 'abc']

print(L5)

L6 = [i for i in os.listdir('.')]

print(L6)

dic = {'Chen': 'Student', '952693358': 'QQ', 'Never-give-up-C-X': 'WeChat'}

L7 = [x+'='+y for x, y in dic.items()]

print(L7)

str1 = 'HeyGirl'

L8 = [i.lower() for i in str1]

print(L8)




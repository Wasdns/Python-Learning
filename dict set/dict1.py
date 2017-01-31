#!/usr/bin/env python3

score = {'Chen' : 90, 'Michael' : 89, 'Li' : 78, 'Wang' : 0}

score['Wang'] = 69		# dict['string'] = value

score['Wang'] = 79
	
print(score)

name = input()

print(score[name])

score.pop('Wang')	# dict.pop('string')

print(score.get('Wang', -1))

print(score)

dict0 = {(1, 2, 3) : 90}

print(dict0[(1, 2, 3)])

dict0 = {(1, 2, [3, 4]) : 90}

print(dict0[(1, 2, [3, 4])])


#!/usr/bin/env python3

h = float(input('Please input your height:'))

w = float(input('Please input your weight:'))

bmi = w / (h * h)

print('Your BMI is:', bmi)

if bmi < 18.5 :
	print('Thin')

elif bmi >= 18.5 and bmi < 25 :
	print('Normal')

elif bmi >= 25 and bmi < 28 :
	print('Overweight')

elif bmi >= 28 and bmi < 32 :
	print('Fat') 

else :
	print('Too Fat')
	print('You should stop eating!')
#!/usr/bin/env python3
import random

cows=0
bulls=0
while True:
	num=(input ("Enter a 4 digit number :"))
	if len(num)==4:
		break
	else:
		print('It should be of 4 digits only')
j= str(random.randint(0000,9999))
for k in range(0,4):
	if num[k]==j[k]:
		cows+=1
	else:
		bulls+=1
print('num={}'.format(num))
print('random={}'.format(j))
print("{}cows and {}bulls".format(cows,bulls))



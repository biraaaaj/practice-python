#!/usr/bin/env python3
num= int(input("Enter a number: "))
k=1
for i in range(2,int(pow(num,.5))):
	if num % i == 0:
		k=0
		print("Not a prime")
		break	
if k==1:
	print("Is prime")		
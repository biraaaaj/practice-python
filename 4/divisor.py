#!/usr/bin/env python3
num = int(input("Enter a no: "))
a = []
for i in range (2,num):
	if num % i == 0:
		a.append(i)
print(a)
	
#!/usr/bin/env python3
b=[]
num=int(input('How many elements? :'))
for i in range(0,num):
	a=input('Element =')
	b.append(a)
d=sorted(b)
c=input("Element that you want to search :")
print(d)
if c in d:
	print('{} is in list'.format(c))
else:
	print('{} is not in list'.format(c))

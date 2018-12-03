#!/usr/bin/env python3
b= input('enter a number :')
while True:
	c=0
	for i in str(b):
		c=c+int(i)**2
	print (c)
	if len(str(c))==1:
		if c==1:
			print('Happy')
		else:
			print('Not Happy')
		break
	else:
		b=c
		


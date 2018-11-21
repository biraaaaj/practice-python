#!/usr/bin/env python3
def func():
	array=[]
	while True:
		a=input("List element>> ")
		if a=='':
			break
		array.append(a)
	if len(array) < 2:
		print(array)
	else:
		print(array[0],array[-1])
	return
func()

 


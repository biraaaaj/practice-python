#!/usr/bin/env python3


class Rectangle:

	def __init__(self,l,b):
		hor = '-'
		ver = '|'

		self.l = l
		self.b = b
		s = ' '
		print (s + hor * 2 * l)
		for i in range(b):
			print(ver + s * 2 * l + ver)
		print (s + hor * 2 * l)

l = int(input('Enter the length :'))
b = int(input('Enter the breadth :'))	
Rectangle(l,b)


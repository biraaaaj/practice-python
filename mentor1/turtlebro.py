#!/usr/bin/env python3
import turtle

def circle():
	radius = int(input("Enter the radius :"))
	turtle.circle(radius)
	turtle.done()
	return

def rectangle():
	length = int(input("Enter the length of rectangle :"))
	breadth = int(input("Enter the breadth of rectangle :"))
	for i in range(2):
		turtle.forward(breadth)
		turtle.left(90)
		turtle.forward(length)
		turtle.left(90)
	turtle.done()
	return

def square():
	length = int(input("Enter the length of square :"))
	for i in range(4):
		turtle.forward(length)
		turtle.left(90)
	return

def triangle():
	side = int(input("Enter the side of the triangle :"))
	for i in range(3):
		turtle.forward(side)
		turtle.left(120)
	return

options = ('circle', 'rectangle', 'square', 'triangle')
choice = (input ("What do you want to draw? :"))
while choice in options:
	if choice == 'circle':
		circle()
		break
	elif choice == 'rectangle': 
		rectangle()
		break
	elif choice == 'square': 
		square()
		break
	elif choice == 'triangle': 
		triangle()
		break
	else: break
print('That option is not available')
	
#!/usr/bin/env python3
import random

a= random.randint(1,9)
b=int(input("Enter a random number: "))
if a==b:
	print("you guessed it right")
elif a>b:
	print("you guessed it low")
else:
	print("you guessed it high")
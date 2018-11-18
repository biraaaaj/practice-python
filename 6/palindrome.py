#!/usr/bin/env python3
string = input("Enter a string: ")
reverse = string[::-1]
if string == reverse:
	print (" It is a palindrome")
else:
	print ("It is not a palindrome")
	
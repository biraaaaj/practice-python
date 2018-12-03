#!/usr/bin/env python3
swaps = {'ba':'ab', 'cb':'bc', 'ca':'ac'}
string = input('Enter string with a, b, c')
sorted_string = ''.join(sorted(string))

while string != sorted_string:
	print(string)
	for keys in swaps:
		if(keys in string):
			string = string.replace(keys,swaps[keys],1)

print(string)

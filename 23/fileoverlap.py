#!/usr/bin/env python3
# happynumbers=[]
# primenumbers=[]
# with open('happy.txt','r')as file1:
# 	for num1 in file1:
# 		happynumbers.append(num1)

# with open('prime.txt','r') as file2:
# 	for num2 in file2:
# 		primenumbers.append(num2)

# for numbers in happynumbers:
# 	if numbers in primenumbers:
# 		print(numbers)

with open('happy.txt','r') as file1, open('prime.txt','r') as file2:
	common = []
	num1 = file1.read()
	num1 = num1.split('\n')
	num2 = file2.read()
	num2 = num2.split('\n')
	for number in num1:
		if number in num2:
			common.append(number)
	print(common)
	# print(num1)
	
	


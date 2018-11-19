#!/usr/bin/env python3
print ("Type one: rock, paper, scissors")

data = {'rock':1,'paper':2,'scissors':3}

while True:
	p1 = input("Player 1 does : ")
	if p1 == 'exit':
		exit()
	
	p2 = input("Player 2 does : ")
	if p2 == 'exit':
		exit()

	if p1 in data and p2 in data:
		v1 = data[p1]
		v2 = data[p2]

		s = abs(v1-v2)

		if s == 2:
			print(p1+" "+"wins")
		elif s == 1:
			print(p2+" "+"wins")
		elif s == 0:
			print("Draw")
	else:
		print("Does not exist.") 





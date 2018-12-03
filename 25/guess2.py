#!/usr/bin/env python3
import random
guess=int(input('Guess a number from 0 t0 100:'))
counter=0
if 0<guess<100:
	for i in range(0,10000):
		num = random.randint(0,100)
		counter+=1
		if num == guess:
			break
	print('It took me {} guesses to guess that number'.format(counter))
else:
	print('You picked a number out of range')
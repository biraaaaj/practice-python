#!/usr/bin/env python3
with open('prime.txt','w') as fileprime:
	for num in range(2,1000):
		k=1
		for i in range(2,int(pow(num,.5))):
			if num % i == 0:
				k=0
				break
		if k==1:
			fileprime.write('{}\n'.format(str(num)))	
fileprime.close()
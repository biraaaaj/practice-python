#!/usr/bin/env python3
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[]

print ("The numbers less than 5 are:")
for i in a:
	if i < 5 and i not in b:
		b.append(i)
print (b)
			


		
			

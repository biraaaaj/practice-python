#!/usr/bin/env python3
def get_split_squared(num):
	result = 0 
	for i in str(num):
		result += int(i)**2
		return (result)

allhappy = []
for num in range(1,1000):
	result = num
	while True:
		result = get_split_squared(result)
		if len(str(result))==1:
			if result==1:
				allhappy.append(int(num))
				break
			else:
				break
print(allhappy) 
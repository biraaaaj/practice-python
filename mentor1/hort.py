#!/usr/bin/env python3
a = ['H','T']
for i in range(0,2):
	for j in range(0,2):
		for k in range(0,2):
			for l in range(0,2):
				print(a[i]+a[j]+a[k]+a[l])
				if (a[i]==a[j]==a[k]=='H') or (a[j]==a[k]==a[l]=='H'):
					print('Three heads in a row')




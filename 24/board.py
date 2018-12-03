#!/usr/bin/env python3

n = int(input("n for n*n :"))
hori = ' ---'
vert ='|   '
n=n+1
for i in range(1,n):
	print(hori*(n-1))
	print(vert*n)
print(hori*(n-1))

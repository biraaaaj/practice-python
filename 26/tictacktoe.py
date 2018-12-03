#!/usr/bin/env python3
matrix = [[1,1,1],
	      [0,1,2],
	      [2,0,1]]

for row in matrix:
	if row[0] == row[1] == row[2] != 0:
		print('The winner is {}'.format(row[1]))
if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
	print('The winner is {}'.format(matrix[0][0]))
if matrix[0][0] == matrix[1][0] == matrix[2][0] != 0:
	print('The winner is {}'.format(matrix[0][0]))
if matrix[0][1] == matrix[1][1] == matrix[2][1] != 0:
	print('The winner is {}'.format(matrix[0][1]))
if matrix[0][2] == matrix[1][2] == matrix[2][2] != 0:
	print('The winner is {}'.format(matrix[0][2]))
if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
	print('The winner is {}'.format(matrix[0][2]))


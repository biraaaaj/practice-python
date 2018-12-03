#!/usr/bin/env python3

user1 = []
user2 = []
combination = [1, 3, 4, 5]
nums = [1, 2, 3, 5, 6, 7, 9, 10, 11]
numstodisplay = [1, 2, 3, 5, 6, 7, 9, 10, 11]
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
count = 0


def check(user, name):
    user.sort()
    for c in combination:
        for u in user:
            if (u + c) in user and (u + c + c) in user:
                display_data()
                print(name + ' wins')
                exit()


def display_data():
    iterator = 1
    for item in numstodisplay:
        if item in user1:
            print('O' + "\t", end='')
        elif item in user2:
            print('X' + "\t", end='')
        else:
            index = numstodisplay.index(item)
            print(alphas[index] + "\t", end='')
        if iterator % 3 == 0:
            print("\n", end='\n')
        iterator += 1



print(" This is your game board for tic tac toe")
print("Enter the position choosing from the placeholder alphabets")
display_data()
while len(nums) > 0:
    if count % 2 == 0:
        user = user1
        name = "User 1"
    else:
        user = user2
        name = "User 2"

    i = input(name + " enter a position alphabet :")
    i.lower()

    if i in alphas:
        i = alphas.index(i)
        i = numstodisplay[i]
    elif i=="exit":
    	exit()
    else:
        print("Enter a valid alphabet to play or type in exit to quit")
        continue

    if i in nums:
	    user.append(i)
	    nums.remove(i)
	    display_data()
    else:
   		print("Place already taken or wrong input.")
   		continue	

    if len(user) > 2:
        check(user, name)

    count += 1
display_data()
print("It's a Draw")




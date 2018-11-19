#!/usr/bin/env python3
def loses_against(choice):
	if choice=="paper":
		return "scissors"
	if choice=="rock":
		return "paper"
	if choice=="scissors":
		return "rock"

print ("Type one: rock, paper, scissors")
c1=input("enter your choice player 1: ")
c2=input("enter your choice player 2: ")
if c1 == c2:
	print("Draw")
elif c1==loses_against(c2):
	print("Player1 Wins")
else:
	print("Player2 wins")



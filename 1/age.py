#!/usr/bin/env python3
import datetime
name= input('enter your name')
age = int(input('Enter your age'))
now = datetime.datetime.now()
print("the year you will turn 100 years old is", now.year-age+100)


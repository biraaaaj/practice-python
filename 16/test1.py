#!/usr/bin/env python3
import string
import random
p = int(input("How many letters? :"))
a = string.ascii_letters
a += string.punctuation
print("Password is::  "+ "".join(random.sample(a, p)))

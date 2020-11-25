#! /usr/bin/python3
#Author @MAALP1225

import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbol = "!@#$^&*(),-="

all = lower + upper + number + symbol

while 1:
	password_length =int(input("How long should the password be? :- "))
	password_number =int(input("Number of password you want:- "))
	for x in range(0,password_number):
		password = ""
		for x in range(0,password_length):
			password_char = random.choice(all)
			password      = password + password_char
		print("Here is your password :- ",password)
	break

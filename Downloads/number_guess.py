import random
from random import randint

num = (randint(1, 100))
user_num = input("I am thinking of a number between 1 and 100.")
user_num += input("What do you think it is? ")
user_num = int(user_num)

while user_num != num:
	if user_num > num:
		print("Too high!")
		user_num = input("What do you think it is? ")
		user_num = int(user_num)
	elif user_num < num:
		print("Too low!")
		user_num = input("What do you think it is? ")
		user_num = int(user_num)

print("Congrats, you guessed the number.")
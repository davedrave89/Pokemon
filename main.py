from move import *
from assets import *
import random

#Declare classes
move = Move("Punch", 10, 20, 20)
pokemon = Pokemon("Charmander", 10, move)
user = User("Claire", 100, 1000)

#Start Game

while (user.healing > 0):
	result = raw_input("Please select move: \n1. Kick\n2. Punch\n")
	print(pokemon.Move.Name) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
	hit = random.randint(0,100)

	print(pokemon.GetName())
	print(user.GetName())
	print(user.Score())
	healing = user.Healing()
	print("You have been hit: ", hit)

	# Function that will calculate the score of player
	def calculate_score(healing, score):
		total = healing - score
		user.healing = total
		print("Your current health is: ", user.healing)

	calculate_score(healing, hit)

print("Game Over")
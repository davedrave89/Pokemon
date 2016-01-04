from move import *
from assets import *
import random

<<<<<<< HEAD

punch = Move("Punch", 10, 20, 20)
kick = Move("Kick", 10, 20, 20)

moves = [punch, kick]

pokemon = Pokemon("Claire", 10, moves)

result = raw_input("Please select move: \n1. Kick\n2. Punch\n")
result = int(result) # parse string result to int

result -= 1 #decrement result because the moves array is 0 based

print(pokemon.Moves[result].Name) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
print(random.randint(0,9))
=======
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
>>>>>>> origin/master

print("Game Over")




from move import *
from assets import *
import random

#Declare classes
punch = Move("Punch", 10, 20, 20)
kick = Move("Kick", 10, 20, 20)

moves = [punch, kick]

pokemon = Pokemon("Claire", 10, moves)

user = User("Claire", 100, 1000)

    # Function that will calculate the score of player
def calculate_score(healing, score):
	score = healing - score
	health = score
	print("Your current health is: ", user.health)
	
	return score, health

#Start Game

while (user.health > 0):
    result = raw_input("Please select move: \n1. Kick\n2. Punch\n")
    result = int(result) # parse string result to int
    result -= 1
    print(pokemon.name + " used " + pokemon.moves[result].name) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
    hit = random.randint(0,100)
        
    print calculate_score(user.health, hit)

    print(user.score)
    healing = user.health
    print "You have been hit: ", hit





print("Game Over")
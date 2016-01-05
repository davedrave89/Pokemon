from move import *
from assets import *
import random

#Declare classes
punch = Move("Punch", 10, 20, 20)
kick = Move("Kick", 10, 20, 20)

moves = [punch, kick]

pokemon = Pokemon("Claire", 10, moves)

user = User("Claire", 100, 1000)

#Start Game

while (user.healing > 0):
    result = raw_input("Please select move: \n1. Kick\n2. Punch\n")
    result = int(result) # parse string result to int
    result -= 1
    print(pokemon.Moves[result].Name) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
    hit = random.randint(0,100)

    print(pokemon.GetName())
    print(user.GetName())
    print(user.Score())
    healing = user.Healing()
    print "You have been hit: ", hit

    # Function that will calculate the score of player
def calculate_score(healing, score):
	total = healing - score
	user.healing = total
	print("Your current health is: ", user.healing)

calculate_score(healing, hit)

print("Game Over")
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

while (user.health > 0):

    print("Please select move:")

    #loop through moves that the pokemon can do
    #enumerate allows for the index to be included with the collection object
    for index, move in enumerate(pokemon.moves):
        print str(index + 1) + "." + move.name

    move_choice = raw_input()
    move_choice = int(move_choice) # parse string result to int
    move_choice -= 1

    print(pokemon.name + " used " + pokemon.moves[move_choice].name) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
    hit = random.randint(0,100)

    print(user.score)
    healing = user.health
    print "You have been hit: ", hit

    # Function that will calculate the score of player
def calculate_score(healing, score):
	total = healing - score
	user.healing = total
	print("Your current health is: ", user.healing)

calculate_score(healing, hit)

print("Game Over")
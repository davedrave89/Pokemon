



from move import *
from assets import *
import random

#Declare classes
punch = Move("Punch", 10, [18,25], 20)
kick = Move("Kick", 10, [10,35], 20)

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
<<<<<<< HEAD
    result = raw_input("Please select move: \n1. Kick\n2. Punch\n")
    result = int(result) # parse string result to int
    result -= 1
    print(pokemon.name + " used " + pokemon.moves[result].name) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
    hit = random.randint(0,100)
        
    print calculate_score(user.health, hit)

    print(user.score)
    healing = user.health
    print "You have been hit: ", hit
=======

    print("Please select move:")

    #loop through moves that the pokemon can do
    #enumerate allows for the index to be included with the collection object
    for index, move in enumerate(pokemon.moves):
        print str(index + 1) + "." + move.name

    #get users choice
    move_choice = raw_input()
    move_choice = int(move_choice) # parse string result to int
    move_choice -= 1

    #reuse move_choice, now to store the move itself (neater than referring to it WITHIN pokemon.moves)
    move_choice = pokemon.moves[move_choice]


    #damage dealt will be a random amount within the range specified by the move
    damage = random.randint(move_choice.range[0],move_choice.range[1])

    print(pokemon.name + " used " + move_choice.name + ", causing " + str(damage) + " damage.") #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object

    user.health = user.health - damage

    print(user.name + "'s health is now " + str(user.health))
>>>>>>> 9e527dc019093241ab9ad50ff616f8a57ae3a37e





print("Game Over")

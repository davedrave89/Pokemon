from move import *
from assets import *
import random

#Declare classes
punch = Move("Punch", 10, [18,25], 20)
kick = Move("Kick", 10, [10,35], 20)

moves = [punch, kick]

ComputerPlayer = Player("ComputerPlayer", 100, 1000, Pokemon("Charmander", 10, moves))

clairePlayer = Player("ClairePlayer", 100, 1000, Pokemon("Squirtle", 10, moves))

    # Function that will calculate the score of player
def calculate_score(healing, score):
	score = healing - score
	health = score
	print("Your current health is: ", clairePlayer.health)
	
	return score, health

#Start Game

while (Player.health > 0):

    print("Please select move:")

    #loop through moves that the pokemon can do
    #enumerate allows for the index to be included with the collection object
    for index, move in enumerate(clairePlayer.pokemon.moves):
        print str(index + 1) + "." + move.name

    #get users choice
    move_choice = raw_input()
    move_choice = int(move_choice) # parse string result to int
    move_choice -= 1

    #reuse move_choice, now to store the move itself (neater than referring to it WITHIN pokemon.moves)
    move_choice = clairePlayer.pokemon.moves[move_choice]


    #damage dealt will be a random amount within the range specified by the move
    damage = random.randint(move_choice.range[0],move_choice.range[1])

    print(clairePlayer.pokemon.name + " used " + move_choice.name + ", causing " + str(damage) + " damage.\n") #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object

    clairePlayer.health = clairePlayer.health - damage

    print(clairePlayer.name + "'s health is now " + str(clairePlayer.health)+ "\n")

print("Game Over")

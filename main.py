from move import *
from assets import *
import random

#Declare classes
punch = Move("Punch", 10, 20, 20)
kick = Move("Kick", 10, 20, 20)

moves = ['Tackle', 'Tail whip']

pokemon = Pokemon("Squirtle", 1000, moves)

# computer_player = Computer_player("Claire", 100, 1000, "Squirtle", 1000, moves)

user = User("Claire", 100, 1000)
computer = User("Computer", 100, 1000)

def hit():
    return random.randint(0,100)

    # Function that will calculate the score of player
def calculate_score(healing, hit, score):
	computer.health = pokemon.health - hit
	user.score += 20
	print(pokemon.name +  " health is: ", pokemon.health)
	
	return hit, user.health, user.score


def computer_hit():
    computer_move = random.randint(0, len(moves)-1)
    print computer.name + " used " + moves[computer_move]
    computer.score += 20
    

#Start Game
# while (user.health > 0):
#     print "***********************************Next Move ******************************"
#     result = raw_input("Please select move: \n1. " + pokemon.moves[0] + "\n2. " + pokemon.moves[1] + "\n")
#     result = int(result) # parse string result to int
#     result -= 1
#     print(pokemon.name + " used " + pokemon.moves[result]) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
#     hit = hit()
        
#     print calculate_score(user.health, hit, user.score)


#     print(user.score)
#     healing = user.health
#     print "You have been hit: ", hit

# print("Game Over")

computer_hit()

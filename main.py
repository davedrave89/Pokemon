from move import *
from assets import *
import random

#Declare classes
punch = Move("Punch", 10, [18,25], 20)
kick = Move("Kick", 10, [10,35], 20)

moves = [punch, kick]

ComputerPlayer = Player("ComputerPlayer", 100, 1000, Pokemon("Charmander", 100, moves))

ClairePlayer = Player("ClairePlayer", 100, 1000, Pokemon("Squirtle", 100, moves))

# Function that will calculate the score of player
def calculate_score(damage, player_health, pokemon_health, current_player):
	print("Damage: ", damage)
	print("Player health", player_health)
	print("Pokemon health", pokemon_health)
	
	#printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
	print(current_player.pokemon.name + " used " + move_choice.name + ", causing " + str(damage) + " damage.\n") 
	current_player.pokemon.health = current_player.pokemon.health - damage
	
	return current_player.pokemon.health
	
#Start Game
Game_count = 1
while (ClairePlayer.pokemon.health > 0):
    #Player to alternate between goes
    if Game_count % 2 == 0:
        current_player = ComputerPlayer
        print current_player.name
    else:
        current_player = ClairePlayer
        print ("working")
        print current_player.name
    print("Please select move:")

    #loop through moves that the pokemon can do
    #enumerate allows for the index to be included with the collection object
    for index, move in enumerate(current_player.pokemon.moves):
        print str(index + 1) + "." + move.name

    #get users choice
    move_choice = raw_input()
    move_choice = int(move_choice) # parse string result to int
    move_choice -= 1

    #reuse move_choice, now to store the move itself (neater than referring to it WITHIN pokemon.moves)
    move_choice = current_player.pokemon.moves[move_choice]
    
    #damage dealt will be a random amount within the range specified by the move
    damage = random.randint(move_choice.range[0],move_choice.range[1])
    
    #call calculate score fucntion
    calculate_score(damage, current_player.health, current_player.pokemon.health, current_player)

    print(current_player.pokemon.name + "'s health is now " + str(current_player.pokemon.health)+ "\n")
    
    #Increment Game count per player turn
    Game_count += 1

print("Game Over")

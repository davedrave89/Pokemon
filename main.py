from move import *
import random


punch = Move("Punch", 10, 20, 20)
kick = Move("Kick", 10, 20, 20)

moves = [punch, kick]

pokemon = Pokemon("Claire", 10, moves)

result = raw_input("Please select move: \n1. Kick\n2. Punch\n")
result = int(result) # parse string result to int

result -= 1 #decrement result because the moves array is 0 based

print(pokemon.Moves[result].Name) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
print(random.randint(0,9))

print(pokemon.GetName())
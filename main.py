from move import *
import random


move = Move("Punch", 10, 20, 20)
pokemon = Pokemon("Claire", 10, move)

result = raw_input("Please select move: \n1. Kick\n2. Punch\n")
print(pokemon.Move.Name) #printing name within pokemon to show that an instantiation of the Move class has been passed into the pokemon object
print(random.randint(0,9))

print(pokemon.GetName())
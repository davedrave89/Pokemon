from moves import *
import random

pokemon = Pokemon("Claire", 10, "Punch")
move = Move("Punch", 10, 20, 20)

result = raw_input("Please select move: \n1. Kick\n2. Punch\n")
print(random.randint(0,9))

print(pokemon.GetName())
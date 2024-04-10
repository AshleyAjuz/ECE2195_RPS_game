import numpy as np
import random
from random import randint

def RPS(fingerUp):

    if fingerUp == 0:
        userInput = 1
    elif fingerUp == 5:
        userInput = 2
    elif fingerUp == 2:
        userInput = 3
    else:
        print(fingerUp)
        raise Exception("Invalid Input")

    # 1 = rock, 2 = paper, 3=scissors
    cpu_choice =  random.randint(1, 3)

    #Hashmap for mapping
    rps_map = {1: "rock", 2: "paper", 3: "scissors"}

    print(f" User choice: {rps_map[userInput]}. CPU choice: {rps_map[cpu_choice]}")
    if userInput == cpu_choice:
        print("Tie!")
    elif userInput == 1:
        if cpu_choice == 2:
            print("CPU wins")
        else:
            print("You Win!")
    elif userInput == 2:
        if cpu_choice == 1:
            print("You Win!")
        else:
            print("CPU wins")
    elif userInput == 3:
        if cpu_choice == 1:
            print("CPU Wins")
        else:
            print("You win!")
     

import random       # Importing Random Module for random number generation
import time         # Importing the Time Module to handle time-related tasks

def dice():

 player = random.randint(1,6)  # Getting a random number between 1 and 6 rolled by the player
 print("You rolled " + str(player))  # Printing the random number rolled by player

 eb = random.randint(1, 6)

 time.sleep(3)                   # Calling the sleep function to suspend execution of the current thread for 3 seconds

 print("The electronic brain has rolled a " + str(eb))  # Getting a random number between 1 and 6 rolled by the machine

 if player > eb:     # If statement that uses the  <, >, or == operators to compare results


    print("You win")
 elif player == eb:
    print("Tie game")
 else:
    print("You loose")
 print("Do you want to quit or continue ? Y/N ")  # Game prompts player with a boolean dialog message: Y to quit or N to
                                                  # continue
 cont = input()         # Taking response from player
 if cont == "Y" or cont == "y":
        exit()         # Exiting game if player responds with a Y
 elif cont == "N" or cont == "n":   # Continuing  game if player responds with a N
        pass
 else:             # Game does not accept any response other than boolean !
        print("I did not understand that. Do you want to play again ?")


while True:       # While loop prompting user to roll a die, then calls the dice function to calculate the result


    print("Press enter to roll the die.")
    roll = input()
    dice()


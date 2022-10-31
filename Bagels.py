#Bagels, a deductive logic game.
#Inspired by Al Sweigart, al@inventwithpython.com

#In Bagels, a deductive logic game, you must guess a secret three digit number
#based on clues. The game offers one of the following hints in response to your
#guess.

#'Pico' when your guess has a correct digit in the wrong place,
#'Fermi' when your guess has a correct digit in the correct place.
#'Bagels' if your guess has no correct digits.

#You have 10 tries to guess the secret number.

#First we have to create the secret three digit number randomizer
import random

SecretNumber = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

#This is the start of the main program, a commit example

while True:
    wrong_counter = 0
    print('Please insert a three digit number')
    PlayerNumber = str(input())

    if PlayerNumber == SecretNumber:
        print('You got it!')
        Break

    for i in range(len(PlayerNumber)):
            if PlayerNumber[i] == SecretNumber[i]:
                print('Fermi', end=' ')
            elif PlayerNumber[i] in SecretNumber:
                print('Pico', end=' ')
            else:
                wrong_counter = wrong_counter + 1
    
    if wrong_counter == 3:
        print('Bagels')
    else:
        continue








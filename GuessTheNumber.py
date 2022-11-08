#Guess the Number, inspired by Al Sweigart al@inventwithpython.com

import random, sys

#Parameters: lower number, higher number, guesses
lower = 1
higher = 100
guesses = 10

#Number selector at the beginning of the match

SecretNumber = random.randint(lower, higher)

#Main game loop, if player guesses the chosen number, exits the loop

print('Guess the Number. Inspired by Al Sweigart al@inventwithpython.com \n')

print('I am thinking of a number between %d and %d' % (lower, higher))

while guesses > 0:
    print('You have %d guesses left. Take a guess.' % guesses)
    PlayerGuess = float(input())
    if PlayerGuess.is_integer() == True:
        if PlayerGuess > SecretNumber:
            print('Your guess is too high.')
            guesses -= 1
        elif PlayerGuess < SecretNumber:
            print('Your guess is too low.')
            guesses -= 1
        else:
            print('Yay! You guessed my number!')
            sys.exit()
    else:
        print('That is not an integer, try again.')
print('You ran out of guesses, the secret number was %d' % SecretNumber)
#Hangman, inspired by Al Sweigart al@inventwithpython.com

#Definition of modules

import random

#TO DO: Define the categories of the game,
#This means then that each category contains a certain number of words in it to guess

#Definition of Categories and words within categories
Animals = ['Cow', 'Pig', 'Chicken', 'Otter']
Fruits = ['Apple', 'Pineapple', 'Banana', 'Coconut']

MasterList = [Animals, Fruits]

#TO DO: The Hangman_Pics must be stored somewhere, and they must be displayed
#to the user sequentially everytime the user misses the letter.
#By the standard rules of hangman, the user has 7 tries before losing the game. 

def HangmenInitializer():
    H1 = '''
 +--+
 |  |
    |
    |
    |
    | 
=====
'''

    H2 = '''
 +--+
 |  |   
 O  |    
    |      
    |     
    |   
=====   
'''

    H3 = '''
 +--+
 |  |
 O  |
 |  |
    |
    |
===== 
'''

    H4 = '''
 +--+
 |  |
 O  |
/|  |
    |
    |
===== 
'''

    H5 = '''
 +--+
 |  |
 O  |
/|\\ |
    |
    |
===== 
'''

    H6 = '''
 +--+
 |  |
 O  |
/|\\ |
/   |
    |
===== 
'''

    H7 = '''
 +--+
 |  |
 O  |
/|\\ |
/ \\ |
    |
===== 
'''

    Hangmen = [H1, H2, H3, H4, H5, H6, H7]
    return Hangmen


#TO DO: Define a function that randomly chooses one of the categories 
#and then randomly chooses a word from said category

#First we can use random.choice() to have a random category selected from a specific list
#And then we can use another random.choice() to select a random word from the selected category
#This chosen word is important because it is what guides the current game round 

#We make ChosenCategory a global variable so that it can be called into the print function

def ChooseGuessWord():
    global ChosenCategory
    ChosenCategory = random.choice(MasterList)
    ChosenWord = random.choice(ChosenCategory)
    return ChosenWord


#TO DO: Create a function that displays a number of underscores (_ _ _) depending on the chosen guess word
#This means this part of the program can count the number of letters in the selected word
#And then it displays an appropiate number of underscores.

#Then it stores the number of underscores into a list
#One way to do this is to store '_ ' into a variable, and then
#multiply that variable by the len(chosenWord) and printing it to output
#This list is very important, since it contains the word that will mutate throughout the game sequence 

def GameWordCreator(Word):
    UnderScoredWord = list('_' * len(Word))
    return UnderScoredWord

#TO DO: Create a function that can check if a word is "complete" or not.
#One way to do this is check if there are '_' in the UnderScoredWord, or any list like variable really
#Then we can insert this function into a while loop, so while CheckCompletion(Word) is not True, continue
#running the program

def CheckCompletion(ListWord):
    if '_' in ListWord:
        return True


#TO DO: Create a system that takes in a letter chosen by the user, and then looks for it
#in the GuessWord, if it finds it in the guess word, then it displays just that letter
#back to the user.

#ChosenLetter = str(input('Please input a letter\n').upper())

#if ChosenLetter in GameWord:
    #Insert function here that completes word

#After searching in the GuessWord for any letter that matches the ChosenLetter, 
#We have to take the ChosenLetter and complete the respective spots in the UnderScoredWord


def WordCompleter(Guessword, ChosenLetter):
    ListWord = list(Guessword)                   #transform the GuessWord into a list,
    for i in range(len(ListWord)):          #important! range(len(Word)) converts the thing into integers which can be iterated upon and used as indexes
        if ChosenLetter == ListWord[i]:     #This runs through every letter of the Guessword, and compares it with the ChosenLetter
            GameWord[i] = ChosenLetter   #For every match of the chosenLetter and the letter in the GuessWord, this then edits or mutates the UnderScoredWord

#Main game loop:

Hangmen = HangmenInitializer()
GuessWord = ChooseGuessWord()
GameWord = GameWordCreator(GuessWord)

#Initialize Tries and MissedLetters list
Tries = 0
MissedLetters = []

print(Hangmen[Tries])
print('The category is: %s' % ChosenCategory)
print('Missed letters: No missed letters yet.')
print(GameWord)

#Initialize the main gain loop 
while Tries < 7:
    while CheckCompletion(GameWord) == True:
        PlayerLetter = str(input('Guess a letter.\n').upper())
        if PlayerLetter in GameWord:
            WordCompleter(GuessWord,PlayerLetter) #WordCompleter edits a global variable
            print(Hangmen[Tries])
            print('The category is: %s' % ChosenCategory)
            if MissedLetters == []:
                print('Missed letters: No missed letters yet.')
            else:
                print('Missed letters: ' + ' '.join(MissedLetters))
            print(GameWord)
        else:
            Tries += 1
            MissedLetters.append(PlayerLetter)
            print(Hangmen[Tries])
            print('The category is: %s' % ChosenCategory)
            print('Missed letters: ' + ' '.join(MissedLetters))
            print(GameWord)
    print('Congratulations you won!')
print('Sorry you lost, try again!')

            













#in the else part of the program, we have to be able to print out the stages
#of the hangman drawing in sequence, which means there must be a sort of counter
#that is able to count the number of wrong tries you have
#and with that counter then print the corresponding hangman drawing 


#There must also be a way to store the new UnderScoredWord so that,
#the next time player chooses another letter, it doesnt delete
#the old chosen letter

#The game must also recognize when the letter is complete

#When the ChosenLetter check fails we have to 
#Print out the HangmanList[TotalWrongTries]


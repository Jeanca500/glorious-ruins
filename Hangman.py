#Hangman, inspired by Al Sweigart al@inventwithpython.com

#Definition of modules
import random, sys

#TO DO: Define the categories and words of the game in a dictionary. 
#Each category contains a certain number of words in it to guess by the player.

MasterDict = {
    'Animals': ['Cow', 'Pig', 'Chicken', 'Otter'],
    'Fruits' : ['Apple', 'Pineapple', 'Banana', 'Coconut'],
    'Cars' : ['BMW', 'Kia', 'Audi', 'Volkswagen'],
    'Video Games' : ['Zelda', 'Mario', 'Halo', 'Metroid', 'Uncharted']
}

#TO DO: A function that stores the Hangman_Pics 
#The sequential display of the hangmen pics is managed in the main game loop
#By the standard rules of hangman, the user has 7 tries before losing the game, so there
#are seven ASCII pictures.  The function returns a list with the stored Hangmen in each index.

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
# and then randomly chooses a word from the selected category
# The function requires a dictionary as input and returns both the 
# chosen category and chosen word in a dictionary.

def ChooseCatAndWord(dict):
    ChosenItems = random.choice(list(dict.items()))
    ChosenCategory = ChosenItems[0] 
    ChosenWord = random.choice(ChosenItems[1])
    return {'Chosen Category' : ChosenCategory,
            'Chosen Word':    ChosenWord}

#TO DO: Create a function that creates a "Gameword" element represented initially by 
# a number of underscores (_ _ _) whose number depend on the chosen guess word.
# The function receives as input the chosen guessword and returns 
# a list of underscores ['_','_','_'] that correspond to the number of letters 
# in the chosen guess word.
# This game word is then the list that changes throughout gameplay
 
def GameWordCreator(Guessword):
    UnderscoreWord = list('_' * len(Guessword))
    return UnderscoreWord

#TO DO: Create a function that can check if a word is "complete" or not.
#One way to do this is check if there are '_' in the GameWord, or any list like variable really
#The function returns True if it finds underscores in the gameword. 

def CheckUnderscores(Gameword):
    if '_' in Gameword:
        return True

#TO DO: Create a function that takes in a letter chosen by the user, and then
#  looks for it in the GuessWord, if it finds it in the guess word, 
#  then it completes the letter in the GameWord list.

#The word completer function takes in the Chosen GuessWord , and the PlayerLetter.
#It runs through the guessword, checking letter by letter and mutates the GameWord list
#depending on the player letter. 

def WordCompleter(Guessword, Letter):
    UpperGuessWord = Guessword.upper()          #Transforms the guessword into all Caps
    ListGuessWord = list(UpperGuessWord)     #transfroms the guessword into a list
    for i in range(len(Guessword)):          #range(len(Word)) converts the thing into integers which can be iterated upon and used as indexes
        if Letter == ListGuessWord[i]:     #This runs through every letter of the Guessword, and compares it with the ChosenLetter
            GameWord[i] = Letter               #For every match of the chosenLetter and the letter in the GuessWord, this then edits or mutates the UnderScoredWord


#Main game initialization, the hangmen, category, and word are chosen. GameWord is created.

Hangmen = HangmenInitializer()
CatAndWord = ChooseCatAndWord(MasterDict)
Category = CatAndWord['Chosen Category']
GuessWord = CatAndWord['Chosen Word']
GameWord = GameWordCreator(GuessWord)

#Initialize Tries and MissedLetters list
Tries = 0
MissedLetters = []

#The following sequence prints out the initial setup, the hangman drawing,
#the chosen category, and the Gameword (which will be a number of underscores)

print('Hangman, inspired by Al Sweigart al@inventwithpython.com \n')
print(Hangmen[Tries])
print('The category is: %s' % Category)
print('Missed letters: No missed letters yet.')
print(' '.join(GameWord))

#Initialize the main gain loop 
while Tries < 7:
    if CheckUnderscores(GameWord) == True:
        PlayerLetter = str(input('Guess a letter.\n')).upper()   #The PlayerLetter is always in caps

        if PlayerLetter in GuessWord.upper():     #Checks if the player letter is in the upper cased guess word
            WordCompleter(GuessWord,PlayerLetter) #Word Completer mutates the GameWord list with the PlayerLetter
            print(Hangmen[Tries])
            print('The category is: %s' % Category)
            if MissedLetters == []:
                print('Missed letters: No missed letters yet.')
            else:
                print('Missed letters: ' + ' '.join(MissedLetters))
            print(' '.join(GameWord))
        else:
            MissedLetters.append(PlayerLetter)
            print(Hangmen[Tries])
            print('The category is: %s' % Category)
            print('Missed letters: ' + ' '.join(MissedLetters))
            print(' '.join(GameWord))
            Tries += 1
    else:
        print('Congratulations you won! The secret word is %s' % GuessWord.upper())
        sys.exit()
print('Sorry you lost, try again! The secret word was %s' % GuessWord.upper())

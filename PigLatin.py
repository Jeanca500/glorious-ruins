#Pig Latin
#Inspired by Al Sweigart, al@inventwithpython.com

#If the word starts with any consonant
#take the value of the first consonant and append it
#to the end of the individual word and add 'ay'

#How to recognize the first letter of a string
#Define a vowel list which will be used to discrimatethe first letter of each word

vowels = ['a','e','i','o','u']

#We would also have to include a string composed of many words
#into a list of words, so that the main program
#iterates over a list of words, and then applies the
#function to each of the elements of the list of words.

#We can define a function that takes the string, and then
#checks what is the first letter of the word
#This function then checks word[0] to see if its a vowel or a consonant,
#and depending on what it finds, it transforms the word

def Translate(word):
    if word[0] not in vowels:
        newWord = word[1:] + word[0] + 'ay'
        return newWord
    elif word[0] in vowels:
        newWord = word + 'yay'
        return newWord

#Start of the program, here it asks the user to input any phrase they want translated. 

message = input('Please input the phrase you want translated into PigLatin')

#We also have to define a way to take a string of words and then store each individual word
#(anything separated by a space) into a list
#For this we will use the split() method.

splitMessage = message.split(' ')
PigLatinList = []

for word in splitMessage:
    PigLatinList.append(Translate(word))
    
#Join the PigLatinMessage list into a string using the .join() method

PigLatinMessage = ' '.join(PigLatinList)

print(PigLatinMessage)



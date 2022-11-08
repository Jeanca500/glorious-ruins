#Powerball Lottery, inspired by Al Sweigart al@inventwithpython.com

#First we would have to create a random number generator
import random

#Define a Powerball Randomizer function
def PowerballRandomize():
    a = random.randint(1,69)
    b = random.randint(1,69)
    c = random.randint(1,69)
    d = random.randint(1,69)
    e = random.randint(1,69)
    f = random.randint(1,26)

    Powerball = [a,b,c,d,e,f] #Insert the six generated numbers into a list
    return Powerball

#Define a function that displays the beginning message of the PowerBall Program

def ProgramStart():
    print("""
Powerball Lottery, inspired by Al Sweigart al@inventwithpython.com

Each Powerball lottery ticket costs $2. The jackpot for this game is $1.586 billion! 
It doesn't matter what the jackpot is, though, because the odds are 1 in 292,201,338, 
so you won't win. 
            
This simulation gives you the thrill of playing without wasting money.""")

#Ask the user to input a string of five numbers 

ProgramStart()

#This section of code defines a function that creates a list for the userChoice, and then inserts the numbers that the user has input into the UserChoice list

FirstFiveNumbers = input('''
Please enter 5 different numbers from 1 to 69, with spaces between each number. 
(For example 5 17 23 42 50)\n''')
PowerBallNumber = input('Enter the powerball number from 1 to 26\n')

UserChoice = []
PowerballFirst = FirstFiveNumbers.split(' ')

for number in PowerballFirst:
    UserChoice.append(int(number))

UserChoice.append(int(PowerBallNumber))

#This section asks the user how many times they want to play 

PlayTimes = int(input('How many times do you want to play? (Max: 1,000,000)\n'))
CostToPlay = PlayTimes * 2
print("It costs $%d to play %d, but don't worry. I'm sure you'll win it all back" % (CostToPlay, PlayTimes))

input('Press Enter to start...')


#Have to deploy a part of the script that runs the PowerBallRandomize() function 1,000,000 times 

for iteration in range(PlayTimes):
    Powerball = PowerballRandomize()
    if UserChoice == Powerball:
        print('The winning numbers are ' + str(Powerball[0]) + ' ' + str(Powerball[1]) + ' ' + str(Powerball[2]) + ' ' + str(Powerball[3]) + ' ' + str(Powerball[4]) + ' and ' + str(Powerball[5]) + '  You win!')
        break
    else:
        print('The winning numbers are ' + str(Powerball[0]) + ' ' + str(Powerball[1]) + ' ' + str(Powerball[2]) + ' ' + str(Powerball[3]) + ' ' + str(Powerball[4]) + ' and ' + str(Powerball[5]) + '  You lost!')

print('You have wasted $%d' % (CostToPlay))
print('Thanks for playing!')
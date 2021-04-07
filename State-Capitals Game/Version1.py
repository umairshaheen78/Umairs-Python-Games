#Version 1 of Python Game:

import time #Importing time for how long you have to wait for Python.

#Welcoming the user to the game
print ("Welcome to Version 1 of Umair's Python State Capital Quiz!")
time.sleep(1)

#The states used in the game/quiz
states = {'Colorado':'Denver', 'Ohio':'Columbus',
'Florida':'Tallahassee','Arizona':'Phoenix', 'Mississippi':'Jackson', 'California':'Sacramento', 'New York': 'New York City', 'Idaho': 'Boise', 'Wisconsin': 'Madison'}

#Setting up the values/variables for the scores
correct = 0
incorrect = 0

#For loop for the random states picked
for state in states:
    capital = states[state]
    print("What is the capital of:", state)
    answer = input("Please type your answer: ")
    if (answer == capital):
        print("Correct!")
        correct += 1
    else:
        print("Sorry the correct answer was", capital)
        incorrect += 1

#Final score user gets for the game
print("You got",correct,"correct and",incorrect,"incorrect answers" )

#Asking user if they would like to play again
PlayAgain = str(input("Do you want to play again? [y/n]"))
if (PlayAgain == "y"):
    PlayAgain = True

if (PlayAgain == "n"):
    PlayAgain = False
import time

print ("Welcome to Version 2 of Umair's Python State Capital Quiz!")
time.sleep(1)
print ("Loading Python quiz system...")
time.sleep(1)

states = {'Mississippi':'Jackson', 'California':'Sacramento', 'New York': 'New York City', 'Idaho': 'Boise', 'Wisconsin': 'Madison'}

print("Question 1: - What is the capital of Colorado?\na - Colorado\nb - Denver\nc - Aspen")

answer = input().lower()

if answer == "a":
    print("Don't be silly! How can the capital of Colorado be Colorado??")
elif answer == "b":
    print("Correct!!")
elif answer == "c":
    print("Aspen... uh, I am pretty sure that is not correct. ")
else:
    print("You didn't choose a, b, or c. Let's move on to the next question.")

print("Question 2: - What is the capital of Ohio?\na - Columbus\nb - Indiana\nc - Squaw Valley")

answer = input().lower()

if answer == "a":
    print("Correct!!")
elif answer == "b":
    print("That's incorrect. Indiana is literally a seperate state.")
elif answer == "c":
    print("Squaw Valley... I recognize that place... It's near South Lake Tahoe, which is in California, so I don't understood why you put that.")
else:
    print("You didn't choose a, b, or c. Let's move on to the next question.")

print("Question 3: - What is the capital of Florida?\na - Tallahase\nb - Tallahease\nc - Tallahassee")

answer = input().lower()

if answer == "a":
    print("That's incorrect. Did you notice that I spelled Tallahassee wrong??")
elif answer == "b":
    print("That's incorrect. Did you notice that I spelled Tallahassee wrong??")
elif answer == "c":
    print("Correct! Thankfully, you didn't fall for putting the 2 other choices, which were Tallahassee, but spelled wrong!")
else:
    print("You didn't choose a, b, or c. Let's move on to the next question.")

print("Question 4: - What is the capital of Arizona?\na - Dragon Fly\nb - Pheenix\nc - Phoenix")

answer = input().lower()

if answer == "a":
    print("That's incorrect. Did you know that Dragon Fly is a character from a movie?")
elif answer == "b":
    print("That's incorrect. Did you notice that I spelled Phoenix wrong?? Pheenix is like how you would pronounce Phoenix, so... I don't understand why you put a weird answer.")
elif answer == "c":
    print("Correct! Thankfully, you didn't fall for putting the 2 other choices, which one was a movie character and the other was Pheenix!")
else:
    print("You didn't choose a, b, or c. Let's move on to the next question.")

print("Question 5: - What is the capital of California?\na - Hi\nb - Sacramento\nc - Sacrameto")

answer = input().lower()

if answer == "a":
    print("That's incorrect. Why did you pick Hi as your answer?")
elif answer == "b":
    print("Correct! Thankfully, you didn't fall for putting the 2 other choices, which one was Hi and the other was Sacramento, but spelled wrong!!")
elif answer == "c":
    print("That's incorrect. Did you notice that I spelled Sacramento wrong?? I just took out some letters, don't fall for these dumb mistakes.")
else:
    print("You didn't choose a, b, or c. Let's move on to the next question.")

print ("Now... I need to test your typing skills. You will be typing the capital of each state, as you see it. Check out the example below...\nWhat is the capital of Colorado?\nPlease type your answer: Denver\nPython Input: Correct!\n")

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

print("\nFor the typing skills part of this game, You got",correct,"correct and",incorrect,"incorrect answer(s)")
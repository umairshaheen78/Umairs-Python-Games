import random
import time

print ("Welcome to the Python Number Guessing Game!")
time.sleep(1)
print ("Loading Python math system...\n")
time.sleep(1)

name = input('What is your name?\n')
print('Hi, %s.\n' % name)

number = random.randrange(1, 10)
guess = int(input("Please enter your guess:"))
 
if guess == number:
    print("You got the number! Great Job!")
elif guess < number:
    print("Your guess is too low.")
else:
    print("Your guess is too high.")
import time

print ("Welcome to The General Knowledge and Thinking Quiz!")
time.sleep(1)
print ("Loading Python quiz system...")
time.sleep(1)

name = input('What is your name?\n')
print('Hi, %s.' % name)

score = 0

print("\nQuestion 1:")
time.sleep(1)
print("What is the capital of Australia?\na) Sydney\nb) Canberra\nc) Yerevan\n")
answer = input().lower()
if answer == "b":
        print("Correct!\n")
        score += 1
else:
    print ("Incorrect!\n")

print("\nQuestion 2:")
time.sleep(1)
print("What is the capital of Denmark?\na) Copenhagen\nb) Australia\nc) Gothenburg\n")
answer = input().lower()
if answer == "a":
        print("Correct!\n")
        score += 1
else:
    print ("Incorrect!\n")

print("\nQuestion 3:")
time.sleep(1)
print("What is 13 x 19?\na) 250\nb) 291\nc) 247\n")
answer = input().lower()
if answer == "c":
        print("Correct! Great job calculating!\n")
        score += 1
else:
    print ("Incorrect!\n")

print("\nQuestion 4:")
time.sleep(1)
print("Name a city in Jordan\na) Amman\nb) Oman\nc) Jordania\n")
answer = input().lower()
if answer == "a":
        print("Correct! Amman is actually the capital of Jordan, so good job!\n")
        score += 1
else:
    print ("Incorrect!\n")

print("\nQuestion 5:")
time.sleep(1)
print("Which NBA player is starring in the new movie, Space Jam 2?\na) Stephen Curry\nb) Lebron James\nc) Zach Lavine\n")
answer = input().lower()
if answer == "b":
        print("Correct! Did you know that Lebron James is actually the main character of the movie??\n")
        score += 1
else:
    print ("Incorrect!\n")

print("\nThis is the end of the quiz! Here are your results:\n")
time.sleep(1)
print("You got",(score),"/ 5 correct answers!\nGreat Job!")
def factorial(n):
    if n == 0:
        return 1 and print ("0 doesn't really have a factorial, so that's why it's marked to be 1. The answer also might be marked as None.")
    else:
        return n * factorial(n-1)
print ("Welcome to the Factorial Calculator!")
print("Loading Factorial Calculator Python system...")
n=int(input("Input a number, so I can find the factorial: "))
print("The answer is",factorial(n))
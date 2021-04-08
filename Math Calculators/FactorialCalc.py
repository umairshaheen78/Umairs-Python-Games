def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print ("Welcome to the Factorial Calculator!")
print("Loading Factorial Calculator Python system...")
n=int(input("Input a number, so I can find the factorial: "))
print("The answer is",factorial(n))
import time

# Calculate Miles Per Gallon
print("This program calculates mpg.")
time.sleep(1)
print("Loading MPG Calculator Python system...")
time.sleep(1)
 
# Get miles driven from the user
miles_driven = input("Enter miles driven: ")
# Convert text entered to a floating point number
miles_driven = float(miles_driven)
 
# Get gallons used from the user
gallons_used = input("Enter gallons used:")
# Convert text entered to a floating point number
gallons_used = float(gallons_used)
 
# Calculate and print the answer
mpg = miles_driven / gallons_used
print("Miles per gallon:", mpg)
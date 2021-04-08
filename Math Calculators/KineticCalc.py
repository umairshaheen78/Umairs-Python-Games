print ("Welcome to the Kinetic Energy Calculator!\nThis program calculates the kinetic energy of a moving object.")
print("Loading Kinetic Energy Calculator Python system...")
m_string = input("Enter the object's mass in kilograms: ")
m = float(m_string)
v_string = input("Enter the object's speed in meters per second: ")
v = float(v_string)
e = 0.5 * m * v * v
print("The object has " + str(e) + " joules of energy.")
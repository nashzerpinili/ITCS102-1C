from activity23_1 import *

print("WELCOME TO MY COMPILER PROGRAM")
name = input("Hi Visitor, what is your name --> ")

print(f"Hi {name}, select from the options below")
print("A - Greet Name\nB - Greet with Name, Age, Location\nC - Triangle\nE - Exit")

isCont = True

while isCont == True:
    choice = input("Select from A - E --> ").lower()

    if choice == 'a':
        name = input("Please state your name --> ")
        GreetWithName(name)
        continue

    elif choice == 'b':
        number = eval(input("Input any number --> "))
        print(f"Factorial of {number} is {Factorial(number)}")
        continue

    elif choice == 'c':
        GetTriangle()
        continue

    elif choice == 'e':
        print("Program terminated...")
        break

    else:
        print("Invalid choice")
        continue

number = eval(input("Type your number here --> "))
factorial = 1
for A in range(number,0,-1):
    factorial *= A
print("The factorial of ",number, "is" ,factorial)

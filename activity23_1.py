def GreetWithName(name):
    print(f"Maayong Gabii cuh {name}")

def GreetPerson(name, loc, age):
    print(f"Hi {name} from {loc}, {age} yr/s old")

def FunctionWithReturn(number):
    print(f"This function calculates the summation from 1 to {number}")
    sum = 0
    for x in range(1, number + 1, 1):
        sum += x
    return sum

def FactorialWithReturn(number):
    print(f"This function calculates the factorial from 1 to {number}")
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact

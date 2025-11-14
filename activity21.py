import random
print("THE NUMBER GUESSING GAME")
print("\n++++++++++++++++++++++++++")

random_value = random.randint(1, 5)
tries = 0
simula = True

name = input("What's your name? ")

while simula == True:
    num = eval(input("Guess a number: "))
    tries += 1
    
    if num == random_value:
        print("RRRRRRR!!!!!!!!!!!!!!!!!")
        break
    else:
        print("INCORRECT GUESS")
        continue

print(f"Hi {name} your guess is correct\nnumber of tries {tries}")

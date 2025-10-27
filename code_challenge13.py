
name = input("Enter your name: ")
print("ODD NUMBER SELECTOR")

odd = ""
sum = 0
uneven = True
while uneven == True:
    number = eval(input("Enter an odd number: "))

    if number % 2 == 1:  
        print("ODD NUMBER DETECTED")
        sum += number
        odd += str(number) + " "
        continue
    elif number== 0:
        print("LOOP TERMINATED")
        break
    else:
        if number % 2 == 0:
            print("EVEN NUMBER DETECTED")
        else:
            print("Invalid number / input")
        continue

print(f"Hi {name}, the sum of all odd numbers is {sum}")
print(f"ODD NUMBERS include the ff --> {odd}")
        


        

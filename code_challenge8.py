print("MULTIPLICATION TABLE MAKER")
num = int(input("Enter a number: "))

print(f"\nMultiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

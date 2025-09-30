print("\t\t *", end=" ")
for e in range(1,11,1):
    for f in range(10,e,-1):
        print(" ", end=" ")
    for g in range(1,e,1):
        print("*", end=" ")
    for h in range(1,e,1):
        print("*", end=" ")
    print()

name = input("Please input your name ---> ")
fare = eval(input("Fare fee ---> "))
isStudent = input("Are you currently a student (yes/no ) ")

if isStudent.lower() == "yes":
            discount = fare * 0.2
            new_fare = fare - discount
            print("Hi",name," Your discount is ", discount, "Your new fare is ", new_fare)
            print("Hi",name," Your only eligible for regular price")

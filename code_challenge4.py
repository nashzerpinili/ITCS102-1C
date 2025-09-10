print("Welcome to Anime World")
print("Select the genre action/comedy/horror?")

ur_choice = input("Enter your choice (action/comedy/horror): ")


if ur_choice == "action":
    print("Your chosen genre is Action")
    print("Choose your era:")
    print("2000/2010 ")

    ur_choice2 = input("Choose one (2000,2010): ")

    if ur_choice2 == "2000":
        print("You chose 2000")
        print("Here are my recommendations:")
        print("1. One Piece")
        print("2. Naruto Shippuden")
        print("3. Jujutse Kaisen")
        print("4. Hunter x Hunter")

    elif ur_choice2 == "2010":
        print("You chose 2010")
        print("Here are my recommendations:")
        print("1. One Punch Man")
        print("2. Spy x Family")
        print("3. Saiki K")


elif ur_choice == "comedy":
    print("Your chosen genre is Comedy")
    print("Choose your era:")
    print("2000/2010")

    ur_choice3 = input("Choose one (2000/2010): ")

    if ur_choice3 == "2000":
        print("Your era 2000")
        print("Here are my recommendations:")
        print("1. Gintama")
        print("2. Nichijou")
        print("3. Toradora!")

    elif ur_choice3 == "2010":
        print("Your era 2010")
        print("Here are my recommendations:")
        print("1. Konosuba")
        print("2. Mr. Osomatsu")
        print("3. Haganai")


elif ur_choice == "horror":
    print("Your chosen genre is Horror")
    print("Choose your era:")
    print("2000/2010")

    ur_choice4 = input("Choose one (2000/2010): ")

    if ur_choice4 == "2000":
        print("Your era 2000")
        print("Here are my recommendations:")
        print("1. Hell Girl")
        print("2. Mononoke")
        print("3. When They Cry")

    elif ur_choice4 == "2010":
        print("Your era 2010")
        print("Here are my recommendations:")
        print("1. Uzumaki")
        print("2. Parasyte")
        print("3. Homunculus")

deposit = input("Enter amount you want to deposit: ")
deposit = int(deposit)
bluebill = deposit // 1000
print("This is the breakdown of the amount you deposit : \n 1000 : ", bluebill)
deposit = deposit - bluebill * 1000
yellowbill = deposit // 500
print("\n 500 : ", yellowbill)
deposit = deposit - yellowbill * 500
greenbill = deposit // 200
print("\n 200 : ", greenbill)
deposit = deposit - greenbill * 200
purplebill = deposit // 100
print("\n 100 : ", purplebill)
deposit = deposit - purplebill * 100
redbill = deposit // 50
print("\n 50 : ", redbill)
deposit = deposit - redbill * 50
coin20 = deposit // 20
print("\n 20 : ", coin20)
deposit = deposit - coin20 * 20
coin5 = deposit // 5
print("\n 5 : ", coin5)
deposit = deposit - coin5 * 5

import random
print("welcome to the general shop \n \n what would you like to buy")

clothes = 0
fruits = 0
medicines = 0
total = 0
while True:
    choice = 0
    choice1 = 0
    choice2 = 0
    print("1.clothes \n 2.fruits \n 3.medicines")
    yeah = int(input("what would you like to buy :"))
    if yeah == 1:
        clothes = int(input("how many do you want :"))
        choice = clothes * random.randint(10,40) 
        total += choice 
        print("the price of this is :",choice)
    
    elif yeah == 2:
        fruits = int(input("how many do you want :"))
        choice1 = fruits * random.randint(2,15)
        total += choice1
        print("the price of this is :",choice1)
    
    elif yeah == 3:
        medicines = int(input("how many do you want :"))
        choice2 = medicines * random.randint(10,40)
        total += choice2
        print("the price of this is:",choice2)
        
    ble = input("do you still want to play this game (n/y) only lowercase letters work)")
    if ble == "n":
        print("your bill is :",total)
        print("thank you for shopping with us...!")
        break
        

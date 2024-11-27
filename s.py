import random
print("welcome to the general shop \n \n what would you like to buy")
clothes = 0
fruits = 0
medicines = 0
choice = 0
total = 0
while True:
    
    print("1.clothes \n 2.fruits \n 3.medicines")
    yeah = int(input("what would you like to buy :"))
    if yeah == 1:
        clothes = int(input("how many do you want :"))
        choice = clothes * random.randint(10,40)
        total += choice
    
    elif yeah == 2:
        fruits = int(input("how many do you want :"))
        choice = fruits * random.randint(2,15)
        total += choice
     
    elif yeah == 3:
        medicines = int(input("how many do you want :"))
        choice = medicines * random.randint(10,40)
        total += choice

    print("price = ",total)
    ble = input("do you still want to play this game (n/y) only lowercase letters work)")
    if ble == "n":
        print("your bill is :",total)
        break
        

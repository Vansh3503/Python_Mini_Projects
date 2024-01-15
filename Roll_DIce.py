import random
print("Welcome to Dice GAme")

while True:
    no=int(input("Enter 1 to Roll the Dice and 0 to exit:"))


    if no==1:
        print("ROLLING THE DICE")
        number=random.randint(1,6)
        print(number)

    elif no==0:
        break
    else:
        print("Invalid Input")

import random
print("Welcome to Dice GAme")
dice_outcome_list=[]
max_roll=0
while max_roll<5:
    number=int(input("Enter 1 to Roll the Dice and 0 to exit:"))


    if number==1:
        print("ROLLING THE DICE")
        dice_value=random.randint(1,6)
        dice_outcome_list.append(dice_value)
        max_roll=max_roll+1

    elif number==0:
        break
    else:
        print("Invalid Input")


print(dice_outcome_list)

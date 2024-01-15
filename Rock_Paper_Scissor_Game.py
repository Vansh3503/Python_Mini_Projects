import os
import random


def rock_sign():
    
    rockk='''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣷⡄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⠙⠻⠿⠋⣰⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣶⣤⣌⡙⠻⡿⢃⣾⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⡿⢿⣿⣿⣿⠃⠘⣠⣾⣿⣿⠟⢁⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣧⣄⡈⠡⣄⠀⢼⣿⣿⡿⠋⣰⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⡄⢹⣿⣦⣉⠛⢁⣾⣿⣿⡟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣷⣄⠙⠿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣦⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣷⣤⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
    print(rockk)
    


def scissor_sign():
    signn='''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠉⠉⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⡶⠶⢶⣤⣄⣀⠘⠛⠶⣴⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⡇⠀⠀⠀⠈⠙⢿⣿⣷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢷⣄⡀⠀⠀⢀⣸⡟⠉⠙⠻⣿⣿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠛⠛⠛⠉⠀⠀⢸⣦⣄⡉⠛⠿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣆⠀⠀⠙⠻⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣦⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀'''
    print(signn)


def paper_sign():
    papaerr='''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣿⣿⡿⠋⣀⣀⣀⣀⣀⣤⣤⣤⣶⣶⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡏⢀⣶⣿⣿⣿⣿⡿⠿⠿⠛⠛⠋⠁⠀⠀⠀
⠀⠀⣾⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣯⣁⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⢉⣁⣴⣿⣿⣿⣿⣉⣉⣉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠉⠉⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⢿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
    print(papaerr)
dicr={"rock":rock_sign,"paper":paper_sign,"scissor":scissor_sign}

LST=['rock','paper','scissor']
print("Welcome to Rock Paper Scissor Game")
flag=1
temp=1
while flag:
    game=int(input("Enter 1 to Start the Game and 0 to Exit: "))

    if game==0:
        break
    while temp:
        game_type=input("PLAYER OR ROBOT: ")
        game_type.lower()

        if game_type=='player':


                name_1=input("Enter User 1 Name : ")
                
                name_2=input("Enter User 2 Name : ")


                print("Let Start the Game: ")
               
                input_1=input(f"Enter  {name_1} (ROCK OR PAPER OR SCISSOR): ").lower()
               
                userr=dicr[input_1]
                userr()
                os.system("clear")
                
                input_2=input(f"Enter {name_2}(ROCK OR PAPER OR SCISSOR): ").lower()
               
                userr_2=dicr[input_2]
                userr_2()
                os.system("clear")

                print(f"{name_1} Inputs: ")
                userr()

                print(f"{name_2} input: ")
                userr_2()

                

                if input_1==input_2:
                    print("TIE")

                elif input_1=="rock" and input_2=="scissor":
                    print(f"{name_1} Win")

                elif input_1=="rock" and input_2=="paper":
                    print(f"{name_2} Win")

                elif input_1=="paper" and input_2=="scissor":
                    print(f"{name_2} Win")

                elif input_1=="paper" and input_2=="rock":
                    print(f"{name_1} Win")

                elif input_1=="scissor" and input_2=="paper":
                    print(f"{name_1} Win")

                elif input_1=="scissor" and input_2=="rock":
                    print(f"{name_2} Win")

                else:
                    print("Invalid Input!")
                break


        elif game_type=="robot":

                name_1=input("Enter User 1 Name : ")



                print("Let Start the Game: ")
            
                input_1=input(f"Enter {name_1} (ROCK OR PAPER OR SCISSOR): ")
                input_1.lower()
            
                userr=dicr[input_1]
                userr()
                os.system("clear")
                input_2=random.choice(LST)
                userr_2=dicr[input_2]
                userr_2()
                os.system("clear")

                print(f"{name_1} Inputs: ")
                userr()

                print("Robot input: ")
                userr_2()

                if input_1==input_2:
                    print("TIE")

                elif input_1=="rock" and input_2=="scissor":
                    print(f"{name_1} Win")

                elif input_1=="rock" and input_2=="paper":
                    
                    print("Robot  Win")

                elif input_1=="paper" and input_2=="scissor":
                  
                    print("Robot  Win")

                elif input_1=="paper" and input_2=="rock":
                    print(f"{name_1} Win")

                elif input_1=="scissor" and input_2=="paper":
                    print(f"{name_1} Win")

                elif input_1=="scissor" and input_2=="rock":
                    
                    print("Robot  Win")

                else:
                    print("Invalid Input!")
                break

        else:
            print("Invalid Input")
            temp=1
        


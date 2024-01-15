import random
print("WElcome to Guessing game")
flag=1

while flag:

    flag=int(input("enter 1 to play the game 0 to exit: "))
    if flag==1:
        print("Enter the Range:")
        A=int(input("Enter the lower range: "))
        B=int(input("Enter the upper range: "))
        Guess_counter=0
        if(A<B):
            C=random.randint(A,B)
          

            print("Lets start the guessing game")

            while C:


                n=int(input("Enter your Number: "))

                if n>B:
                    print("Out of Range")

                elif n<A:
                    print("Out of range")
                    
                


                elif n>C:
                    print("Try again! Too High ")
                    
                    Guess_counter=Guess_counter+1

                elif n<C:
                    print("Try again! Too Low")
                    Guess_counter=Guess_counter+1
                
                

                


                elif n==C:
                    print(f'Congrats You Guess the right Number  with {Guess_counter} guesses')
            

                    break
        else:
            print("Invalid Range")

    elif flag==0:
        print("Bye Bye")

    else:
        print("invalid input ")

        
                






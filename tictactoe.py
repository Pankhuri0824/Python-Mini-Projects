cross="X"
circle="O"

def printgrid(list):
    for a in range (3):
        for b in range(3):
            ind=(3*(a))+b
            if(list[ind]==0):
                print("_", end=" ")
            elif(list[ind]==1):
                print("X", end=" ")
            elif(list[ind]==2):
                print("O", end=" ")
        print("\n")


def single():
    print("\n"+"\033[1mSINGLE PLAYER MODE\033[0m"+"\n")
    list=[0]*9
    global cross
    global circle

def multi():
    print("\n"+"\033[1mMULTI PLAYER MODE\033[0m"+"\n")
    list=[0]*9
    global cross # dented by 1
    global circle # denoted by 2 ## 0 means empty
    turn=0 

    while(True):
        
        if(turn==0): #player one X turn
            print("Player 1's turn\n")

            turnbool=True
            while(turnbool):
                row=int(input("Enter Row:"))
                col=int(input("Enter Coloumn:"))
                index=(3*(row-1))+col-1

                if(list[index]==0):
                    list[index]=1
                    turnbool=False
                else:
                    print("Block already marked. Try again")
                
                printgrid(list)
            turn=1

        elif(turn==1): #player one turn
            print("Player 2's turn\n")

            turnbool=True
            while(turnbool):
                row=int(input("Enter Row:"))
                col=int(input("Enter Coloumn:"))
                index=(3*(row-1))+col-1

                if(list[index]==0):
                    list[index]=2
                    turnbool=False
                else:
                    print("Block already marked. Try again")
                
                printgrid(list)
            turn=0





    for i in range(9):
        print(list[i])

t=True
while (t):
    print("\n"+"\033[1mWELCOME TO TIC-TAC-TOE\033[0m"+"\n")
    print("1.Single PLayer Mode\n"+"2.Multiplayer Mode\n"+"3.Exit Game\n"+"----------------------")
    one=int(input())

    if(one==1):
        t1=True
        while(t1):
            single()

            print("1.Play Again\n"+"2.Exit Game\n")
            re=int(input())
            if(re==1):
                pass
            elif(re==2):
                print("Thank you for playing . See you soon :)")
                t=False
                t1=False
            else:
                print("Invalid entry. Try again")

    elif(one==2):
        t1=True
        while(t1):
            multi()

            print("1.Play Again\n"+"2.Exit Game\n")
            re=int(input())
            if(re==1):
                pass
            elif(re==2):
                print("Thank you for playing . See you soon :)")
                t=False
                t1=False
            else:
                print("Invalid entry. Try again")

    elif(one==3):
        print("Thank you for playing . See you soon :)")
        t=False

    else:
        print("Invalid entry. Try again")

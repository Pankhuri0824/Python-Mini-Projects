cross="X"
circle="O"

def single():
    print("\n"+"\033[1mSINGLE PLAYER MODE\033[0m"+"\n")
    list=[0]*9
    global cross
    global circle

def multi():
    print("\n"+"\033[1mMULTI PLAYER MODE\033[0m"+"\n")
    list=[0]*9
    global cross # dented by 1
    global circle # denoted by 2
    turn=0 

    while(True):
        if(turn==0): #player one turn
            print("Player 1's turn\n"+"Enter box to be marked : ")
            row=int(input())
            col=int(input())
            index=(3*(row-1))+col-1



            turn=1

        elif(turn==1): #player one turn
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

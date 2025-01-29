import random
def mainMenu():
    player1=str(input("Your Turn. Rock(R), Paper(P), Scissor(S): "))
    ranDo=random.randint(1, 3)
    if ranDo==1:
        player2='R'
    elif ranDo==2:
        player2='P'
    elif ranDo==3:
        player2='S'
    else:
        mainMenu()
    player1=player1.upper()

    if player2=='R':
        if player1=='R':
            print("Tie Because computer also choose Rock.\n")
            mainMenu()
        elif player1=='P':
            print("You win Because computer choose Rock.\n")
            mainMenu()
        elif player1=='S':
            print("You lose Because computer choose Rock.\n")
            mainMenu()
        else:
            mainMenu()
    elif player2=='P':
        if player1=='R':
            print("You lose because computer choose Paper.\n")
            mainMenu()
        elif player1=='P':
            print("Tie Because computer also choose Paper.\n")
            mainMenu()
        elif player1=='S':
            print("You win Because computer choose Paper.\n")
            mainMenu()
        else:
            mainMenu()
    elif player2=='S':
        if player1=='S':
            print("Tie Because computer also choose Scissor.\n")
            mainMenu()
        elif player1=='R':
            print("You Win because computer choose Scissor.\n")
            mainMenu()
        elif player1=='P':
            print("You lose Because computer choose Scissor.\n")
            mainMenu()
        else:
            mainMenu()
    else:
        mainMenu()
print(mainMenu())

        
            

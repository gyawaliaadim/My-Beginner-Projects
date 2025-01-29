import random
def mainMenu():
    player1=str(input("Your Turn. Snake(S), Water(W), Gun(G): "))
    ranDo=random.randint(1,3)
    if ranDo==1:
        player2='S'
    elif ranDo==2:
        player2='W'
    elif ranDo==3:
        player2='G'
    else:
        mainMenu()
    player1=player1.upper()

    if player2=='S':
        if player1=='S':
            print("Tie because computer also choose Snake.\n")
            mainMenu()
        elif player1=='W':
            print("You lose because computer choose Water.\n")
            mainMenu()
        elif player1=='G':
            print("You win because computer choose Snake.\n")
            mainMenu()
        else:
            mainMenu()
    elif player2=='W':
        if player1=='W':
            print("Tie because computer also choose Water.\n")
            mainmenu()
        elif player1=='G':
            print("You lose because computer choose Water.\n")
            mainMenu()
        elif player1=='S':
            print("You win because computer choose Water.\n")
            mainMenu()
        else:
            mainMenu()
    elif player2=='G':
        if player1=='G':
            print("Tie because computer also choose gun.\n")
            mainMenu()
        elif player1=='S':
            print("You lose because computer choose gun.\n")
            mainMenu()
        elif player1=='W':
            print("You win because computer choose Gun.\n")
            mainMenu()
        else:
            mainMenu()
    else:
        mainMenu()
print(mainMenu())

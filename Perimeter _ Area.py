def mainMenu():
    print('''1) Find Perimeter of Rectrangle
2) Find Perimeter of Square
3) Find Area of Rectrangle
4) Find Area of Square
5) Exit''')
    a=input("Your Choice: ")
    a=int(a)
    if a==1:
        main()
    elif a==2:
        menu()
    elif a==3:
        menumain()
    elif a==4:
        mainmenu()
    elif a==5:
        exit()
    else:
        print("Please Enter the valid choice.")
        mainMenu()
    main()

def main():
    #Perimater of rectrangle
    a=int(input("Length: "))
    b=int(input("Breath: "))
    c=(2*(a+b))
    print(f"Perimeter is: {c}")
    print("\n")
    mainMenu()

def menu():
    #Perimeter of square
    a=int(input("Length: "))
    b=4*a
    print(f"Perimeter is: {b}")
    print("\n")
    mainMenu()

def menumain():
    #Area of rectrangle
    a=int(input("Length: "))
    b=int(input("Breath: "))
    c=a*b
    print(f"Area is: {c}")
    print("\n")
    mainMenu()

def mainmenu():
    #Area of square
    a=int(input("Length: "))
    c=a*a
    print(f"Area is: {c}")
    print("\n")
    mainMenu()



print(mainMenu())

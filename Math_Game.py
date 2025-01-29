import random
import time
def main():
    a=random.randint(1, 10)
    b=random.randint(1, 10)
    print(f"What is {a} * {b}?")
    c=int(input("Answer: "))
    if c==(a*b):
        print("Correct Answer\n")
        mainMenu()
    else:
        print("Incorrect Answer\n")
        mainMenu()
def menu():
    a=random.randint(1,20)
    b=random.randint(1,20)
    print(f"What is {a} * {b}?")
    c=int(input("Answer: "))
    if c==(a*b):
        print("Correct Answer\n")
        mainMenu()
    else:
        print("Incorrect Answer\n")
        mainMenu()
def menuMain():
    a=random.randint(1,50)
    b=random.randint(1,50)
    print(f"What is {a} * {b}?")
    c=int(input("Answer: "))
    if c==(a*b):
        print("Correct Answer\n")
        mainMenu()
    else:
        print("Incorrect Answer\n")
        mainMenu()
def mainmenu():
    a=random.randint(1,100)
    b=random.randint(1,100)
    print(f"What is {a} * {b}?")
    c=int(input("Answer: "))
    if c==(a*b):
        print("Correct Answer\n")
        mainMenu()
    else:
        print("Incorrect Answer\n")
        mainMenu()
def mainMenu():
    print('''1) Easy
2) Normal
3) Hard
4) Extreme
Q) Quit''')
    e=(input("Your Choice: "))
    e=e.upper()
    e=str(e)
    if e=="Q":
        print("Thank you for using")
        input()
        exit()  
    e=int(e)
    if e==1:
        main()
    elif e==2:
        menu()
    elif e==3:
        menuMain()
    elif e==4:
        mainmenu()
    else:
        mainMenu()
print(mainMenu())

def main():
    a=int(input("Amount: "))
    b=int(input("Principal: "))
    d=a-b
    print(f'''A={a}
P={b}
I=?
F=P=A-I
A-I={a}-{b}={d}
So I={d}''')
    mainMenu()
def menu():
    a=int(input("Principal: "))
    b=int(input("Intrest: "))
    d=a+b
    print(f'''P={a}
I={b}
A=?
F=A=P+I
P+I={a}+{b}={d}
So A={d}\n''')
    mainMenu()
def menuMain():
    a=int(input("Amount: "))
    b=int(input("Intrest: "))
    d=a-b
    print(f'''A={a}
I={b}
P=?
F=P=A-I
A-I={a}-{b}={d}
So P={d}\n''')
    mainMenu()
def mainMenu():
    print('''1) Find Intrest from Amount and Pricipal
2) Find Amount from Pricipal and Intrest
3) Find Pricipal from Amount and Intrest
Q) Quit''')
    a=input("Your choice: ")
    a=str(a)
    a=a.upper()
    if a=='Q':
        print("Thank you for using.")
        input()
        exit()
    a=int(a)
    if a==1:
        main()
    elif a==2:
        menu()
    elif a==3:
        menuMain()
print(mainMenu())

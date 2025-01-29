def mainMenu():
    print("1) Substraction[-]")
    print("2) Addition[+]")
    print("3) Multiplication[*]")
    print("4) Division[\]")
    a = int(input("Your choice: "))
    if a==1:
        print("Substraction")
        b=float(input("Enter the minuend: "))
        c=float(input("Enter the subtrahend: "))
        d="Difference: %s"
        print(d % (b-c))
        input()
        mainMenu()
    elif a==2:
        print("Addition")
        b=float(input("Enter the addend: "))
        c=float(input("Enter the addend: "))
        d="Sum: %s"
        print(d % (b+c))
        input()
        mainMenu()
    elif a==3:
        print("Multiplication")
        b=float(input("Enter the multiplicand: "))
        c=float(input("Enter the multiplier: "))
        d="Product: %s"
        print(d % (b*c))
        input()
        mainMenu()
    elif a==4:
        print("Division")
        b=float(input("Enter the dividend: "))
        c=float(input("Enter the divisor: "))
        d="Quotient: %s"
        e="Reminder: %s"
        print(d % (b/c))
        print(e % (b % c))
        input()
        mainMenu()
print(mainMenu())

def mainMenu():
    a=int(input("Any number: "))
    b=a%2
    d="%s is a Even Number."
    c=(d % a)
    f="%s is a Odd Number"
    e=(f % a)
    if b==0:
        print(c)
    elif b==1:
        print(e)
    mainMenu()
print(mainMenu())

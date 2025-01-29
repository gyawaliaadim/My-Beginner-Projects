from playsound import playsound
def mainMenu():
    a=str(input("Do you want to play Abandoned & Shiah Maisel([Y]/[N]): "))
    a=a.upper()
    if a=="Y":
        print("Playing Cartoon On & On")
        playsound('Music.mp3')
    elif a=="N":
        print("Thank You for watching")
        input("Press Enter to continue")
        exit()
    else:
        mainMenu()
print(mainMenu())

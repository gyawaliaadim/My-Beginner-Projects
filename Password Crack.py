# importing random
from random import *
def mainMenu():
    # taking input from user
    user_pass = input("Enter your password:")

    # storing alphabet letter to use thm to crack password
    password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
                'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*',
                '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\ ',
                '|', ';', ':', '<', '>', ',', '.', '/',
                '?', '~', '`', ''' ''']

    # initializing an empty string
    guess = ""


    # using while loop to generate many passwords untill one of
    # them does not matches user_pass
    while (guess != user_pass):
        guess = ""
        # generating random passwords using for loop
        for letter in range(len(user_pass)):
            guess_letter = password[randint(0, 65)]
            guess = str(guess_letter) + str(guess)
        # printing guessed passwords
        print(guess)
        
    # printing the matched password
    print(f"Your password is {guess}")
    mainMenu()
print(mainMenu())


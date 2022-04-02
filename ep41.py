# Dice Roller

import random


rolled = random.randrange(1, 7)
guess = 0


while(True):
    number = int(input("Input a number: "))
    if number == rolled:
        print("\nComputer rolled", rolled, ", and it took you",
              guess + 1, "try(s) to guess correctly. ")
        break
    else:
        guess += 1
        print("\nNice try, but nope! You still have", 3-guess, "try(s) left")
        if rolled > number:
            print("(Hint: the number should be higher)")
        else:
            print("(Hint: the number should be lower)")
    if guess >= 3:
        print("\nSorry, better luck next time.")
        break

import random
import time

print("Welcome into : Guess The Number")
time.sleep(2)
print("You will have a number to guess between 1 and 100")
time.sleep(2)
target_number = random.randint(0, 101)
your_number = int(input("Enter a number between 1 and 100 :"))

if target_number != your_number:
    while target_number != your_number:
        if target_number > your_number:
            print("Try again !")
            time.sleep(2)
            print("Your number was too low !")
        elif target_number < your_number:
            print("Try again !")
            time.sleep(2)
            print("Your number was too high !")
        time.sleep(2)
        your_number = int(input("Enter a new number between 1 and 100 :"))

print("Congrats ! You found the right number !")
time.sleep(2)
print("Relaunch the program to play again")
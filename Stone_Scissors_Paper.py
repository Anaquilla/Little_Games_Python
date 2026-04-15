import time
import random
print("Welcome into Stone, Paper, Scissors")
time.sleep(1)
print("You will play against a computer")
time.sleep(1)
print("To start the game, you will to press s or S")
time.sleep(1)
print("The game won't stop until you write 'finish'")
time.sleep(1)
print("I will let you write your answer in the same way there are displayed in the name")
time.sleep(1)
print("Enjoy it !")

s_player = 0
s_robot = 0
proposition = ['Stone', 'Paper', 'Scissors']

answer = input("Ready to start ? Press s or S :")
answer = input("Write your first proposition :")
while answer != 'Finish':
    robot = proposition[random.randint(0, len(proposition)-1)]
    if answer == 'Stone' and robot == 'Paper' or answer == 'Scissors' and robot == 'Stone' or answer == 'Paper' and robot == 'Scissors':
        print(f"You lost ! You said {answer} and the robot said {robot}")
        s_robot += 1

    elif answer == 'Stone' and robot == 'Scissors' or answer == 'Scissors' and robot == 'Paper' or answer == 'Paper' and robot == 'Stone':
        print(f"You won ! You said {answer} and the robot said {robot}")
        s_player += 1

    elif answer == robot:
        print("You wrote the same proposition, nobody won")

    answer = input("Write a new propostion or write 'finish' to leave :")

print(f"You finished the game with {s_player} points, the robot with {s_robot}")
time.sleep(1)
if s_player > s_robot:
    print("You won the game !")
else:
    print("You lost the game !")
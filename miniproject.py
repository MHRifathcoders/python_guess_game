#Guess the number
import random

target = random.randint(1, 100)

while True:
    userchoice= int(input("Enter your Guess Number: "))
    if userchoice == target:
        print(f"You guess the right number")
        break
    elif userchoice > target:
        print("Take the Guess number small")
    else:
        print("You need to take bigger number to guess")
print("-------Game Over------")
import random

secret= random.randint(1, 100)
guess=0
print("welcome to the number guessing game")
print("guess the number between 1 to 100")

while guess !=secret:
    guess=int(input("enter your guess:"))
    if guess<secret:
        print("too low! try again")
    elif guess>secret:
        print("too high! try again")
    else:
        print("con*gratulations! you guessed the number.") 
        break
input("press enter to exit")
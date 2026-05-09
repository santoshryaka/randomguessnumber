#import require model for project
import random

#Generates a random number
secret = random.randint(1,100)
guess = 0
print("__welcome to the number guessing game__")
print("guess the number between 1 to 100.")

#loops run until correct guess
while guess != secret:
    guess=int(input("enter your guess:"))
    if guess<secret:
        print("too low! try again.")
    elif guess>secret:
        print("too high! try again.")
    else:
        print("con*gratulations! you guessed the number.") 
        break
print("__Thankyou for playing this game__")

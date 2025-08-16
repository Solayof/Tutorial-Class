import random
#include <stdio.h>
value = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

while True:
    if guess < value:
        print("Too low! Try again.")
    elif guess > value:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
    guess = int(input("Guess a number between 1 and 10: "))
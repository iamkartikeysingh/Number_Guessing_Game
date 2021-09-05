from art import logo
import random

print(logo)
print("Welcome to Number Guessing Game.")
print("I am thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)
difficulty_choice = input("Choose your difficulty. Type 'easy' or 'hard': ")

def easy_choice():
    for i in range(10):
        print(f"You have {10 - i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
        else:
            print(f"You got it. The answer was {guess}.")
            break


def hard_choice():
    for i in range(5):
        print(f"You have {5 - i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
        else:
            print(f"You got it. The answer was {guess}.")
            break

if difficulty_choice == "easy":
    easy_choice()

elif difficulty_choice == "hard":
    hard_choice()

import random

from art import number_guessing
print(number_guessing)

print("Welcome to the number game!")
print("I am thinking of a number from 1 to 100!")
computer_choice = random.randint(1, 100)
difficulty = input("Enter a difficulty, Easy or Hard! \n").lower()
my_choice = int(input("Enter your choice of number \n"))


def easy_game(my_choice, computer_choice):
    if_game = False
    no_of_attempts = 10
    print("You have 10 attempts to win this game \n")
    while not if_game:
        if my_choice > computer_choice:
            print("Guess Lower")
            no_of_attempts -= 1
            print(f"You have {no_of_attempts} more attempts")
            my_choice = int(input("Enter your choice of number \n"))

        elif my_choice < computer_choice:
            print("Guess Higher")
            no_of_attempts -= 1
            print(f"You have {no_of_attempts} more attempts")
            my_choice = int(input("Enter your choice of number \n"))

        elif my_choice == computer_choice:
            print("You made the right choice. You win!!")
            if_game = True

        elif no_of_attempts == 0 and my_choice != computer_choice:
            print("You lose, the number was {computer_choice")

        else:
            print(f"You lost the game. The number was {computer_choice}")
            if_game = True


def hard_game(my_choice, computer_choice):
    if_game = False
    no_of_attempts = 5

    print("You have 5 attempts to win this game \n")

    while not if_game:
        if no_of_attempts == 0 and my_choice != computer_choice:
            print(f"You lost the game. The number was {computer_choice}")
            if_game = True

        elif my_choice > computer_choice:
            print("Guess Lower ")
            no_of_attempts -= 1
            print(f"You have {no_of_attempts} more attempts")
            my_choice = int(input("Enter your choice of number "))
            print()

        elif my_choice < computer_choice:
            print("Guess Higher")
            no_of_attempts -= 1
            print(f"You have {no_of_attempts} more attempts")
            my_choice = int(input("Enter your choice of number "))
            print()

        else:
            print("You made the right choice. You win!!")
            if_game = True


if difficulty == "easy":
    easy_game(my_choice=my_choice, computer_choice=computer_choice)
    if_game = True

else:
    hard_game(my_choice=my_choice, computer_choice=computer_choice)
    if_game = True

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_choice>= 3 or user_choice < 0:
    print("Invalid Number, Winner can't be determined!!")
    
else:
    games_images = [rock,paper,scissors]


    print(f"You chose: \n {games_images[user_choice]}")

    import random
    computer_choice = random.randint(0 , 2)
    print(f"Computer Chose: \n {games_images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You Win")
        
    elif computer_choice > user_choice:
        print("You Lose")

    elif computer_choice == user_choice:
        print("It's a draw!!")

    elif computer_choice == 0 and user_choice== 2:
        print("You lose!!")
        
    elif user_choice > computer_choice:
        print("You win!")
    


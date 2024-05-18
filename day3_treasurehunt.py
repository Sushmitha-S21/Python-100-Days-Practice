print('''
 
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
sush       / HHH  \\
          /  \_/   \\


''')

print("Welcome to my Treasure Island Game")
print("Your mission in this game is to find your treasure, let's test your luck, Cheers.🥂")

start = input("To start the game, Choose which side do you want to go? 'Left' or 'Right'? ").lower()

if  start == "left":
    choice2 = input("Congratulations, you have reached a lake,do you want to swim or do you want to wait for the boat? ").lower()
    if choice2 == "wait":
        choice3 = input("Kudos, you have arrived at the last stage of the game. Which door do you want to choose? Red, Yellow or Green? ").lower()
        if choice3 == "red":
            #end
            print("You fell prey to the hungry lions")
        if choice3 == "yellow":
            print("Congratulations, you found the treasure!! 🙌🤑")
        if choice3 == "green":
            print("Sorry fella, try again!!")
        else:
            ("Sorry, try again!!")
    else:
        print("Game over! The crocordiles caught you")  
else:
    print("Oops!! Sorry Game Over, you fell into the dragon whole")
    
    

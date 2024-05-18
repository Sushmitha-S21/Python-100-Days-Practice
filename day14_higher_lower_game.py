import random
from day14_game_data import data
from art import logo_higher_lower, vs_higher_lower

score = 0

print(logo_higher_lower)
print()
print()

#!format account data into printable format


def format_data(account):
    '''Takes the account data and returns printable format'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, is a {account_descr}, from {account_country}"


account_b = random.choice(data)
game_should_continue = True

while game_should_continue:
    #!generate random account from data
    #!making account at position B to move to position A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs_higher_lower)
    print(f"Against B: {format_data(account_b)}")

    #!ask users for a guess between A and B

    user_choice = input("Who has more followers? A or B ").lower()

    #!check if user is correct or wrong
    # get follower count of each account,use if statement to check if user is correct
    def check_answer(guess, a_follower, b_follower):

        if a_follower > b_follower:
            return guess == "a"

        else:
            return guess == "b"

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(user_choice, a_follower_count, b_follower_count)

    #! Give user feedback on their Guess and track the score if it's right

    if is_correct:
        score += 1
        print(f"You are right! You're currect score is {score}")
        print("\n"*15)
        print(logo_higher_lower)

    else:
        game_should_continue = False
        print(f"You are wrong..  Final score {score}")

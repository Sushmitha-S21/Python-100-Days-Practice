import random

def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

user_cards = []
computer_cards =[]

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
print(user_cards, computer_cards)

def calculate_score(cards):
    user_score = user_cards[0] + user_cards[1]
    computer_score = computer_cards[0] + computer_cards[1]
    print(user_score)
    print(computer_score)
    
calculate_score()


    

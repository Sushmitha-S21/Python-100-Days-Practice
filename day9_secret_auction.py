from art import auction
print(auction)
print("Welcome to the Secret Auction Program!")

is_bid = False

bid_dictionary = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {bidder}. They won with a bid of ${highest_bid}")
    
while not is_bid:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $ "))
    bid_dictionary[name] =  bid
    repeat = input("Are there any other bidders? Type Y or N ").lower() 
    if repeat == "n":
        is_bid = True
        find_highest_bidder(bid_dictionary)
    else:
        print("\n"*50)
    
    
    


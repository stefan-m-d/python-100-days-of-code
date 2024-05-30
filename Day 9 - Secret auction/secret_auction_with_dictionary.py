import os
print ("Welcome to the secret auction")
bidders = {}
name = input ("What is your name? \n")
bid = int(input("What is your bid? $ \n"))
bidders[name]=bid
def find_highest_bidder(bidding_record):
    max_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>max_bid:
            max_bid=bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")
flag = True
while flag:
    add_more = input ("Are there any other bidders? \n")
    if add_more.lower() == "no":
        flag = False
    else: 
        os.system('cls')
        name = input ("What is your name? \n")
        bid = int(input("What is your bid? $ \n"))
        bidders[name]=bid
find_highest_bidder(bidders)


    


    
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print(logo)
print("WELCOME TO THE SECRET ACTION PROGRAM")

bids = {}
bidding_finished = False

def higher_bidder(bidding_record):
    higher_bid = 0
    winner = ""
    # bidding_record = {" "}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > higher_bid:
            higher_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${higher_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("Wha is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type yes or no: ")
    if should_continue == "no":
        bidding_finished = True
        higher_bidder(bids)
    elif should_continue == "yes":
        print("\n"*100)




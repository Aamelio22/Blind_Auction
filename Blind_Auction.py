# Import logo from art and clear function
from replit import clear
from art import logo

# Create dictionary to hold keys and values.
bid_info = {}
get_bid = True
# Greet the user.
print(logo)
print("Welcome to the secret auction program.\n")


# Defining a function to add bid to a dictionary.
def append_dict(name, amount):
    bid_info[name] = amount


# Creating while loop to get more bids, if any.

while get_bid == True:
    # Get the user's name and bid amount.
    bidder_name = input("What's your name?:")
    bid = int(input("What's your bid?: $"))
    append_dict(name=bidder_name, amount=bid)
    while True:
        more_bid = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
        if more_bid == "yes":
            get_bid = True
            clear()
            break
        elif more_bid == "no":
            get_bid = False
            break
        else:
            print("Please enter yes or no.")
            break
# Get highest bid and the winner.
highest_bid = 0
winner = []
for key in bid_info:
    current_bid = bid_info[key]
    if current_bid > highest_bid:
        highest_bid = current_bid
        winner = (key, current_bid)
print(f"The winner is {winner[0]} with a bid of ${winner[1]}.")



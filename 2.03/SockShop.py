from random import shuffle

"""SockShop.py: Interacts with a consumer and helps them determine the best product for their price range."""

__author__  = "Eric Rabil"
__date__    = "10/14/2018"

class Item:
    """Represents an item being sold"""
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

def print_with_separator(text, separator):
    """Prints a string with the given separator"""
    print(separator)
    print(text)
    print(separator)

def main():
    # App constants
    GREETING = "Welcome to the Sock Shop!"
    GOODBYE = "Thanks for shopping!"
    SEPARATOR = "".ljust(len(GREETING), "*")
    SOCK_NAMES = [
        "Wool",
        "Paper",
        "Concrete",
        "Steel Wool",
        "Cardboard",
        "Cotton",
        "Synthetic",
        "Plastic"
    ]
    SOCK_PRICES = [
        1,
        5,
        10,
        15,
        25,
        75,
        125,
        175
    ]
    # Randomize price order
    shuffle(SOCK_PRICES)
    # Randomize name order
    shuffle(SOCK_NAMES)
    # Maps name to the corresponding index in prices
    SOCKS: list = list(map(
        lambda name: Item(name, SOCK_PRICES[SOCK_NAMES.index(name)]), SOCK_NAMES))

    budget = None

    while budget == None:
        try:
            raw_budget = input("What is your budget? ").replace("$", "")
            budget = int(raw_budget)
        except ValueError:
            print("Please provide a valid budget")
            budget = None

    print_with_separator(GREETING, SEPARATOR)

    # Sort by price
    SOCKS.sort(key=lambda item: item.price)
    # Filter out socks outside of price range
    USABLE_SOCKS: list = list(filter(lambda item: item.price <= budget, SOCKS))
    # Put most expensive socks at start of list
    USABLE_SOCKS.reverse()

    sock = USABLE_SOCKS[0] if len(USABLE_SOCKS) > 0 else None

    print(f"Your budget is ${str(budget)}.")

    remaining_required = None if budget >= 200 else 200 - budget

    print(
        "By spending at least $200, you have qualified for a free gift!"
            if remaining_required is None else
        f"If you spend ${str(remaining_required)} more, you qualify for a free gift!"
    )

    # Promote a sock to purchase
    if sock != None:
        print(
            f"With that in mind, we recommend our\n{sock.name} Socks, for ${sock.price}."
        )
        print("You won't want to pass up this dazzling pair.")

    print_with_separator(GOODBYE, SEPARATOR)

main()
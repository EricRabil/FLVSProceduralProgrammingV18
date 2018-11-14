import datetime

"""VoterRegistration.py: Engages with the user and discusses the importance of voting."""

__author__  = "Eric Rabil"
__date__    = "10/14/2018"

# Greeting
def hello(name):
    print("Hello, " + name + "!")

# Exit message
def goodbye(name):
    print("Goodbye, " + name + "!")

def main():
    # Get their name
    name = input("Hello! What's your name? ")

    hello(name)

    # Are they a pre-registered voter?
    pre_registered = input("Are you pre-registered to vote? ").lower() == "yes"

    if pre_registered:
        print("Thank you for taking the initiative to get pre-registered!")
        goodbye(name)
        exit(0)

    age = None

    # Ensure a valid age is parsed
    while age == None:
        try:
            age = int(input("How old are you? "))
        except ValueError:
            print("Please provide a valid age.")

    # Ask what voting means to them. Discard the input as it is not used again.
    input("What does voting mean to you? ")

    print("That's amazing! It's very important to understand the importance of voting, even if you cannot yet vote.")

    # Calculate how many years until they can vote
    years_until_vote = 18 - age

    print("You will be able to vote in roughly " + str(years_until_vote) + " years.")

    goodbye(name)

main()
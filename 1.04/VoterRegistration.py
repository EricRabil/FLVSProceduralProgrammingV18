import datetime

# Get their name
name = raw_input("Hello! What's your name? ")

def hello():
    print("Hello, " + name + "!")

def goodbye():
    print("Goodbye, " + name + "!")

hello()

# Are they a pre-registered voter?
pre_registered = raw_input("Are you pre-registered to vote? ").lower() == "yes"

if pre_registered:
    print("Thank you for taking the initiative to get pre-registered!")
    goodbye()
    exit(0)

age = None

# Ensure a valid age is parsed
while age == None:
    try:
        age = int(raw_input("How old are you? "))
    except ValueError:
        print("Please provide a valid age.")

# Ask what voting means to them. Discard the input as it is not used again.
raw_input("What does voting mean to you? ")

print("That's amazing! It's very important to understand the importance of voting, even if you cannot yet vote.")

# Calculate how many years until they can vote
years_until_vote = 18 - age

print("You will be able to vote in roughly " + str(years_until_vote) + " years.")

goodbye()
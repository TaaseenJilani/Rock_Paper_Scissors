import random
list_plays = ["rock", "paper", "scissors"]
choice = random.choice(list_plays)
choice_2 = random.choice(list_plays)
print("You played " + choice + "!")
a = input("")
print("The opponent played " + choice_2 + "!")
if choice == choice_2:
    print("It's a tie!")
if choice == "rock":
    if choice_2 == "paper":
        b = input("")
        print("The opponent won!")
    if choice_2 == "scissors":
        c = input("")
        print("You won!")
if choice == "paper":
    if choice_2 == "rock":
        d = input("")
        print("You won!")
    if choice_2 == "scissors":
        e = input("")
        print("The opponent won!")
if choice == "scissors":
    if choice_2 == "paper":
        f = input("")
        print("You won!")
    if choice_2 == "rock":
        g = input("")
        print("The opponent won!")
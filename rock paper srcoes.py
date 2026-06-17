#Write a Program to Play Rock, Paper and Scissors

import random

options = ["rock", "paper", "scissors"]
sroces = 0

print("Lets Play Rock, Paper and Scissors with Computer.")

while True:
    option = random.choice(options)
    guess = input("Write Your blw Rock, Paper and Scissors (q to Quit) : ").lower()
    if guess == "q":
        break
    elif guess in options:
        if guess == option:
            print(f"The Game Tie Because {guess} are Equal to {option}")
        elif option == options[0] and guess == options[1]:
            print(f"The Game is Won by You Because {options[1]} Beats {options[0]}")
            sroces += 1
        elif option == options[0] and guess == options[2]:
            print(f"The Game is Won by Computer Because {options[0]} Beats {options[2]}")
        elif option == options[1] and guess == options[0]:
            print(f"The Game is Won by Computer Because {options[1]} Beats {options[0]}")
        elif option == options[1] and guess == options[2]:
            print(f"The Game is Won by You Because {options[2]} Beats {options[1]}")
            sroces += 1
        elif option == options[2] and guess == options[0]:
            print(f"The Game is Won by You Because {options[0]} Beats {options[2]}")
            sroces += 1
        elif option == options[2] and guess == options[1]:
            print(f"The Game is Won by Computer Because {options[2]} Beats {options[1]}")    
    else:
        print("You Wrote an Invalid option")

print(f"You Won {sroces} Games against the Computer")

# import random

# dice_art = {
#     1: ["┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"],
#     2: ["┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"],
#     3: ["┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"],
#     4: ["┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"],
#     5: ["┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"],
#     6: ["┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘"]
# }
# while True:
#     num = input("Write the Number of Dices you Wanted:")
#     if num.isdigit():
#         num  = int(num)
#         break

# low = 1
# high = 6
# a =  0

# for i in range(a,num):
#     z = random.randint(low,high)
#     for x  in  dice_art.get(z):
#         print(x, end= "")
#         print()
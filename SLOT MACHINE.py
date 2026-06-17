# Write a Program for Slot Machine

import random

import time

def menu():

    print("************************")
    print("      Slot Machine      ")
    print("************************")
    print("Symbol: 🍋 🍉 🍒      ")
    print("************************")

def balance_sys(balance):

    print(f"Your Balances is {balance}Rs.")

    bet = (input("Write the amount of Bet (q to quit) : ")).lower()

    if bet.isdigit():

        bet = int(bet)

        if bet > balance:
            print("Bet can be Bigger then Total Balance.")
            return balance , 0
        
        elif bet <= 0:
            print("Bet can't be Zero or Lower then Zero")
            return balance , 0
        
        else:
            balance -= bet
            return balance , bet
        
    elif bet == "q":
        return balance , "q"
    
    else:
        print(f"{bet} is not Valid.")
        print("Please Write a Valid bet.")
        return balance, 0
    
     
def slot_machine(bet, balance):

    fruits = ["🍋","🍉","🍒"]
    choice = []

    for fruit in fruits:
        fruit = random.choice(fruits)
        choice.append(fruit)

    print("************************")
    print("        Spinning        ")
    print("************************")

    time.sleep(1)

    for fruit in choice:
        print(f"| {fruit:^3} |", end=" ")
    print()
    print("************************")

    if choice[0] == choice[1] == choice[2]:
        bet = bet*2
        balance += bet
        print(f"Congratulations Your Won! {bet}Rs")
        return balance
    
    else:
        print(f"Sorry You lose! {bet}Rs")
        return balance
    
def balance_add(balance):

    amount = (input("Please Write the amount you want to Add (q to Quit) : ")).lower()

    if amount.isdigit():
        amount = int(amount)

        if amount <= 0:
            print("Invalid Amount!")
            return balance , 0
        
        else:
            balance += amount
            return balance , amount
        
    elif amount == "q":
        return balance , "q"
    
    else:
        print("Invalid Amount!")
        return balance , 0
 
def main():

    bet = 0
    balance = 100
    is_running = True

    while is_running:

        menu()

        balance, bet = balance_sys(balance)

        if bet == "q":
            is_running = False

        elif bet == 0:
            continue                                              
        else:
            balance = slot_machine(bet, balance)

        if balance == 0:

            while True:

                balance, amount = balance_add(balance)

                if amount == 0:
                    continue

                elif amount == "q":
                    is_running = False
                    break

                else:
                    break

if __name__ == "__main__":
    main()


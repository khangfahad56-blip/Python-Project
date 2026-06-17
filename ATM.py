# Writing a Program for a Simple ATM for Modify

# starting_menu Function

def starting_menu():
    print("*************************")
    print("Auto Teller Machine (ATM)")
    print("*************************")
    print("1 : Check Balance        ")
    print("2 : Deposit Money        ")
    print("3 : Withdraw Money       ")
    print("4 : Exit Program         ")
    print("*************************")
    print()

# Checking Balances Function

def check_balance(balance):
    print("***********************************")
    print(f"Your Bank Balances  is {balance}Rs")
    print("***********************************")
    print()

# Depositing Money Function

def deposit():

    print        ("************************")
    money =int(input("Write the Amount Money: "))
    print        ("************************") 
    print()
    if money >= 0:
        print("*****************************")
        print(f"You have Deposited {money}Rs")
        print("*****************************")
        print()
        return money
    else:
        print("***********************************")
        print("The amount Should be Greater then 0")
        print("***********************************")
        print()
        return 0


# Withdrawing Money Function

def withdraw(balance):

    print           ("************************")
    money =int(input("Write the Amount Money: "))
    print           ("************************") 
    print()

    if money >= 0 and money <= balance:
        print("****************************")
        print(f"You have Withdraw {money}Rs")
        print("****************************")
        print()
        return money
    else:
        print("*************************************************************")
        print("The amount Should be Greater then 0 and Less then the Balance")
        print("*************************************************************")
        print()
        return 0

# Starting Code

def main():

    balance = 1000

    while True:

        starting_menu()

        option = (input("Choice the Option (1,2,3,4): "))

        if option == "1":
            check_balance(balance)
        
        elif option == "2":
            balance += deposit()

        elif option == "3":
            balance -= withdraw(balance)

        elif option == "4":
                break

        else:
            print("***********************************")    
            print("You have Selected A Invalid Option.")
            print("***********************************") 
            print()

    print("****************************")
    print("Thank you for using the ATM.")
    print("****************************")
    print()

if __name__ == "__main__":
    main()

# # Writing a Program for a Simple ATM

# # Starting meun Function

# def starting_meun():
#     print("*************************")
#     print("Auto Teller Machine (ATM)")
#     print("*************************")
#     print("1 : Check Balance        ")
#     print("2 : Deposit Money        ")
#     print("3 : Withdraw Money       ")
#     print("4 : Exit Program         ")
#     print("*************************")
#     print()

# # Checking Balances Function

# def check_balance(balance):
#     print(f"Your Bank Balances  is {balance}Rs")

# # Depositing Money Function
# def deposit(balance, money):
#     balance += money
#     print(f"You have Deposited {money}Rs")
#     return balance

# # Withdrawing Money Function
# def withdraw(balance, money):
#     balance -= money
#     print(f"You have Withdraw {money}Rs")
#     return balance

# # Initail Value of Balance
# balance = 1000

# # Starting Code
# while True:
#     starting_meun()

#     option = (input("Choice the Option (1,2,3,4): "))

#     if option.isdigit():
#         option = int(option)

#         if option == 1:
#             check_balance(balance)
#             print()

#         elif option == 2:
#             while True:
#                 money = input("Please Write the amount of Money: ")

#                 if money.isdigit():
#                     money = float(money)
#                     balance = deposit(balance, money)
#                     print()
#                     break
#                 else:
#                     print("Please enter valid amount.")

#         elif option == 3:
#             while True:
#                 money = input("Please Write the amount of Money: ")

#                 if money.isdigit():
#                     money = float(money)

#                     if money <= balance:
#                         balance = withdraw(balance, money)
#                         print()
#                         break

#                     elif money > balance:
#                         print("Insufficient balance check")

#                 else:
#                     print("Please enter valid amount.")

#         elif option == 4:
#             print()
#             break

#         else:
#             print("You have Selected A Invalid Option.")

#     else:
#         print("Invalid Option!")

#     print()

# print("Thank you for using the ATM.")

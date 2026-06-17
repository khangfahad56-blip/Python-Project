#Stop Watch

#Shape Maker

# rows = int(input("Write the # of Rows: "))
# columns= int(input("Write the # of Columns: "))
# Symbol = (input("Write the Symbol: "))

# for i in range(rows):
#     for x in range(columns):
#         print(Symbol,end="")
#     print()

#Shopping Cart Programme

# items = []
# prices = []
# total = 0

# item = input("Write the item's name: ")
# price = float(input("Write the item's Prices: "))
# items.append(item)
# prices.append(price)
# ask = input("Are there any more items (Y/N): ")

# while ask.upper() == "Y":
#     item = input("Write the item's name: ")
#     price = float(input("Write the item's Prices: "))
#     items.append(item)
#     prices.append(price)
#     ask = input("Are there any more items (Y/N): ")

# print("-----Your Shopping Contains-----")

# for item in items:
#     print(item, end=" ")

# print()

# for price in prices:
#     total += price

# print(f"Your total is {total:.2f}")

#Number_pad

# num_pad = ((1,2,3)
#            ,(4,5,6)
#            ,(7,8,9)
#            ,("*",0,"#"))

# for row in num_pad:
#     for num in row:
#         print(num , end=" ")
#     print()

# # Write a Programme to Take and Check MCQ:

# questions = [
#     "The speed of sound in air mainly depends on: ",
#     "Which wave can travel through a vacuum?",
#     "The unit of electric current is: ",
#     "Ohm's Law states that: ",
#     "The resistance of a conductor depends on",
# ]

# options = [
#     ["A:Frequency", "B:Amplitude", "C:Temperature", "D:Wavelength"],
#     ["A:Sound wave", "B:Water wave", "C:Light wave" ,"D:Mechanical wave"],
#     ["A:Volt", "B:Ampere", "C:Ohm", "D:Watt"],
#     ["A:V = IR", "B:P = VI", "C:E = mc²","D:F = ma"],
#     ["A:Length", "B:Area", "C:Material", "D:All of these"],
# ]

# answers = [
#     "C",
#     "C",
#     "B",
#     "A",
#     "D",
# ]

# guesses = []
# num_ques = 0
# marks = 0

# for question in questions:
#     print("------------------------------")
#     print(question)
#     for option in options[num_ques]:
#         print(option)
    
#     guess= input("Write the Correct option (A,B,C,D): ").upper()
#     guesses.append(guess)
#     if guess == answers[num_ques]:
#         marks += 1
#         print("Corrent!")
#     else:
#         print("Incorret!")
    
#     num_ques += 1
#     print(marks)

# print("------------------------------")
# print("-----------Result-------------")
# print("------------------------------")
# print("The options you choice")
# for guess in guesses:
#     print(guess, end=" ")
# print()
# print("The correct the option")
# for answer in answers:
#     print(answer, end=" ")

#Write a Program for Concession Stand

# menu = {
#     "Popcorn" : 200 ,
#     "Cola coke" : 100 ,
#     "Chicken pop" : 500 ,
#     "Shawarma" : 300 ,
#     "Burger" : 350 ,
#     "Sandwich" : 250 ,
# }

# print("--------------------------")
# print("     Concession Stand     ")
# print("--------------------------")

# for x , y in menu.items():
#     print(f"{x:12} : {y} Rs")

# totals = []
# price = 0

# while True:
#     food =  input("Write the Item you Want to Buy: ").capitalize()
#     if menu.get(food) is not None:
#         num =  int(input(f"Write the amount of {food} you Want to Buy: "))
#         total = (menu[food])*num
#         totals.append(total)
#         ques = input("Do you Want to Buy More Items (Y/N)?: ").upper()
#         if ques != "Y":
#             break
#     else:
#         print("You have Selected a Invalid Item")

# for x in totals:
#     price += x

# print("--------------------------")
# print(f"Your Total is {price} Rs.")
# print("--------------------------")

# while True:
#     payment = input("Would like to do Payment with Card or Cash: ").capitalize()
#     if payment == "Card":
#         print(f"{price} Rs amount of Money has been transfer for Your bank.")
#         print("Thank you!")
#         break
#     elif payment == "Cash":
#         while True:
#             money = int(input("Please Write the amount of Cash you Paid: "))
#             if money < price:
#                 print("You have Paid not enough money.")
#             elif money > price:
#                 money -= price
#                 print(f"Here is your Changes {money} Rs.")
#                 break
#             elif money == price:
#                 print("Thank You!")
#                 break
#         break
#     else:
#         print("You have selected a invalid method of Payment.")

# Write a Program to Guess a Number

# import random

# low = 1
# high = 100
# num = random.randint(low , high)
# sroce = 0

# while True:
#     guess = input(f"Guess a Number blw {low} and {high}: ")
#     if guess.isdigit():
#         guess = int(guess)
#         if guess > high or guess < low:
#             print("The Number you Guess is out of Range")
#         elif guess ==  num:
#             print(f"You Guessed the Correct Number {num}.")
#             if sroce > 1:
#                 print(f"You Guessed the Number in {sroce} Guesses")
#             elif sroce == 1:
#                 print("You Guessed the Number in One Guess")
#             else:
#                 print("You Guessed the Number in First Try, Weldone")
#                 break
#         elif guess > num:
#             print(f"The Number is Lower then Your Guess of {guess}")
#             sroce +=1
#         elif guess < num:
#             print(f"The Number is Higher then Your Guess of {guess}")
#             sroce +=1
#     else:
#         print("You wrote an Invalid Number.")

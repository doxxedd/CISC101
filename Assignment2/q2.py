"""
# Description: A program that displays the items and their prices listed on K-pop Subsushi's menu, a restaurant Kingston. 
#              The user can choose which item they want. The program will inform them of their choice.
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Sept 24th, 2021
"""
#clears terminal
import os
os.system('cls')


food1 = "K-pop Kimbab"
food2 = "Mayo Tuna Kimbab"
food3 = "Galbi Beef Kimbab"

#displaying the menu items and prices
print("\nWelcome to the K-pop Subsushi's menu!")
print("\n1. " + food1 + " - $6.00")
print("2. " + food2 + " - $8.00")
print("3. "+ food3 + " - $12.00")

#taking in users input and converting to int
menuNumber = int(input("Please enter the menu number corresponding to your choice: "))

#comparison statements for printing the correct menu item
if menuNumber == 1:
    print("\nThank you for choosing a " + food1 + ", it'll be ready soon!")
elif menuNumber == 2:
    print("Thank you for choosing a " + food2 + ", it'll be ready soon!")
elif menuNumber == 3:
    print("Thank you for choosing a " + food3 + ", it'll be ready soon!")
else:
    print("Please restart the program and enter a correct menu number (1,2,3).")
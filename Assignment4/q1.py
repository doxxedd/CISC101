"""
# Description: A program simulating a grocery shop experience
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Oct 8th, 2021
"""

import os
os.system('cls') #clears terminal

def groceryTotal(numItems):
    """
    This function prompts the user for the price of some number of items (given
    by the parameter) and returns the total price for all the items.
    Parameters:  numItems - integer
    Return: a floating point value (2 digits) representing the cost of the items.
    """

    total = 0.0
    for i in range (numItems):
        print("\nWhat is the price of item #", i+1, "? ")
        response = float(input())
        total += response
    
    total = float(format(total, '.2f'))
    return total

def amountOfTax(total):
    """
    This function will return the amount of tax that should be paid on the groceries
    given the total bill amount.  The tax will be at a rate of 13%.
    Parameters:  total - float representing the total amount of the grocery bill.
    Return: a floating point value (2 digits) representing the tax amount.
    """

    taxAmount = total * 0.13
    taxAmount = float(format(taxAmount, '.2f'))
    return taxAmount
    

def totalBill(amount, tax):
    """
    This function will return the total cost of a bill of "amount" plus the tax. 
    Parameters:  amount - float representing the total amount of the grocery bill.
                 tax - float representing the amount of tax to be paid.
    Return: a floating point value (2 digits) representing the total amount with tax added.
    """

    totalBillAmount = amount + tax
    totalBillAmount = float(format(totalBillAmount, '.2f'))
    return totalBillAmount



def greeting():
    """
    This function greets the user and tells them what groceries are available for purchase.
    (Just make up a list of groceries).
    The purpose of this function is just to inform the user of some information.
    Parameters:  None
    Return:  None
    """

    print("""\nHello and welcome to the grocery store!\nThe items available for purchase are listed below:

    Cereal - $3
    Apples - $1
    Orange Juice - $4

    """)

def main():
    """
    The main function controls the program flow.  this is where execution will start.
    It is very common to have a function called main() in a program.
    """
    greeting() #calling greeting method for intro
    
    numItems = input("How many items will you be purchasing today? ")
    while numItems <= "0" or numItems.isdigit() is False or numItems == "0": #requiring a valid input (input > 0 and must be a number)
        numItems = input("Please enter a valid number: ")
    numItems = int(numItems)

    totalItems = groceryTotal(numItems) #saving item amount
    print("The total bill amount is: $" , totalItems) #printing item amount only
    
    taxAmount = amountOfTax(totalItems) #saving tax amount
    print("Tax amount: $" , taxAmount) #printing tax amount only

    totalDue = totalBill(totalItems, taxAmount)
    print("Total amount due: $" , totalDue) #printing total bill

main() #executing main function
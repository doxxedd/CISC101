"""
# Description: A menu driven program that takes user input and does the specified task 
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Oct 1st, 2021
"""

import os
import webbrowser
os.system('cls') #clears terminal

isRunning = True

while isRunning == True:
    print("""
1. Sing happy birthday to you.
2. Calculate percentage of Kingston locals in the class
3. Display a website given a URL
4. Quit\n""")

    menuChoice = input("Please choose an option by inputting the corresponding number: ")

    while menuChoice < "1" or menuChoice > "4" or menuChoice.isdigit() is False or len(menuChoice) != 1: #making sure input is 1-4 and one digit
        menuChoice = input("Your response is not valid. Please choose a valid response '1' '2' '3' '4': ")

    if menuChoice == "1": 
        userName = input("\nEnter your name: \n")
        print("\n\tHappy Birthday to You\n\tHappy Birthday Dear " + userName + " \n\tHappy Birthday to You!\n")

    elif menuChoice == "2":
        numLocal = input("\nHow many students from Kingston are in your class? ")
        while numLocal <= "0" or numLocal.isdigit() is False or numLocal == "0": #requiring a valid input (input > 0 and must be a number)
            numLocal = input("Please enter a valid number: ")
        numLocal = int(numLocal) #converting answer to int for calculations

        numNonLocals = input("How many students from outside of Kingston are in your class? ")
        while numNonLocals <= "0" or numNonLocals.isdigit() is False or numNonLocals == "0": #requiring a valid input (input > 0 and must be a number)
            numNonLocals = input("Please enter a valid number: ")
        numNonLocals = int(numNonLocals) #converting answer to int for calculations

        #local % calculation
        studentTotal = numLocal + numNonLocals
        localPercentage = (numLocal / studentTotal) * 100
        print (str(round(localPercentage,2))+"% of the students in your class are from Kingston.") #rounding answer to 2 decimal values
    elif menuChoice == "3":
        url = input("\nPlease enter the URL of the website to be opened in your default browser: ")
        webbrowser.open(url)
    
    elif menuChoice == "4":
        print("\nThank you for using this program. Have a great day!")
        isRunning = False #stopping the program by changing the boolean value, stopping the while loop
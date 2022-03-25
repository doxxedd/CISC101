"""
# Description: A terminal based adventure game
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Oct 8th, 2021
"""

import os
os.system('cls') #clears terminal

def wakeUp():
    """
    This function marks the start of the game when the player just wakes up. 
    Depending on user's choices, they can end up here.
    Parameter: none
    Return: none
    """

    print("""
Ah, what a beautiful day it is today. Sunny, 19 degrees and no wind.
You look at the clock and realize that you woke up just a bit too late for your first class. 
You can either play a few Call of Duty games on your computer and attend your next class, 
OR pack up your stuff and at least attend half of your first class. 
    """)
    choice = input("Input 'G' for games and 'C' for class: ")
    while (choice != "C") and (choice != "G"):  #accepts only C and G as input
        choice = input("Input not valid. Please choose a valid response ('G' or 'C'): ")

    if choice == "G":
        games()
    elif choice == "C":
        school()

def games():
    """
    This function runs when user chooses to play games after waking up. 
    Parameter: none
    Return: none
    """

    print("""
You chose to play stay home and play Call of Duty on one of the nicest days this month.
Good choice!
I would have done the same. You can watch the recording of that class later anyways.

The reminder that you set to get to your 2nd class in-time goes off.
But you still haven't eaten breakfast and want some McDonald's. 
At the same time, you kind of wanna go back to sleep.
    """)
    choice = input("Input 'M' to get breakfast at McDonald's and 'S' to sleep in: ")
    while (choice != "M") and (choice != "S"): #only accepting M and S
        choice = input("Input not valid. Please choose a valid response ('M' or 'S'): ")

    if choice == "M":
        mcdonalds()
    elif choice == "S":
        print("\nYou go back to sleep for the rest of the day. Mom gets mad.")
        


def school():
    """
    This function is the place school in this adventure game. 
    Depending on user's choices, they can end up here.
    Parameter: none
    Return: none
    """

    print("""
You start packing up in a hurry and get to class with half the class time left. 
Your teacher is surprised that you actually showed up and as they were in middle of
teaching math, they ask you one of the questions on the board.
"Whats 24463*223? You have 10 seconds to answer. "
    """)
    answer = int(input("Type in your answer: "))
    mathSchool(answer) #passing input to function to check calculation


def mathSchool(answer):
    """
    This function checks if math was done correctly
    Depending on user's choices, they can end up here.
    Parameter: answer - int
    Return: none
    """
    x = True
    correct = 24463*223 #5455249 is expected
    if answer == correct:
        x = True
    else:
        x = False

    if x == True:
        print("\nGood job. You got the correct answer. Teacher tells you to go sit down.")
    else: 
        print("\nTeacher mocks you in-front of the class :(")


def mcdonalds():
    """
    This function runs if the user decides to get breakfast after playing games
    Parameter: none
    Return: none
    """
    print("""
Before you leave your house, you decide to order an English Muffin for breakfast from McDonald's.
You remember that it costs $3 + tax.
You are trying to figure out the tax amount to get the money ready before you leave.
How much money are you bringing for the tax only? (13% tax)
    """)
    answer = float(input("Type in your answer with 2 places of decimal: "))
    mcdonaldsMath(answer)

def mcdonaldsMath(answer):
    """
    This function checks if the tax math was done correctly
    Depending on user's choices, they can end up here.
    Parameter: answer - float
    Return: none
    """

    x = True
    correct = 3 * 0.13 #0.39 is expected
    if answer == correct:
        x = True
    else:
        x = False

    if x == True:
        print("\nGoodjob you brought the correct amount of money and left with a fully belly.")
    else:
        print("""
You miscalculated and couldn't buy food because the cashier had 0 change (weird I know)
You left with an empty belly
""")

def main():
    print("\nHello and welcome to the 'Just a normal day' adventure game! Lets begin!")
    wakeUp() #user wakes up and the story begins

main() #executes the main function
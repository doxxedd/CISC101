"""
# Description: This implements a simplified version of Wheel of Fortune. The computer chooses a word
from a list of words and the user guesses letters until they have filled in all the letters 
in the word or have guessed incorrectly 5 times.

# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Oct 29nd, 2021
"""

import random
import os
os.system('cls') #clears terminal


def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the word
    """
    
    validWords = ["generation", "consume", "computing", "residence", "memory", "hosting"]

    #random.randint(0, 5) will generate an integer between 0 and 5 (inclusive)
    #this is then used to select a value from the list validWords.

    return validWords[random.randint(0,5)]

def printStringWithSpaces(word):
    """
    This function prints the word representation (eg: "__r_")
    on the screen with spaces between each underscore/letter
    so that the user can better see how many letters there are.
    Parameter: string
    Return Value:  None
    """

    print(" ".join(word) + "\n\n") #adding spaces between the characters of given word


def convertToUnderscores(word):
    """
    Creates a string consisting of len(word) underscores.
    For example, if word = "cat", function returns "___" (3 underscores)
    Parameter: string
    Return Value: string
    """

    wordUnderscored = ""
    wordUnderscored = '_'*len(word) #replacing the word's charecters with underscores

    return wordUnderscored
    

def updateWord(currentRep, word, letter):
    """
    This function replaces the underscores with the guessed letter.
    Eg.  letter = 'p', word = "stop", currentRep = "s___" --> returns "s__p"
    Paramters:   currentRep, word are strings
                letter is a string, but a single letter.
    Returns:  a string
    """

    newString = ""
    
    for i in range(len(word)): 
        if letter == word[i]: 
            newString += letter #adding the letter if the letter is found in word, to newString
        else:
            newString += currentRep[i] #if letter is not found in the word, adding currentRep  to newString
        
    return newString

    
def updateUsedLetters(usedLetters, letter):
    """
    This function concatenates the guessed letter onto the list of letters
    that have been guessed, returning the result.
    Parameters: string representing the used letters
                string respresenting the current user guess
    Return Value:  string
    """

    usedLetters += letter
    
    return usedLetters

    

def main():
    """
    This implements the user interface for the program.
    """
    usedLetters = "" #no letters guessed yet
    wrongGuesses = 0 #keep track of incorrect guesses

    #the word to guess
    word = chooseWord()

    #although this isn't realistic, we need to see the word for testing
    print("The word to guess is:", word)  

    currentRep = convertToUnderscores(word)

    print(currentRep)

    #continueGame is a flag that will turn to false when the user wins or loses the game.
    continueGame = True
    while continueGame:
        guess = input("Please enter a letter (a-z): ")
        
        #check for valid input
        while not(guess.isalpha()) or len(guess) != 1:
            guess = input("Please enter valid input(a single letter (a-z)):")
            
        guess = guess.lower()

        print("You have guessed the letter:", guess)

        #if statement checking to see if the user's guess is not in the list of already chosen letter
        if guess not in usedLetters:
            usedLetters = updateUsedLetters(usedLetters, guess)
            if guess in word:
                #letter is in the secret word so update the current representation
                currentRep = updateWord(currentRep, word, guess)
                printStringWithSpaces(currentRep)
                if currentRep == word:
                    print("Great job, you guessed the word fully!")
                    continueGame = False #stops game after checking if currentRep is the same as word

            else:
                wrongGuesses += 1
                print("\nThe letter that you guessed is not in the word.")

                #stopping the game after 5 guesses
                if wrongGuesses == 5:
                    print("\nYou have reached the maximum amount of wrong guesses. You lost :(")
                    continueGame = False
            
        else:
            #letter has been guessed already -- update the user
            print("You have already guessed that letter!!!")
            print("Here are the letters you have guessed so far: ")
            printStringWithSpaces(usedLetters)
            
main()
"""
# Description: Bingo game with 5x5 cards. Support for max of 3 players.
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Dec 3rd, 2021
"""

import ssl
import urllib.request
import os
import random as rand

os.system('cls')  # clears terminal
ssl._create_default_https_context = ssl._create_unverified_context  # to resolve ssl error

remaining_words_list = []


def process_webpage(url):
    """Reading the contents of the webpage and putting each words in as an element in a list

    Args:
        url (String): url of website that will be accessed

    Returns:
        list: web contents with each element as a word
    """

    try:
        connection = urllib.request.urlopen(url)  # opening connection to site
        web_content = connection.read().decode('utf-8').strip('\n')  # getting raw data from site
        word_list = web_content.split("\n")  # processing the content in lines
        
        return word_list  # returning the list of words

    except urllib.error.URLError:  # catching the error if url is wrong
        print("URL Error. Re-run the program with a correct URL.")


def win_condition_generator():
    """Function randomly choosing the win condition of the game

    Returns:
        String: stating the win condition
    """
    win_condition_types = ["Four Corners", "Single Line", "Full Card"]

    return win_condition_types[rand.randint(0, len(win_condition_types) - 1)]


def win_condition_met(win_condition, card):
    """Checking if any one has won given card and chosen win condition

    Args:
        win_condition (String): condition of winning 
        card (2d list): list of player

    Returns:
        bool: True if there is a bingo
    """

    if win_condition == "Four Corners":
        
        # checking for 4 corners
        if card[0][0] == "FOUND" and card[4][0] == "FOUND" and card[0][4] == "FOUND" and card[4][4] == "FOUND":
            return True
        else:
            return False
        
    elif win_condition == "Single Line":

        # checks for vertical lines that are FOUND
        for r in range(5):
            l = [False, False, False, False, False]
            for c in range(5):
                if card[c][r] == "FOUND" or (r == 2 and c == 2):
                    l[c] = True
                else:
                    break
            if not False in l:
                return True

        # checks for horizontal lines that are FOUND
        for c in range(5):
            l = [False, False, False, False, False]
            for r in range(5):
                if card[c][r] == "FOUND" or (r == 2 and c == 2):
                    l[r] = True
                else:
                    break
            if not False in l:
                return True

        return False

    elif win_condition == "Full Card":

        # checking all words in card
        for r in card:
            for word in r:
                if word != "FOUND" and word != "FREE":
                    return False

        return True


def generate_card(word_list):
    """Generating a card that has no duplicating cells

    Args:
        word_list (list): list of all words taken from process_webpage()

    Returns:
        2d list: completed bingo card
    """

    list_copy = word_list[:]  # make a copy of the ENTIRE elements in input list
    rand.shuffle(list_copy)  # shuffle the elements in list

    card = []

    for i in range(5):
        card += [[list_copy.pop((i*5)), list_copy.pop((i*5)+1), list_copy.pop((i*5)+2), list_copy.pop((i*5)+3), list_copy.pop((i*5)+4)]]

    card[2][2] = "FREE"  # replacing the middle cell with FREE slot
    
    return card


def display_card(card):
    """Displays the words on a given card

    Args:
        card (String): Bingo card
    """

    max_phrase_len = 0
    for row in card:
        for phrase in row:
            if max_phrase_len < len(phrase):
                max_phrase_len = len(phrase)
    
    max_phrase_len += 2
    
    formatted_card = ""
    for row in card:
        for phrase in row:
            formatted_card += (phrase + (max_phrase_len - len(phrase)) * " ")
        formatted_card += "\n"
    
    return formatted_card
    
    
def get_player_count():
    """Gets player count from user

    Returns:
        int: # of players
    """

    player_count = int(input("\nWelcome to the Bingo game.\nHow many people will be playing? "))
    while player_count > 3 or player_count < 1: 
        player_count = int(input("Please enter a valid player count (1-3): "))

    return player_count


def filling_up_remaining_words_list(word_list):
    """Fills up the remaining_words_list

    Args:
        word_list (list): list of words
    """

    global remaining_words_list
    remaining_words_list = word_list[:]  # make a copy of the ENTIRE elements in input list
    rand.shuffle(remaining_words_list)  # shuffle the elements in list


def phrase_caller():
    """Chooses a random word from list_copy

    Returns:
        String: A unique phrase from list_copy
    """
    
    global remaining_words_list
    chosen_phrase = remaining_words_list.pop(rand.randint(0, len(remaining_words_list)-1))  # pop ensures the returned word will not be called again if method is called

    return chosen_phrase


def check_phrase(card, chosen):
    """Checks a card for a randomly picked phrase

    Args:
        card (2d list): card of a player
        chosen (String): string called as phrase

    Returns:
        boolean: returns true if phrase was in card
    """

    word_found_flag = False

    for i in range(len(card)):
        if word_found_flag:
            break
        
        for j in range(len(card[0])):
            if card[i][j] == chosen:
                card[i][j] = 'FOUND'
                word_found_flag = True
                break
    
    return word_found_flag


def main():
    word_list = process_webpage("https://research.cs.queensu.ca/home/cords2/bingo.txt")
    
    while True:
        
        player_count = get_player_count()
        filling_up_remaining_words_list(word_list)

        match player_count:
            
            case 1:  # one player
                win_condition_1 = win_condition_generator()
                player_1 = input("Input player 1's name: ")
                print()

                card_1 = generate_card(word_list)

                print("Here is the win condition:", win_condition_1, ", good Luck!\n")

                print(f"{player_1}'s card:\n{display_card(card_1)}")

                while win_condition_met(win_condition_1, card_1) == False:  # checking for a valid bingo
                    response = input("Do you wish to see a new phrase? (y/n): ")
                    if response == "y":
                        chosen = phrase_caller()
                        print(f"\nThe chosen phrase is: {chosen}")
                        if check_phrase(card_1, chosen):
                            print(f"The phrase was in {player_1}'s card")
                            print("\n"+display_card(card_1))
                        else:
                            print(f"The phrase was NOT in {player_1}'s card\n")
                    else:
                        print("Well I guess we aren't continuing the game then.")
                
                again = input("Congrats, you have won the game. Do you want to play again? (y/n)")

                if again == "n":
                    print("Thanks for playing!")
                    break  # emulating a do while loop

            case 2:  # two players
                win_condition_2 = win_condition_generator()
                player_1 = input("Input player 1's name: ")
                player_2 = input("Input player 2's name: ")
                print()

                card_1 = generate_card(word_list)
                card_2 = generate_card(word_list)

                print("Here is the win condition:", win_condition_2, ", good Luck!\n")
                print(f"{player_1}'s card:\n{display_card(card_1)}")
                print(f"{player_2}'s card:\n{display_card(card_2)}")

                while True:

                    # prompt
                    response = input(f"Do {player_1} and {player_2} wish to see a new phrase? (y/n): ")
                    if response == "y":
                        chosen = phrase_caller()
                        print(f"\nThe chosen phrase is: {chosen}\n")

                        # checking player 1's card
                        if check_phrase(card_1, chosen):
                            print(f"The phrase was in {player_1}'s card")
                            print("\n"+display_card(card_1))
                        else:
                            print(f"The phrase was NOT in {player_1}'s card\n")
                        
                        # checking player 2's card
                        if check_phrase(card_2, chosen):
                            print(f"The phrase was in {player_2}'s card")
                            print("\n"+display_card(card_2))
                        else:
                            print(f"The phrase was NOT in {player_2}'s card\n")
                    else:
                        print("Well I guess we aren't continuing the game then.")

                    # checking if player 1 won
                    if win_condition_met(win_condition_2, card_1) == True:
                        print(f"Congrats, {player_1} has won the game.")
                        break
                    
                    # checking if player 2 won
                    if win_condition_met(win_condition_2, card_2) == True:
                        print(f"Congrats, {player_2} has won the game.")
                        break    
                        
                    # if both win
                    if win_condition_met(win_condition_2, card_1) == True and win_condition_met(win_condition_2, card_2) == True:
                        print("All players have won the game!")
                        break
                
                again = input("Thanks for playing! Do you want to play again?")
                if again == "n":
                    break  # emulating a do while loop

            case 3:  # three players
                win_condition_3 = win_condition_generator()
                player_1 = input("Input player 1's name: ")
                player_2 = input("Input player 2's name: ")
                player_3 = input("Input player 3's name: ")
                print()

                card_1 = generate_card(word_list)
                card_2 = generate_card(word_list)
                card_3 = generate_card(word_list)

                print("Here is the win condition:", win_condition_3, ", good Luck!\n")
                print(f"{player_1}'s card:\n{display_card(card_1)}")
                print(f"{player_2}'s card:\n{display_card(card_2)}")
                print(f"{player_3}'s card:\n{display_card(card_3)}")

                while True:

                    # prompt
                    response = input(f"Do {player_1} and {player_2} and {player_3} wish to see a new phrase? (y/n): ")
                    if response == "y":
                        chosen = phrase_caller()
                        print(f"\nThe chosen phrase is: {chosen}\n")

                        # checking player 1's card
                        if check_phrase(card_1, chosen):
                            print(f"The phrase was in {player_1}'s card")
                            print("\n"+display_card(card_1))
                        else:
                            print(f"The phrase was NOT in {player_1}'s card\n")
                        
                        # checking player 2's card
                        if check_phrase(card_2, chosen):
                            print(f"The phrase was in {player_2}'s card")
                            print("\n"+display_card(card_2))
                        else:
                            print(f"The phrase was NOT in {player_2}'s card\n")
                        
                        # checking player 3's card
                        if check_phrase(card_3, chosen):
                            print(f"The phrase was in {player_3}'s card")
                            print("\n"+display_card(card_3))
                        else:
                            print(f"The phrase was NOT in {player_3}'s card\n")

                    else:
                        print("Well I guess we aren't continuing the game then.")

                    # checking if player 1 won
                    if win_condition_met(win_condition_3, card_1) == True:
                        print(f"Congrats, {player_1} has won the game.")
                        break
                    
                    # checking if player 2 won
                    if win_condition_met(win_condition_3, card_2) == True:
                        print(f"Congrats, {player_2} has won the game.")
                        break

                    if win_condition_met(win_condition_3, card_3) == True:
                        print(f"Congrats, {player_3} has won the game.")
                        break
                        
                    # if 1 and 2 win
                    if win_condition_met(win_condition_3, card_1) == True and win_condition_met(win_condition_3, card_2) == True:
                        print(f"Congrats, {player_1} and {player_2} have won the game.")
                        break
                    # if 2 and 3 win
                    if win_condition_met(win_condition_3, card_2) == True and win_condition_met(win_condition_3, card_3) == True:
                        print(f"Congrats, {player_2} and {player_3} have won the game.")
                        break
                    # if 1 and 3 win
                    if win_condition_met(win_condition_3, card_1) == True and win_condition_met(win_condition_3, card_3) == True:
                        print(f"Congrats, {player_1} and {player_3} have won the game.")
                        break

                    # if all win
                    if win_condition_met(win_condition_3, card_1) == True and win_condition_met(win_condition_3, card_2) == True and win_condition_met(win_condition_3, card_3) == True:
                        print("All players have won the game!")
                        break
                
                again = input("Thanks for playing! Do you want to play again?")
                if again == "n":
                    break  # emulating a do while loop

            case _:
                print("Invalid command. Please restart the program")


main()

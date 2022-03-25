import ssl
import urllib.request
import os
import re

os.system('cls')  # clears terminal
ssl._create_default_https_context = ssl._create_unverified_context  # to resolve ssl error

def process_webpage(url):

    guest_dict = {}

    try:
        connection = urllib.request.urlopen(url)  # opening connection to site
        web_content = connection.read().decode('utf-8').strip('\n')  # getting raw data from site
        families = web_content.split("\n")  # processing the content in lines

    except urllib.error.URLError:  # catching the error if url is wrong
        print("URL Error")
        return guest_dict
    
    # searching each family for name, email, # adults, # children
    # using regex. Regex tested with regex101.com
    for family in families:
        values = re.search(r'^([A-Za-z]+) ([a-z0-9.]+@[a-z]+\.[a-z]+) (\d+) (\d+)$', family)  

        guest_dict[values.group(1)] = [values.group(2), int(values.group(3)), int(values.group(4))]

    return guest_dict

def number_of_cupcakes(guess_dict):
    """Calculates how many cupcakes we need to bake for the party

    Args:
        guess_dict (dictionary): Name as keys and containing email, # adults and children

    Returns:
        [int]: number of cupcakes that need to be baked for a party
    """

    num_cupcakes = 0

    for key in guess_dict:
        if guess_dict[key][2] != 0:  # looping through to find adults with no children
            num_cupcakes += guess_dict[key][1] * 2 + guess_dict[key][2] * 3  # if they do have children, do the calculations
    
    return num_cupcakes + 10


def not_invited_here(friend_guest_list, guest_dict):

    #printing the people that are in friends_guest_list and not in my guest_list
    for friends_guest in friend_guest_list:
        if not friends_guest in list(guest_dict.keys()):
            print(friends_guest)


def main():

    guest_dict = process_webpage("https://research.cs.queensu.ca/home/cords2/party.txt")
    
    print("\nWelcome to the family party tracker program.")
    print(f"\nHere is the current guest list:\n{guest_dict}")
    print("\nChoose menu option by selecting the number: ")

    is_running = True
    while is_running:
        response = input(
            "\n1. Calculate how many cupcakes to bake"
            "\n2. See who was invited to your friends party but not yours"
            "\n3. Add a new guest/group to the existing list"
            "\n4. Quit the program"
            "\n"
        )

        # running a switch case for the menu driven part of the program
        match response:
            case "1":
                print(f"\nYou need to bake {number_of_cupcakes(guest_dict)} cupcake(s) for the current guest list.")
            
            case "2":
                friends_list = ["Chuck", "James", "Nancy", "Atif", "Phyllis", "Kay", "Zhonglin"]
                print(f"\nHere are the the people that were invited to your friend's party but not yours:")
                not_invited_here(friends_list, guest_dict)
            
            case "3":
                answer = input("\nEnter a new name to be added: ")
                # prompt until the name doesn't exist in the dict
                while answer in guest_dict:
                    answer = input("This user is already in the list, input another: ")
                email = input("Please type in the email for the user: ")
                adult = int(input("How many adult(s)?"))
                child = int(input("How many children?"))
                guest_dict[answer] = [email, adult, child]  # add new guest to dict

            case "4":
                print("\nThank you for using this program. Have a good day!")
                is_running = False
            
            case _:  # if input is not a num (1-4)
                print("\nPlease input a valid response (numbers from 1-4 only)")


main()


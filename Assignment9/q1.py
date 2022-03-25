"""
# Description: Order Simulation Program for Tim Horton's. Orders are taken at Tim Horton's by  
# the "cashiers" and are placed in a queue to be filled one at a time by the "chefs".
# Chefs fill the orders in the order in which they are submitted by the cashiers.
#
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Nov 19th, 2021
"""

import ssl
import urllib.request
import os

os.system('cls')  # clears terminal
ssl._create_default_https_context = ssl._create_unverified_context  # to resolve ssl error

last_order_id = None


def process_webpage(url):
    """From the url, reads the text. Puts the data into 2d list where food items 
    are their own list

    Args:
        url (String): url
    """

    connection = urllib.request.urlopen(url)  # opening connection to site
    web_content = connection.read().decode('utf-8').strip('\n')  # getting raw data from site
    processed_web_content = web_content.split("\n")  # processing the content in lines
    global last_order_id

    queue = []

    # from the site data, putting order ids, foods, and price in format [101, ['Wrap', 'Coffee'], 8.25]
    for order in processed_web_content:
        elements = order.strip().split(' ')
        food_id = elements.pop(0)
        price = elements.pop(-1)
        queue.append([int(food_id), elements, float(price)])
        last_order_id = int(food_id)

    return queue


def take_order(queue):
    """Prompt the user for the food items and the total amount of the order

    Args:
        queue (2d list): list of orders all in a list (each order has a list of foods)

    Returns:
        queue (2d list): updated queue
    """
    print("\nTaking new order...")
    
    global last_order_id
    ordered_items = []
    still_ordering = True

    # allowing user to type in their orders
    while still_ordering:
        item_name = input("Enter item name: ")
        ordered_items.append(item_name)
        if input("Do you want to add another item? (Y/N): \n") != "Y":
            still_ordering = False

    queue.append([queue[-1][0] + 1, ordered_items, float(input("Enter total price:"))])  # adding the new order to queue
    last_order_id = queue[-1][0]  # updating the last_order_id

    return queue


def find_food_in_order(queue):
    """Finding a particular food item in orders after prompting user for food item

    Args:
        queue (2d list): list of orders all in a list (each order has a list of foods)
    """
    print("\nFinding your food in queue...")
    response = input("Specify the food you are searching for: ")
    hits = []  # to be filled with matching IDs

    # iterating through queue to find order IDs that contain the given food
    for order in queue:
        if response in order[1]:
            hits.append(order[0])

    hits_as_string = ', '.join(map(str, hits))  # converting the matching IDs to string 
    print(f'{response}(s) were found in order(s) {hits_as_string}.')


def max_min_prices(queue):
    """Find the IDs of the least and the most expensive totals and print the IDs on the screen.

    Args:
        queue (2d list): list of orders all in a list (each order has a list of foods)
    """
    print("\nFiding the max and min prices...")
    min_order = min(queue, key=lambda x: x[2])  # gets the min order based on the key representing the price index
    max_order = max(queue, key=lambda x: x[2])  # gets the max order based on the key representing the price index
    #https://thispointer.com/python-how-to-get-all-keys-with-maximum-value-in-a-dictionary/

    print(f'The max price in all orders is ${max_order[2]} and is located in order {max_order[0]}')
    print(f'The min price in all orders is ${min_order[2]} and is located in order {min_order[0]}')


def cancel_order(queue):
    """Cancel an order given a particular ID

    Args:
        queue (2d list): list of orders all in a list (each order has a list of foods)
    """
    global last_order_id
    print("Cancelling order...")
    response = int(input("Which order would you like to cancel? (enter ID)"))
    print(f'\nHere is the queue before canceling:{queue}\n')

    for order in queue:
        if order[0] == response:
            queue.remove(order)
        
    last_order_id = max(queue, key=lambda x: x[0])[0]

    print(f'\nHere is the queue after canceling:{queue}')


def unique_foods(queue):
    """Display all the unique food items that are currently in the queue.

    Args:
        queue (2d list): list of orders all in a list (each order has a list of foods)
    """
    unique_food_list = set()
    for order in queue:
        unique_food_list = unique_food_list.union(set(order[1]))
    
    print(f"\nHere are the unique foods: {', '.join(unique_food_list)}")


def complete_order(queue):
    """Complete the next order.

    Args:
        queue (2d list): list of orders all in a list (each order has a list of foods)
    """
    print(f'The order before completion{queue}')
    
    print(queue.pop(0), "popped")
    print(f'The order AFTER completion{queue}')


def main():
    url = "https://www.cs.queensu.ca/home/cords2/timHortons.txt"
    queue = process_webpage(url)
    print("\nWelcome to the Tim Horton's Order Simulator Program or TOSP!\n")

    is_running = True
    while is_running:

        response = int(input(
            "\n1. Submit a new order"
            "\n2. Find all orders with a particular food item"
            "\n3. Find the IDs of the least and the most expensive totals and print the IDs on the screen"
            "\n4. Cancel an order given a particular ID"
            "\n5. Display all the unique food items currently in the queue."
            "\n6. Complete the next order"
            "\nPlease type in your menu choice: "))
    
        match response:
            case 1: 
                queue = take_order(queue)
            case 2:
                find_food_in_order(queue)
            case 3:
                max_min_prices(queue)
            case 4:
                cancel_order(queue)
            case 5:
                unique_foods(queue)
            case 6:
                complete_order(queue)
            case _:
                print("\nThank you for using TOSP!")
                is_running = False 


main()

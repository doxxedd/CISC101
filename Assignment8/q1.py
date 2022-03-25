"""
# Description: This program generates a random essay using words that are found in another piece of text
# NOTE: function and variables names were changed according to the Official Python Documentation
# https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Nov 12th, 2021
"""

import urllib.request
import string
import random
import re
import os
os.system('cls')  # clears terminal

max_word_length = 0


def write_to_file(text):
    """
    It opens a file called "essay.txt" and writes the text string to the file
    
    Parameters: text - String
    Returns: none
    """
    try:
        file = open(r'D:\STUFF\Code\CSIC101\Assignment8\essay.txt', 'w')  # instance for writing in specified directory
        file.write(text)  # replacing everything in the file with given text
        file.close()  # closing instance
    except IOError:
        print("The file essay.txt didn't exist in the specified directory")


def read_webpage(url):
    """
    From the url, reads the text and returns a list where each element is a word in the text
    
    Parameters:  url - String
    Returns: a list of words
    """
    
    try:
        response = urllib.request.urlopen(url)  # opening connection to site
        data = response.read().decode('utf-8')  # reading the information as a single string
        processed_data = data.split()  # putting every word as an element in a list
        return processed_data
    
    except urllib.error.HTTPError:  # catching the error if url is wrong
        print("An error has occurred when trying to open the url.")
        return []  # returns empty list


def remove_punctuation(word_list):
    """
    Stripping the punctuation at the end of each word
    
    Parameters:  wordList - list of words
    Returns: none
    """
    len_list = int(len(word_list))
    for i in range(len_list):
        word_list[i] = re.sub(r'[^\w\s]$', '', word_list[i])  # removing all END punctuations in every word using regex
        

def convert_to_dictionary(word_list):
    """
    Stripping the punctuation at the end of each word
    
    Parameters:  wordList - list of words
    Returns: the word dictionary
    """
    word_dict = {}  # empty dict
    global max_word_length  # global variable currently 0

    for word in word_list:
        
        word = word.lower()  # made all words lowercase
        
        if len(word) > max_word_length: 
            max_word_length = len(word)  # setting the max word length to the current word because it would be bigger
        
        key = f"{word[0]}{len(word)}"  # getting the key of the current word (machine = m8)
        
        if key not in word_dict.keys():  # generates a new key if it didn't exist before
            word_dict[key] = [word]
        else:
            word_dict[key].insert(len(word_dict) - 1, word)  # inserting the current word in the correct key (append)

    return word_dict


def make_paragraph(dictionary_of_words, number_of_words):
    """
    Takes the dictionary of words and creates a paragraph (a string) consisting of number_of_words words

    Parameters: dictionaryOfWords - dict, number_of_words - int
    Returns: paragraph - String
    """

    global max_word_length
    num = 0
    paragraph = ""

    while num < number_of_words:
        # randomizes the keys (letter+number)
        key = random.choice(string.ascii_letters.lower()) + str(random.randint(1, max_word_length))

        # makes a paragraph based on the keys if they were found in the list
        if key in dictionary_of_words:
            num += 1
            chosen_word = random.choice(dictionary_of_words[key])
            paragraph += chosen_word + " "

    return paragraph


def create_essay(dictionary_of_words):
    """
    Takes the dictionary of words and creates a paragraph (a string) consisting of number_of_words words

    Parameters: dictionaryOfWords - dict, number_of_words - int
    Returns: essay - string
    """
 
    essay = ""
    while True:
        if input("Do you want to add a new paragraph? (y/n)") != "y":
            break
        response = int(input('How many word do you want to generate? (int pls): '))
        essay += f"{make_paragraph(dictionary_of_words, response)}\n"  # adds the paragraphs to the essay variable

    return essay


def main():
    url = "https://research.cs.queensu.ca/home/cords2/cs.txt"
    lists = read_webpage(url)
    print(lists)
    remove_punctuation(lists)
    dict_words = convert_to_dictionary(lists)
    write_to_file(create_essay(dict_words))


main()

"""
This program implements a banking application which keeps track of customer names and their
balances in various accounts as well as a listing of the types of credit cards that they
own. Functionality allows a transfer between accounts, provides totals across all customers
of savings, chequing and loan accounts, adds a new customer and checks to see if a customer
owns a particular credit card.

Author:  Wendy Powley
Date: November 2021
"""

import math

def initializeBankInfo():
    """
    This function defines the dictionary that will hold all the information.
    The dictionary is of the format:
        customerID (key): value is a dictionary
        So, for example an entry for customer ID = 70 might look like:
        70: {"name": "Jerry", "savings": 50.00, "chequing": 40.00,
             "loans": 200.00, "credit cards" = ["MC", "Visa"]}
    A dictionary containing all the customers' info is returned.
    Parameters:  None
    Return:  A dictionary
    """


    customer = {
        700: {"name": "Sally", "savings": 1350.00, "chequing": 2555.23, "loan": 25000.00, "credit cards": ["MC", "Visa"]},
        679: {"name": "Said", "savings": 250.53, "loan": 6500.33,"credit cards": ["Amex", "Visa"]},
        320: {"name": "Molly", "savings": 750.95, "chequing": 3774.32},
        400: {"name": "Jia", "savings": 10123.31, "chequing": 6644.32, "credit cards": ["MC"]},
        667: {"name": "Richie", "savings": 1338.88, "chequing": 848.32, "loan": 38843.34, "credit cards": ["MC", "Amex"]},
        888: {"name": "Chelsea","chequing": 3841.01, "loan": 300.03, "credit cards": ["Visa"]},
        329: {"name": "Ally", "savings": 583.33, "chequing": 88.88, "credit cards": ["Visa", "MC"]},
        644: {"name": "Michael", "savings": 777.77, "loan": 843.32, "credit cards": ["Amex"]},
        }
    
    return customer
    


def addNewCustomer(bankInfo, id, name, saveTot, cheqTot, loanTot, cards):
    """
    This function adds a new entry into the dictionary containing the
    information passed as parameters.
    Parameters:  bankInfo - a dictionary
                 id - integer indicating the customer id
                 name - string indicating the customer's name
                 saveTot - float - total for savings account
                 cheqTot - float - total for chequing account
                 loanTot - float - total for loan account
                 cards - list of strings indicating the cards the user owns

                 If any of saveTot, cheqTot or loanTot is None, the customer does not
                 have an account of that type.
    Returns:  Nothing returned, but bankInfo is updated if the customer is new.
    """
    
    
    if id not in bankInfo:
        bankInfo[id] = {}
        bankInfo[id]["name"] = name
        if saveTot != None:
            bankInfo[id]["savings"] = saveTot
        if cheqTot != None:
            bankInfo[id]["chequing"] = cheqTot
        if loanTot != None:
            bankInfo[id]["loan"] = loanTot
        if len(cards) > 0:
            bankInfo[id]["cards"] = cards
    else:
        print("Customer already exists")
        



def moneyTransfer(bankInfo, id, toAccount, fromAccount, amount):
    """
    Moves money from one account to another for a given customer if there
    are sufficient funds.  If sufficient funds are not available, the
    function returns False.      
    Parameters: bankInfo - a dictionary
                id -- integer representing customer id
                toAccount - string (one of "savings" or "chequing")
                fromAccount - string (one of "savings" or "chequing")
                amount - float - amount of money to be transferred
    Returns:  boolean -- True if amount was transferred, False otherwise
    """
   

    if id in bankInfo:
        
        #does the customer have the appropriate accounts?
        if fromAccount in bankInfo[id]:
            if toAccount in bankInfo[id]:
                
                #check that there are sufficient funds
                if bankInfo[id][fromAccount] >= amount:
                    
                    #do the transfer 
                    bankInfo[id][fromAccount] -= amount
                    bankInfo[id][toAccount] += amount

                    #successful
                    return True
    return False

    


def getTotals(bankInfo):
    """
    Sums the totals for savings accounts, chequing accounts and loan accounts
    across all customers.
    
    Parameters:  bikeInfo - a dictionary
    Returns: a list containing 3 floats [sumSavings, sumChequing, sumLoan]
    """
    

    savingsTot = 0
    chequingTot = 0
    loanTot = 0
    for keys in bankInfo:

        #add savings
        if "savings" in bankInfo[keys]:
            savingsTot += bankInfo[keys]["savings"]
            
	   #add chequing
        if "chequing" in bankInfo[keys]:
            chequingTot += bankInfo[keys]["chequing"]

	   #add loans
        if "loan" in bankInfo[keys]:
            loanTot += bankInfo[keys]["loan"] 

           
    return [round(savingsTot, 2), round(chequingTot, 2), round(loanTot, 2)]




def creditCardCheck(bankInfo, id, cardName):
    """
    This function determines whether a customer has a particular type
    of credit card.
    If the customer doesn't exist, return False.
    
    Parameters:  bankInfo - a dictionary 
                 id - integer
                 cardName - string
    Return: True - customer owns this credit card (or customer doesn't exists),
      False otherwise.
    """

    if id in bankInfo:
        if "credit cards" in bankInfo[id]:
            if cardName in bankInfo[id]["credit cards"]:
                return True
    return False



def testCode():
    #Test initialize function
    info = initializeBankInfo()

    #Test adding new values
    addNewCustomer(info, 431, "Summer", 49.32, 1000.01, 2323.00, ["MC", "Visa"])
    addNewCustomer(info, 932, "Steven", None, None, 1800.00, ["Amex"])
    addNewCustomer(info, 333, "Sandy", 33.00, None, 4335.33, [])
    print("Added three new customers, 431, 932, 333")
    print()
    if len(info) == 11:
        print("Correct number of entries in the dictionary -- test succeeded")
    print()
    print(info[431])
    print(info[932])
    print(info[333])
    print()

    #Adding a customer that already exists
    addNewCustomer(info, 320, "Molly", 43.33, 55.33, None, ["MC"])


    #do some transfers
    if moneyTransfer(info, 700, 'savings', 'chequing', 100):
        print("Transferred 100 to Sally's savings account - test successful")
        print("Sally's savings is ", info[700]["savings"], "checking is ", info[700]["chequing"])
        print("Values should be 1450.0 and 2455.2")
    else:
        print("Transfer not successful -- test failed!")
    if moneyTransfer(info, 700, 'savings', 'chequing', 40000):
        print("Testing transfer of too much $$ -- test failed!")
    else:
        print("Testing transfer of too much $$ -- test successful")
    if moneyTransfer(info, 679, 'chequing', 'savings', 40):
        print("Testing transfer with no account - test failed")
    else:
        print("Testing transfer with no account -- test successful!")


    #Get totals
    print(getTotals(info))
    if getTotals(info) == [15357.09, 18652.09, 44986.35]:
        print("Totals test succeeded")
    else:
        print("Totals test failed")
        print("Totals calculated: ", getTotals(info))

    #test for credit card
    if creditCardCheck(info, 320, "MC"):
        print("Test for 320, credit card = MC failed")
    else:
        print("Test for 320, credit card = MC succeeded")

    if creditCardCheck(info, 679, "Visa"):
        print("Test for 679, credit card = Visa succeeded")
    else:
        print("Test for 679, credit card = Visa failed")

    if creditCardCheck(info, 10000, "Visa"):
        print("Test for non-existent id, failed")
    else:
        print("Test for non-existent id, succeeded")


testCode()
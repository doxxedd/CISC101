"""
# Description: Bank of Queens keeps track of its customers and banking accounts, 
# cards and amount of money in each account.

# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Nov 5th, 2021
"""

import os
os.system('cls') #clears terminal


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

    bankInfo = {} #creating an empty dictionary
    
    #entering all customer data 
    bankInfo[700] = {"name": "Sally", "savings": 1350.00, "chequing": 2555.23, "loan": 25000.00, "credit cards": ["MC", "Visa"]}
    bankInfo[679] = {"name": "Said", "savings": 250.53, "loan": 6500.33, "credit cards": ["Amex", "Visa"]}
    bankInfo[320] = {"name": "Molly", "savings": 750.95, "chequing": 3774.32,}
    bankInfo[400] = {"name": "Jia", "savings": 10123.31, "chequing": 6644.32, "credit cards": ["MC"]}
    bankInfo[667] = {"name": "Richie", "savings": 1338.88, "chequing": 848.32, "loan": 38843.34, "credit cards": ["MC", "Amex"]}
    bankInfo[888] = {"name": "Chelsea", "chequing": 3841.01, "loan": 300.03, "credit cards": ["Visa"]}
    bankInfo[329] = {"name": "Ally", "savings": 583.33, "chequing": 88.88, "credit cards": ["Visa", "MC"]}
    bankInfo[644] = {"name": "Michael", "savings": 777.77, "loan": 843.32, "credit cards": ["Amex"]}

    return bankInfo


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
    
    if id in bankInfo:
        print("customer is already in database")
        return
    
    bankInfo[id] = {}
    
    paramToCheck = [name, saveTot, cheqTot, loanTot, cards] #list of params to go through

    for keys in paramToCheck:
        if keys == None or not paramToCheck[4]: #checking if passed on values are None or cards list is empty
            continue
        elif keys == name:
            bankInfo[id]["name"] = keys
        elif keys == cheqTot:
            bankInfo[id]["chequing"] = keys
        elif keys == saveTot:
            bankInfo[id]["savings"] = keys
        elif keys == loanTot:
            bankInfo[id]["loan"] = keys
        elif keys == cards:
            bankInfo[id]["cards"] = keys
    

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

    if id in bankInfo: #check for user existing 
        return False
    if toAccount not in bankInfo[id] or fromAccount not in bankInfo[id]: #check for account of the user existing 
        return False

    realFrom = bankInfo[id][fromAccount]
    realTo = bankInfo[id][toAccount]
    
    realFrom = realFrom - amount #subtracting the money from From account

    if realFrom <= 0: #if not enough money, send money back and false
        realFrom = realFrom + amount 
        return False
    else:
        realTo = realTo + amount #transferring
        
    return True

   
def getTotals(bankInfo):
    """
    Sums the totals for savings accounts, chequing accounts and loan accounts
    across all customers.
    
    Parameters:  bankInfo - a dictionary
    Returns: a list containing 3 floats [sumSavings, sumChequing, sumLoan]
    """
    
    #declaration of ints that will be used in calculations
    sumSavings = 0
    sumChequing = 0
    sumLoan = 0

    for keys in bankInfo:
        for i in bankInfo[keys]:
            if i not in bankInfo[keys]:
                continue
            elif i == "savings":
                sumSavings = sumSavings + bankInfo[keys][i]
            elif i == "chequing":
                sumChequing = sumChequing + bankInfo[keys][i]
            elif i == "loan":
                sumLoan = sumLoan + bankInfo[keys][i]

    total = [round(sumSavings, 2), round(sumChequing, 2), round(sumLoan, 2)]
    return total


def creditCardCheck(bankInfo, id, cardName):
    """
    This function determines whether a customer has a particular type
    of credit card.
    If the customer doesn't exist, return False.
    
    Parameters:  bankInfo - a dictionary 
                 id - integer
                 cardName - string
    Return: True - customer owns this credit card,
      False - customer does not own this credit card (or does not exist).
    """
    if id not in bankInfo: #check for user existing 
        return False
    
    if "credit cards" not in bankInfo[id]: #check if they have any credit cards
        return False

    if cardName in bankInfo[id]["credit cards"]: #check for the given card for a specific id
        return True
    else:
        return False
    

def testCode():
    #Test initialize function
    info = initializeBankInfo()

    #Test adding new values
    addNewCustomer(info, 431, "Summer", 49.32, 1000.01, 2323.00, ["MC", "Visa"])
    addNewCustomer(info, 932, "Steven", None, None, 1800.00, ["Amex"])
    addNewCustomer(info, 333, "Sandy", 33.00, None, 4335.33, [])
    print("\n\nAdded three new customers, 431, 932, 333")
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
    if getTotals(info) == [15357.09, 18652.09, 79945.35]:
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
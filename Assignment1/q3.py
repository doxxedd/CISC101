"""
# Description: A program that converts US dollars to Canadian dollars based on an exchange rate of 1.00 USD = 0.80 CAD
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Sept 17th, 2021
"""

print("\nWelcome USD to CAD converter. \nTodays exchange rate is 1.00 USD = 0.80 CAD.")
enteredUSDAmount = float(input("\nPlease enter the amount in USD to be converted to CAD: "))
convertedCADResult = format((enteredUSDAmount * 0.8 ), '.2f')
convertedCADResult = str(convertedCADResult)
enteredUSDAmount = str(enteredUSDAmount)

print("\n$" + enteredUSDAmount + " USD is $" + convertedCADResult + " CAD.\n")
"""
# Description: A program that calculates the distance between two points that is inputted from the user
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Sept 17th, 2021
"""
import math

print("\nWelcome to the distance between 2 points calculator!\n")
x1 = float(input("Please enter the x coordinate of the first point: "))
y1 = float(input("Please enter the y coordinate of the first point: "))
x2 = float(input("Please enter the x coordinate of the second point: "))
y2 = float(input("Please enter the y coordinate of the second point: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("\nThe distance between the two points entered is " + format(distance, '.4f') + " units. ")
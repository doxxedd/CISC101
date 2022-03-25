"""
# Description: A program asking for 2 numbers, ensuring the second number is greater than the first. Then printing every 6th number as well as number printed
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Oct 1st, 2021
"""

import os
os.system('cls') #clears terminal

print("\nEnter 2 numbers that are positive and make sure the second number is greater than the first one.")
num1 = int(input("\nFirst number: "))
num2 = int(input("Second number: "))

while num1 > num2 or num1 < 0 or num2 < 0:
    print("\nYour responses are not valid. Enter 2 numbers that are positive and make sure the second number is greater than the first one.")
    num1 = int(input("\nFirst number: "))
    num2 = int(input("Second number: "))

counter = 6
xNum = 0
yNum = 0
for i in range(num1, num2):
    if counter == 6:
        print(i)
        counter = 0
        counter += 1
        xNum += 1
    else:
        counter += 1
        if i % 2 == 0 and i % 3 == 0:
            yNum += 1

print(xNum, "numbers were printed by this program and", yNum, "numbers were skipped because they were evenly divisible by 6.")
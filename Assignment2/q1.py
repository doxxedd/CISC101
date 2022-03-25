"""
# Description: A program that checks for satisfaction of several conditions for Queen's Computing program
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Sept 24th, 2021
"""
 
#clears terminal
import os
os.system('cls')

print("\nHello and welcome to Queens!\nThis program will check for conditions for an automatic acceptance and waitlist status into Queens Computing path.\n")

cisc121Grade = input("Please enter your letter grade for CISC 121: ")
cisc121Grade = cisc121Grade.upper()

#prompt for taking cisc 124
cisc124Taken = input("Have you completed and received a credit for CISC 124? (Y/N): ")
cisc124Taken = cisc124Taken.upper()

#if 124 is taken then program will take into consideration 121 and 124's grade based on user response
if cisc124Taken == "Y": 
    cisc124Grade = input("Please enter your letter grade for CISC 124: ")
    cisc124Grade = cisc124Grade.upper()

    gpa = float(input("Please enter your GPA: "))
    #check for valid gpa range
    if (gpa > 4.3) or (gpa < 0):
        print("Invalid GPA range. Restart the program and enter a valid GPA (4.3-0).")
    else:
        if (cisc124Grade or cisc121Grade <= "B") and (gpa >= 2.6):
            print('Congratulation! You are automatically admitted into Queens Computing plan')
        elif (cisc124Grade or cisc121Grade <= "C") and (gpa >= 2.0):
            print('\nYou have been placed onto the pending list.')
        else:
            print('\nUnfortunately, you are not eligible for the computing plan.\nConsider retaking CISC 121/124.')   

#if 124 is not taken, only grade and gpa of 121 is taken into consideration 
elif cisc124Taken == "N":
    gpa = float(input("Please enter your GPA: "))
    #check for valid gpa range
    if (gpa > 4.3) or (gpa < 0):
            print("Invalid GPA range. Restart the program and enter a valid GPA (4.3-0).")
    else:
        if (cisc121Grade <= "B") and (gpa >= 2.6):
            print('Congratulation! You are automatically admitted into Queens Computing plan')
        elif (cisc121Grade <= "C") and (gpa >= 2.0):
            print('\nYou have been placed onto the pending list.')
        else:
            print('\nUnfortunately, you are not eligible for the computing plan.\nConsider retaking CISC 121/124.')

#if user does not enter Y or N
else:
    print('Please restart the program and enter a valid response: Y for yes, N for no.')
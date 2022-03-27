"""
# Description: a program for processing grades of student in a class. Including displaying, showing avg, adding marks etc...
# @Author:  Daniel D.
# @Date:  Oct 22nd, 2021
"""

import os
import re
import numpy as np

os.system('cls') #clears terminal

def printMark(nameList, assignments, name, assignmentNumber):
    """
    Displaying the name and mark of said student on an inputted assignment number
    Parameter: nameList - list containing student names (Strings), assignments - 2D array of integers,
    name (chosen name to search) - String, assignmentNumber - int
    Return: none
    """
    assignmentNumber = int(assignmentNumber)

    if name in nameList and (0 <= assignmentNumber <= 3): #checking for name existing in the list & assignment# (0-3)
        nameIndex = nameList.index(name) #index of searched name
        print(name, "got a mark of", assignments[nameIndex][assignmentNumber], "on assignment #", assignmentNumber + 1)
    elif assignmentNumber > 3 or assignmentNumber < 0: #checking for out of bounds assignment#
        print("Assignment number on index", assignmentNumber ,   "is out of range.")
    elif name not in nameList: #checking for name not existing in the list
        print("No student by that name.", "(" + name + ")" )

    
def averageAssignment(nameList, assignments, assignmentNumber):
    """
    Based on chosen assignment, displays average mark of all students in the database on that assignment
    Parameter: nameList - list containing student names (Strings), assignments - 2D array of integers, 
    assignmentNumber - int
    Return: number with 2 decimals in String format
    """

    assignmentNumber = int(assignmentNumber)
    sumAssignmentMark = 0
    nameListLength = int(len(nameList)) #length of nameList

    if 0 <= assignmentNumber <= 3: #checking for assignment# (0-3)
        for i in range(nameListLength):
            sumAssignmentMark += assignments[i][assignmentNumber] #sum of assignments with the same inputted index
        return str(format(sumAssignmentMark / nameListLength, '.2f')) #average displayed with 2 decimals
    elif assignmentNumber > 3 or assignmentNumber < 0: #returning -999 if assignment# is out of bounds
        return -999
    

def averageMark(nameList, assignments, name):
    """
    Based on chosen name, displays average mark of student in the database i 
    Parameter: nameList - list containing student names (Strings), assignments - 2D array of integers, 
    assignmentNumber - int
    Return: number with 2 decimals in String format or 0 int 
    """

    sumAssignmentMark = 0

    if name in nameList:
        nameIndex = nameList.index(name) #index of searched name
        for i in range(4):
            sumAssignmentMark += assignments[nameIndex][i] #sum of the marks of assignments of inputted name
        return str(format(sumAssignmentMark / 4, '.2f')) #average displayed with 2 decimals
    else:
        return 0

    
def highestAverageMark(nameList, assignments):
    """
    Based on chosen list of marks and names, returns the student with the highest 
    Parameter: nameList - list containing student names (Strings), assignments - 2D array of integers
    Return: empty list or highestNameList - String list
    """

    averages = []
    nameListLength = int(len(nameList)) #length of nameList

    print()
    for i in range(nameListLength):
        averages.append(averageMark(nameList, assignments, nameList[i])) #calculating the average for every student
        print(nameList[i] + "has an average of: " + averages[i] + "%")

    emptyList = []
    if not averages: #returns an empty list if nameList is empty
        return emptyList
    else:
        highestAvg = max(averages) #finds the highest mark
        print("\nThe highest average achieved was: "+ highestAvg + "%")

    averages = list(map(float, averages)) #converts averages to float list
    
    maxValuesIndices = np.argwhere(averages == np.max(averages)) #getting the max value indices - returns 2d list
    flatMaxValueIndices  = []
    
    #flattens the 2d list
    for sublist in maxValuesIndices:
        for item in sublist:
            flatMaxValueIndices.append(item)

    #gets the names of people with highest averages from the list averages 
    flatMaxValueIndicesRange = int(len(flatMaxValueIndices))
    highestNameList = []
    for i in range(flatMaxValueIndicesRange):
        highestNameList.append(nameList[flatMaxValueIndices[i]])

    return highestNameList


def increaseMarks(name, students):
    """
    Given a student's name, increases all assignment marks by 2% which increases their avg by 2%
    Parameters: students - list, name - String
    Return: none
    """
    for i in range(len(students)):
        if students[i][0] == name:
            students[i] = (name, [students[i][1][0] + 2, students[i][1][1] + 2, students[i][1][2] + 2, students[i][1][3] + 2])
    

def addNewStudent(students):
    """
    Prompts for name, and 4 marks, then adds them to the list of student
    Parameters: students - list
    Return: none
    """
    name = input("\nEnter the student name to be added: ")
    for i in range(len(students)):
        while name == students[i][0]: #check if inputted name already exists
            name = input("\nPlease enter a unique name to be added (name already exists): ")
    
    marks = []
    while len(marks) < 4:
        mark = input(f'Input mark #{len(marks) + 1}:') #f making {} a string
        if re.match("^[0-9]$|^[1-9][0-9]?$|^100$", mark): #using regex numbers checking for 0-100 inclusive
            marks.append(mark)
    students.append((name, marks)) #adding the new name and marks to the students list


def main():
    
    print("Hello and welcome to the mark processing program.\n")
    students = [("Jane", [80, 74, 93, 60]), ("Xinrong", [72, 89, 55, 75]), ("Sima", [93, 80, 74, 60])]
    print("\nThe data set is formatted like so: ('Student name', [assignment1Mark, etc...])\nHere it is:\n", students, "\n")

    #splitting the tuple list students to 2 lists, one containing only names, the other, 2D array of marks
    listOfNames = []
    listOfAssignments = []
    for i in students:
        listOfNames.append(i[0])
    for i in students:
        listOfAssignments.append(i[1])

    #using printMark
    printMark(listOfNames, listOfAssignments, "Xinrong", 3)
    printMark(listOfNames, listOfAssignments, "Sima", 0)
    printMark(listOfNames, listOfAssignments, "Colleen", 1)
    printMark(listOfNames, listOfAssignments, "Xinrong", 6)

    #using assignmentAverage
    firstAssignmentIndex = 0
    assignmentAverage = averageAssignment(listOfNames, listOfAssignments, firstAssignmentIndex)
    if assignmentAverage == -999:
        print("\nInvalid assignment number. Valid (0-3)")
    else:
        print("\nThe class average on assignment number", firstAssignmentIndex + 1, "is", assignmentAverage + "%")
    
    #using averageMark
    nameAvg = 'Jane'
    janeStudentAverage = averageMark(listOfNames, listOfAssignments, nameAvg)
    if janeStudentAverage == 0:
        print("\nThe name " + nameAvg + " does not exist in the database.")
    else:
        print("\n" + nameAvg + "'s average mark on all 4 assignments is: " + janeStudentAverage + "%")
    
    nameAvg2 = 'Bob'
    fakeStudentAverage = averageMark(listOfNames, listOfAssignments, nameAvg2)
    if fakeStudentAverage == 0:
        print("\nThe name " + nameAvg2 + " does not exist in the database.")
    else:
        print("\n" + nameAvg + "'s average mark on all 4 assignments is: " + fakeStudentAverage + "%")

    #using highestAverageMark
    highNameList = highestAverageMark(listOfNames, listOfAssignments)
    highNameListNumIndexes = int(len(highNameList))
    
    if highNameListNumIndexes == 1: #if only 1 student has the highest average
        print("The student with that high average is", highNameList[0])
    else: #if multiple students have the same highest average
        print("The students with that high averages are:" , ', '.join(highNameList))
    
    #using addNewStudent
    addNewStudent(students)
    print(f'\nHere is the updated dataset: (new student added)\n{students}')
    
    #using increaseMarks
    increaseMarks('Jane', students)
    print(f'\nHere is the updated dataset: (all of Jane\'s marks were increased by 2%)\n{students}')


main()

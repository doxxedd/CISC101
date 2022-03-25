"""
# Description: Exam
# @Author:  Daniel Dinari
# @Student Number: 20288573
# @Date:  Dec 15th, 2021
"""

import random

def residence_string_to_dict(res_string):
    res_elements = res_string.split(' ')

    res_dict_to_return = {}  # empty dict

    # filling up dict
    for i in range(0, len(res_elements), 4):
        res_dict_to_return[res_elements[i]] = [int(res_elements[i + 1]), int(res_elements[i + 2]), int(res_elements[i + 3])]

    return res_dict_to_return


def residence_validator(res_dict):

    res_names = []

    # checking for each condition
    for res_name in res_dict.keys():
        if (
            res_dict[res_name][0] > res_dict[res_name][1] or
            res_dict[res_name][2] > 500 or
            res_dict[res_name][0] + res_dict[res_name][1] * 2 > res_dict[res_name][2] or
            'e' in res_name
        ):
            res_names.append(res_name)  # if any of the conditions are met then add to list

    return res_names


def student_assigner(res_list, student_list):
    """Assigning random students to random res buildings

    Args:
        res_list (list of Strings): res buildings
        student_list (list of Strings): students
    Returns:
        List of tuples: formatted like [(students, res)]
    """

    assigned_students = [] 
    for student in student_list:
        assigned_students.append(tuple([student, random.choice(res_list)]))

    return assigned_students


def add_students():
    students = []

    while True:
        name = input("Enter student name:")

        if name == "stop":  # break condition
            break

        students.append(name)

    return students


def display_students(students):
    """displaying the results 

    Args:
        students (list of tuples): [(students, res)]
    """

    for student in students:
        print(f"{student[0]}: {student[1]}")



def main():

    res_dict = residence_string_to_dict("Adelaide 230 15 250 Brant 100 175 445 Leonard 150 300 669 Gordon 400 200 732")
    student_list = add_students()

    assigned_students = student_assigner(list(res_dict.keys()), student_list)  # getting the students assigned to a res

    display_students(assigned_students)


main()

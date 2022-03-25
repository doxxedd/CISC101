import random

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


residences = ["Adelaide", "Chown", "Gordon"]
students = ["Charlie", "Rachael", "Sam", "Samson"]
print(student_assigner(residences, students))

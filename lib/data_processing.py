# data_processing.py

def format_student_data(student):
    """
    Formats student tuple into a readable string.
    """
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(student_generator):
    """
    Takes a generator of students and prints
    formatted student strings.
    """
    for student in student_generator:
        print(format_student_data(student))
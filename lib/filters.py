# filters.py

def filter_students_by_major(students, major):
    """
    Returns a list of students matching the given major.
    """
    return [student for student in students if student[2] == major]
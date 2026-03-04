# set_operations.py

def unique_majors(students):
    """
    Returns a set of unique majors from the student list.
    """
    return {student[2] for student in students}
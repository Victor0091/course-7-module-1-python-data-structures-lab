# data_generator.py

# Sample student data
students = [
    (1, "Alice Johnson", "Science"),
    (2, "Bob Smith", "Mathematics"),
    (3, "Charlie Brown", "Mathematics"),
    (4, "Diana Prince", "History"),
    (5, "Ethan Hunt", "Science"),
]
# data_generator.py

# Sample student data
students = [
    (1, "Alice Johnson", "Computer Science"),
    (2, "Bob Smith", "Mathematics"),
    (3, "Charlie Brown", "Computer Science"),
    (4, "Diana Prince", "History"),
    (5, "Ethan Hunt", "Science"),
]


def student_generator(students, subject):
    """
    Generator that yields students matching a specific subject.
    """
    for student in students:
        if student[2] == subject:
            yield student

def student_generator(students, subject):
    """
    Generator that yields students matching a specific subject.
    
    :param students: list of student tuples (id, name, subject)
    :param subject: subject to filter by
    :yield: tuple (id, name, subject)
    """
    for student in students:
        if student[2] == subject:
            yield student
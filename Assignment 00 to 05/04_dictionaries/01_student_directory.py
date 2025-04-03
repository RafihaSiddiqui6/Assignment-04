# A student directory program that stores names and IDs, prints the directory, and allows ID lookup by name.
def read_student_directory():
    """
    Ask the user for student names and ID numbers to store in a directory (dictionary).
    Returns the student directory.
    """
    student_directory = {}  # Create empty directory

    while True:
        name = input("Student Name: ").strip()
        if name == "":
            break
        if not name.isalpha():
            print("Invalid input! Name should contain only letters.")
            continue
        
        student_id = input("Student ID: ").strip()
        if not student_id.isdigit():
            print("Invalid input! ID should contain only numbers.")
            continue
        
        student_directory[name] = student_id

    return student_directory

def print_student_directory(student_directory):
    """
    Prints out all the student names and their ID numbers.
    """
    for name, student_id in student_directory.items():
        print(f"{name} -> {student_id}")

def lookup_student_id(student_directory):
    """
    Allow the user to lookup student IDs in the directory
    by entering a student name.
    """
    while True:
        name = input("Enter student name to lookup: ").strip()
        if name == "":
            break
        if name not in student_directory:
            print(f"{name} is not in the directory.")
        else:
            print(f"Student ID: {student_directory[name]}")

def main():
    student_directory = read_student_directory()
    print_student_directory(student_directory)
    lookup_student_id(student_directory)

if __name__ == '__main__':
    main()

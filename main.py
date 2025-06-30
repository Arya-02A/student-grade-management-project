student_grades = {}

def add_student():
    name = input("Enter the name of the student : ")
    grade = int(input("Enter student's grades : "))
    student_grades[name] = grade
    print(f"Added {name} with {grade} grade.")

def update_student():
    name = input("Enter the name of the student to update : ")
    grade = int(input(f"Enter {name}'s updated grades : "))
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {grade} as {name}'s grade.")
    else:
        print(f"{name} not found in the data.")

def delete_student():
    name = input("Enter the name of the student to delete : ")
    if name in student_grades:
        grades = student_grades[name]
        del student_grades[name]
        print(f"Deleted student {name} with {grades} grades.")
    else:
        print(f"{name} not found in the data.")

def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No student found or added in the data.")

running = True
while running:
    
    print("| STUDENT GRADE MANAGEMENT SYSTEM |")
    print("1. Add student.")
    print("2. Update student.")
    print("3. Delete student.")
    print("4. Display all students.")
    print("5. Exit.")

    command = int(input("Enter the number of the command : "))

    if command == 1:
        add_student()

    elif command == 2:
        update_student()

    elif command == 3:
        delete_student()

    elif command == 4:
        display_all_students()

    else:
        running = False

studentDetails = {
    'Tom': 'A',
    'Jerry': 'B'
}

while True:

    print("\nStudent Grade Management")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add new student and grade: ")
        name = input("Enter new student name: ")
        grade = input("Enter grade: ")
        studentDetails[name] = grade

    elif choice == "2":
        name = input("Enter student name to update grade: ")
        if name in studentDetails:
            grade = input("Enter new grade: ")
            studentDetails[name] = grade
            print(f"{name}'s grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

    print("studentDetails: \n", studentDetails)

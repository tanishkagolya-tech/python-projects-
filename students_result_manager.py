student = {}

while True:
    print("\n===== Student Result Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Search Student")
    print("5. Update Marks")
    print("6. Delete Student")
    print("7. Find Topper")
    print("8. Average Marks")
    print("9. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} added successfully!")

    # View Students
    elif choice == "2":
        if not student:
            print("No students found!")
        else:
            print("\nStudent Records:")
            for name, marks in student.items():
                print(f"{name} : {marks}")

    # Check Result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 40:
                grade = "D"
            else:
                grade = "Fail"

            print(f"Marks : {marks}")
            print(f"Grade : {grade}")

            if marks >= 40:
                print("Result : Pass")
            else:
                print("Result : Fail")
        else:
            print("Student not found!")

    # Search Student
    elif choice == "4":
        name = input("Enter student name: ")

        if name in student:
            print(f"{name} scored {student[name]} marks.")
        else:
            print("Student not found!")

    # Update Marks
    elif choice == "5":
        name = input("Enter student name: ")

        if name in student:
            new_marks = int(input("Enter new marks: "))
            student[name] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    # Delete Student
    elif choice == "6":
        name = input("Enter student name: ")

        if name in student:
            del student[name]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # Find Topper
    elif choice == "7":
        if student:
            topper = max(student, key=student.get)
            print(f"Topper : {topper}")
            print(f"Marks : {student[topper]}")
        else:
            print("No students found!")

    # Average Marks
    elif choice == "8":
        if student:
            avg = sum(student.values()) / len(student)
            print(f"Average Marks : {avg:.2f}")
        else:
            print("No students found!")

    # Exit
    elif choice == "9":
        print("Exiting Student Manager...")
        break

    else:
        print("Invalid choice! Please try again.")
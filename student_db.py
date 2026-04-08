print("Student Database System")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        print("Student added successfully!")
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("--------------------")
    elif choice == "3":
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("\nStudent Found:")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                found = True
                break

        if not found:
            print("Student not found.")
    elif choice == "4":
        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
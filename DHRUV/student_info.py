students = []


def student_info():

    while True:

        print("\n----- STUDENT INFORMATION -----")

        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Search Student")
        print("6. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            course = input("Enter Course: ")
            semester = input("Enter Semester: ")
            phone = input("Enter Phone Number: ")

            data = [
                student_id,
                name,
                age,
                gender,
                course,
                semester,
                phone
            ]

            students.append(data)

            print("Student details added successfully.")

        elif choice == 2:

            if len(students) == 0:

                print("No student records available.")

            else:

                for data in students:

                    print("\nStudent ID:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Gender:", data[3])
                    print("Course:", data[4])
                    print("Semester:", data[5])
                    print("Phone:", data[6])

        elif choice == 3:

            student_id = int(
                input("Enter Student ID to update: ")
            )

            found = False

            for data in students:

                if data[0] == student_id:

                    data[1] = input("Enter New Name: ")
                    data[2] = int(input("Enter New Age: "))
                    data[3] = input("Enter New Gender: ")
                    data[4] = input("Enter New Course: ")
                    data[5] = input("Enter New Semester: ")
                    data[6] = input("Enter New Phone Number: ")

                    print("Student information updated.")

                    found = True

                    break

            if not found:

                print("No student found with that ID.")

        elif choice == 4:

            student_id = int(
                input("Enter Student ID to delete: ")
            )

            found = False

            for data in students:

                if data[0] == student_id:

                    students.remove(data)

                    print("Student record deleted.")

                    found = True

                    break

            if not found:

                print("No student found with that ID.")

        elif choice == 5:

            student_id = int(
                input("Enter Student ID to search: ")
            )

            found = False

            for data in students:

                if data[0] == student_id:

                    print("\nStudent Found")
                    print("-------------------------")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Gender:", data[3])
                    print("Course:", data[4])
                    print("Semester:", data[5])
                    print("Phone:", data[6])

                    found = True

                    break

            if not found:

                print("Student not found.")

        elif choice == 6:

            break

        else:

            print("Invalid choice.")
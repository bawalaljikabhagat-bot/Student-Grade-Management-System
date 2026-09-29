teachers = []


def teacher_info():

    while True:

        print("\n----- TEACHER INFORMATION -----")

        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            teacher_id = int(
                input("Enter Teacher ID: ")
            )

            name = input(
                "Enter Teacher Name: "
            )

            subject = input(
                "Enter Subject: "
            )

            department = input(
                "Enter Department: "
            )

            phone = input(
                "Enter Phone Number: "
            )

            data = [
                teacher_id,
                name,
                subject,
                department,
                phone
            ]

            teachers.append(data)

            print("Teacher details added.")

        elif choice == 2:

            if len(teachers) == 0:

                print("No teacher records.")

            else:

                for data in teachers:

                    print("\nTeacher ID:", data[0])
                    print("Teacher Name:", data[1])
                    print("Subject:", data[2])
                    print("Department:", data[3])
                    print("Phone:", data[4])

        elif choice == 3:

            teacher_id = int(
                input("Enter Teacher ID to update: ")
            )

            found = False

            for data in teachers:

                if data[0] == teacher_id:

                    data[1] = input(
                        "Enter New Teacher Name: "
                    )

                    data[2] = input(
                        "Enter New Subject: "
                    )

                    data[3] = input(
                        "Enter New Department: "
                    )

                    data[4] = input(
                        "Enter New Phone Number: "
                    )

                    print("Teacher details updated.")

                    found = True

                    break

            if not found:

                print("Teacher not found.")

        elif choice == 4:

            teacher_id = int(
                input("Enter Teacher ID to delete: ")
            )

            found = False

            for data in teachers:

                if data[0] == teacher_id:

                    teachers.remove(data)

                    print("Teacher removed.")

                    found = True

                    break

            if not found:

                print("Teacher not found.")

        elif choice == 5:

            break

        else:

            print("Invalid choice.")
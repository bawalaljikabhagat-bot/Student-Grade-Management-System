subjects = []


def subject_info():

    while True:

        print("\n----- SUBJECT INFORMATION -----")

        print("1. Insert Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            subject_id = int(input("Enter Subject ID: "))
            name = input("Enter Subject Name: ")
            code = input("Enter Subject Code: ")
            credits = int(input("Enter Credits: "))
            teacher = input("Enter Teacher Name: ")

            data = [
                subject_id,
                name,
                code,
                credits,
                teacher
            ]

            subjects.append(data)

            print("Subject added successfully.")

        elif choice == 2:

            if len(subjects) == 0:

                print("No subjects available.")

            else:

                for data in subjects:

                    print("\nSubject ID:", data[0])
                    print("Subject Name:", data[1])
                    print("Subject Code:", data[2])
                    print("Credits:", data[3])
                    print("Teacher:", data[4])

        elif choice == 3:

            subject_id = int(
                input("Enter Subject ID to update: ")
            )

            found = False

            for data in subjects:

                if data[0] == subject_id:

                    data[1] = input("Enter New Subject Name: ")
                    data[2] = input("Enter New Subject Code: ")
                    data[3] = int(input("Enter New Credits: "))
                    data[4] = input("Enter New Teacher Name: ")

                    print("Subject information updated.")

                    found = True

                    break

            if not found:

                print("No subject found with that ID.")

        elif choice == 4:

            subject_id = int(
                input("Enter Subject ID to delete: ")
            )

            found = False

            for data in subjects:

                if data[0] == subject_id:

                    subjects.remove(data)

                    print("Subject deleted.")

                    found = True

                    break

            if not found:

                print("No subject found with that ID.")

        elif choice == 5:

            break

        else:

            print("Invalid choice.")
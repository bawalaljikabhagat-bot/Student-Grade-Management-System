marks = []


def marks_info():

    while True:

        print("\n----- MARKS MANAGEMENT -----")

        print("1. Enter Marks")
        print("2. View Marks")
        print("3. Update Marks")
        print("4. Delete Marks")
        print("5. Calculate Total")
        print("6. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            student_id = int(input("Enter Student ID: "))
            student_name = input("Enter Student Name: ")
            subject = input("Enter Subject Name: ")

            internal = float(
                input("Enter Internal Marks: ")
            )

            midterm = float(
                input("Enter Mid-Term Marks: ")
            )

            final = float(
                input("Enter Final Exam Marks: ")
            )

            total = internal + midterm + final

            data = [
                student_id,
                student_name,
                subject,
                internal,
                midterm,
                final,
                total
            ]

            marks.append(data)

            print("Marks entered successfully.")
            print("Total Marks:", total)

        elif choice == 2:

            if len(marks) == 0:

                print("No marks records available.")

            else:

                for data in marks:

                    print("\nStudent ID:", data[0])
                    print("Student Name:", data[1])
                    print("Subject:", data[2])
                    print("Internal Marks:", data[3])
                    print("Mid-Term Marks:", data[4])
                    print("Final Exam Marks:", data[5])
                    print("Total:", data[6])

        elif choice == 3:

            student_id = int(
                input("Enter Student ID to update: ")
            )

            subject = input(
                "Enter Subject Name: "
            )

            found = False

            for data in marks:

                if (
                    data[0] == student_id
                    and data[2].lower() == subject.lower()
                ):

                    data[3] = float(
                        input("Enter New Internal Marks: ")
                    )

                    data[4] = float(
                        input("Enter New Mid-Term Marks: ")
                    )

                    data[5] = float(
                        input("Enter New Final Exam Marks: ")
                    )

                    data[6] = (
                        data[3]
                        + data[4]
                        + data[5]
                    )

                    print("Marks updated.")

                    found = True

                    break

            if not found:

                print("Marks record not found.")

        elif choice == 4:

            student_id = int(
                input("Enter Student ID: ")
            )

            subject = input(
                "Enter Subject Name: "
            )

            found = False

            for data in marks:

                if (
                    data[0] == student_id
                    and data[2].lower() == subject.lower()
                ):

                    marks.remove(data)

                    print("Marks record deleted.")

                    found = True

                    break

            if not found:

                print("Marks record not found.")

        elif choice == 5:

            student_id = int(
                input("Enter Student ID: ")
            )

            total = 0
            found = False

            for data in marks:

                if data[0] == student_id:

                    total = total + data[6]

                    found = True

            if found:

                print(
                    "Total marks of student:",
                    total
                )

            else:

                print("No marks found for this student.")

        elif choice == 6:

            break

        else:

            print("Invalid choice.")
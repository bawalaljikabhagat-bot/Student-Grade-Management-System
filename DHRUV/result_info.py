results = []


def result_info():

    while True:

        print("\n----- RESULT MANAGEMENT -----")

        print("1. Enter Result")
        print("2. View Results")
        print("3. Update Result")
        print("4. Delete Result")
        print("5. Check Pass or Fail")
        print("6. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            student_id = int(
                input("Enter Student ID: ")
            )

            name = input(
                "Enter Student Name: "
            )

            subject = input(
                "Enter Subject: "
            )

            marks_obtained = float(
                input("Enter Marks Obtained: ")
            )

            maximum_marks = float(
                input("Enter Maximum Marks: ")
            )

            percentage = (
                marks_obtained /
                maximum_marks
            ) * 100

            if percentage >= 40:

                status = "Pass"

            else:

                status = "Fail"

            data = [
                student_id,
                name,
                subject,
                marks_obtained,
                maximum_marks,
                percentage,
                status
            ]

            results.append(data)

            print("Result entered successfully.")

        elif choice == 2:

            if len(results) == 0:

                print("No result records.")

            else:

                for data in results:

                    print("\nStudent ID:", data[0])
                    print("Student Name:", data[1])
                    print("Subject:", data[2])
                    print(
                        "Marks Obtained:",
                        data[3]
                    )
                    print(
                        "Maximum Marks:",
                        data[4]
                    )
                    print(
                        "Percentage:",
                        round(data[5], 2)
                    )
                    print("Status:", data[6])

        elif choice == 3:

            student_id = int(
                input("Enter Student ID: ")
            )

            subject = input(
                "Enter Subject: "
            )

            found = False

            for data in results:

                if (
                    data[0] == student_id
                    and data[2].lower() == subject.lower()
                ):

                    data[1] = input(
                        "Enter New Student Name: "
                    )

                    data[3] = float(
                        input("Enter New Marks: ")
                    )

                    data[4] = float(
                        input("Enter Maximum Marks: ")
                    )

                    data[5] = (
                        data[3] / data[4]
                    ) * 100

                    if data[5] >= 40:

                        data[6] = "Pass"

                    else:

                        data[6] = "Fail"

                    print("Result updated.")

                    found = True

                    break

            if not found:

                print("Result not found.")

        elif choice == 4:

            student_id = int(
                input("Enter Student ID: ")
            )

            subject = input(
                "Enter Subject: "
            )

            found = False

            for data in results:

                if (
                    data[0] == student_id
                    and data[2].lower() == subject.lower()
                ):

                    results.remove(data)

                    print("Result deleted.")

                    found = True

                    break

            if not found:

                print("Result not found.")

        elif choice == 5:

            student_id = int(
                input("Enter Student ID: ")
            )

            found = False

            for data in results:

                if data[0] == student_id:

                    print(
                        data[2],
                        "->",
                        data[6]
                    )

                    found = True

            if not found:

                print("No result found.")

        elif choice == 6:

            break

        else:

            print("Invalid choice.")
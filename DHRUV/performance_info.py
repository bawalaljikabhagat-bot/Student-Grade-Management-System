performance = []


def performance_info():

    while True:

        print("\n----- PERFORMANCE ANALYSIS -----")

        print("1. Add Performance")
        print("2. View Performance")
        print("3. Update Performance")
        print("4. Delete Performance")
        print("5. Check Performance Level")
        print("6. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            student_id = int(
                input("Enter Student ID: ")
            )

            name = input(
                "Enter Student Name: "
            )

            average_marks = float(
                input("Enter Average Marks: ")
            )

            attendance = float(
                input("Enter Attendance Percentage: ")
            )

            assignment_marks = float(
                input("Enter Assignment Average: ")
            )

            overall = (
                average_marks * 0.60
                +
                attendance * 0.20
                +
                assignment_marks * 0.20
            )

            data = [
                student_id,
                name,
                average_marks,
                attendance,
                assignment_marks,
                overall
            ]

            performance.append(data)

            print("Performance details added.")

        elif choice == 2:

            if len(performance) == 0:

                print("No performance records.")

            else:

                for data in performance:

                    print("\nStudent ID:", data[0])
                    print("Student Name:", data[1])
                    print(
                        "Average Marks:",
                        data[2]
                    )
                    print(
                        "Attendance:",
                        data[3]
                    )
                    print(
                        "Assignment Average:",
                        data[4]
                    )
                    print(
                        "Overall Performance:",
                        round(data[5], 2)
                    )

        elif choice == 3:

            student_id = int(
                input("Enter Student ID: ")
            )

            found = False

            for data in performance:

                if data[0] == student_id:

                    data[1] = input(
                        "Enter New Student Name: "
                    )

                    data[2] = float(
                        input("Enter New Average Marks: ")
                    )

                    data[3] = float(
                        input("Enter New Attendance: ")
                    )

                    data[4] = float(
                        input(
                            "Enter New Assignment Average: "
                        )
                    )

                    data[5] = (
                        data[2] * 0.60
                        +
                        data[3] * 0.20
                        +
                        data[4] * 0.20
                    )

                    print("Performance updated.")

                    found = True

                    break

            if not found:

                print("Performance record not found.")

        elif choice == 4:

            student_id = int(
                input("Enter Student ID to delete: ")
            )

            found = False

            for data in performance:

                if data[0] == student_id:

                    performance.remove(data)

                    print("Performance record deleted.")

                    found = True

                    break

            if not found:

                print("Performance record not found.")

        elif choice == 5:

            student_id = int(
                input("Enter Student ID: ")
            )

            found = False

            for data in performance:

                if data[0] == student_id:

                    score = data[5]

                    print(
                        "\nOverall Score:",
                        round(score, 2)
                    )

                    if score >= 85:

                        print(
                            "Performance Level: Excellent"
                        )

                    elif score >= 70:

                        print(
                            "Performance Level: Very Good"
                        )

                    elif score >= 55:

                        print(
                            "Performance Level: Good"
                        )

                    elif score >= 40:

                        print(
                            "Performance Level: Needs Improvement"
                        )

                    else:

                        print(
                            "Performance Level: Poor"
                        )

                    found = True

                    break

            if not found:

                print("Student performance not found.")

        elif choice == 6:

            break

        else:

            print("Invalid choice.")
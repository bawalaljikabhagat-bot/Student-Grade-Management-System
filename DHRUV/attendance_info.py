attendance = []


def attendance_info():

    while True:

        print("\n----- ATTENDANCE MANAGEMENT -----")

        print("1. Insert Attendance")
        print("2. View Attendance")
        print("3. Update Attendance")
        print("4. Delete Attendance")
        print("5. Check Attendance")
        print("6. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            student_id = int(
                input("Enter Student ID: ")
            )

            name = input(
                "Enter Student Name: "
            )

            total_classes = int(
                input("Enter Total Classes: ")
            )

            attended = int(
                input("Enter Classes Attended: ")
            )

            if attended > total_classes:

                print(
                    "Attended classes cannot be greater "
                    "than total classes."
                )

                continue

            percentage = (
                attended / total_classes
            ) * 100

            data = [
                student_id,
                name,
                total_classes,
                attended,
                percentage
            ]

            attendance.append(data)

            print("Attendance added successfully.")

        elif choice == 2:

            if len(attendance) == 0:

                print("No attendance records.")

            else:

                for data in attendance:

                    print("\nStudent ID:", data[0])
                    print("Student Name:", data[1])
                    print("Total Classes:", data[2])
                    print("Classes Attended:", data[3])
                    print(
                        "Attendance Percentage:",
                        round(data[4], 2)
                    )

        elif choice == 3:

            student_id = int(
                input("Enter Student ID to update: ")
            )

            found = False

            for data in attendance:

                if data[0] == student_id:

                    data[1] = input(
                        "Enter New Student Name: "
                    )

                    data[2] = int(
                        input("Enter Total Classes: ")
                    )

                    data[3] = int(
                        input("Enter Classes Attended: ")
                    )

                    if data[3] > data[2]:

                        print("Invalid attendance.")
                        continue

                    data[4] = (
                        data[3] / data[2]
                    ) * 100

                    print("Attendance updated.")

                    found = True

                    break

            if not found:

                print("Attendance record not found.")

        elif choice == 4:

            student_id = int(
                input("Enter Student ID to delete: ")
            )

            found = False

            for data in attendance:

                if data[0] == student_id:

                    attendance.remove(data)

                    print("Attendance record deleted.")

                    found = True

                    break

            if not found:

                print("Attendance record not found.")

        elif choice == 5:

            student_id = int(
                input("Enter Student ID: ")
            )

            found = False

            for data in attendance:

                if data[0] == student_id:

                    print(
                        "Attendance:",
                        round(data[4], 2),
                        "%"
                    )

                    if data[4] >= 75:

                        print(
                            "Attendance status: Good"
                        )

                    else:

                        print(
                            "Attendance status: Low"
                        )

                    found = True

                    break

            if not found:

                print("Student attendance not found.")

        elif choice == 6:

            break

        else:

            print("Invalid choice.")
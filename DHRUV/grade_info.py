grades = []


def calculate_grade(percentage):

    if percentage >= 90:

        return "A+"

    elif percentage >= 80:

        return "A"

    elif percentage >= 70:

        return "B+"

    elif percentage >= 60:

        return "B"

    elif percentage >= 50:

        return "C"

    elif percentage >= 40:

        return "D"

    else:

        return "F"


def grade_info():

    while True:

        print("\n----- GRADE MANAGEMENT -----")

        print("1. Calculate Grade")
        print("2. View Grades")
        print("3. Update Grade")
        print("4. Delete Grade")
        print("5. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            student_id = int(
                input("Enter Student ID: ")
            )

            name = input(
                "Enter Student Name: "
            )

            percentage = float(
                input("Enter Percentage: ")
            )

            grade = calculate_grade(
                percentage
            )

            data = [
                student_id,
                name,
                percentage,
                grade
            ]

            grades.append(data)

            print("\nGrade calculated successfully.")
            print("Percentage:", percentage)
            print("Grade:", grade)

        elif choice == 2:

            if len(grades) == 0:

                print("No grade records available.")

            else:

                for data in grades:

                    print("\nStudent ID:", data[0])
                    print("Student Name:", data[1])
                    print("Percentage:", data[2])
                    print("Grade:", data[3])

        elif choice == 3:

            student_id = int(
                input("Enter Student ID to update: ")
            )

            found = False

            for data in grades:

                if data[0] == student_id:

                    data[1] = input(
                        "Enter New Student Name: "
                    )

                    data[2] = float(
                        input("Enter New Percentage: ")
                    )

                    data[3] = calculate_grade(
                        data[2]
                    )

                    print("Grade information updated.")

                    found = True

                    break

            if not found:

                print("Student grade not found.")

        elif choice == 4:

            student_id = int(
                input("Enter Student ID to delete: ")
            )

            found = False

            for data in grades:

                if data[0] == student_id:

                    grades.remove(data)

                    print("Grade record deleted.")

                    found = True

                    break

            if not found:

                print("Student grade not found.")

        elif choice == 5:

            break

        else:

            print("Invalid choice.")
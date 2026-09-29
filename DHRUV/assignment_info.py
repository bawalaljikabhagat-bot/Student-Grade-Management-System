assignments = []
def assignment_info():
    while True:
        print("\n----- ASSIGNMENT MANAGEMENT -----")
        print("1. Insert Assignment")
        print("2. View Assignments")
        print("3. Update Assignment")
        print("4. Delete Assignment")
        print("5. Check Submission")
        print("6. Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            assignment_id = int(
                input("Enter Assignment ID: ")
            )
            student_id = int(
                input("Enter Student ID: ")
            )
            student_name = input(
                "Enter Student Name: "
            )
            subject = input(
                "Enter Subject: "
            )
            title = input(
                "Enter Assignment Title: "
            )
            marks = float(
                input("Enter Assignment Marks: ")
            )
            status = input(
                "Enter Submission Status: "
            )
            data = [
                assignment_id,
                student_id,
                student_name,
                subject,
                title,
                marks,
                status
            ]
            assignments.append(data)
            print("Assignment added successfully.")
        elif choice == 2:
            if len(assignments) == 0:
                print("No assignments available.")
            else:
                for data in assignments:
                    print("\nAssignment ID:", data[0])
                    print("Student ID:", data[1])
                    print("Student Name:", data[2])
                    print("Subject:", data[3])
                    print("Assignment:", data[4])
                    print("Marks:", data[5])
                    print("Status:", data[6])
        elif choice == 3:
            assignment_id = int(
                input("Enter Assignment ID: ")
            )
            found = False
            for data in assignments:
                if data[0] == assignment_id:
                    data[1] = int(
                        input("Enter New Student ID: ")
                    )
                    data[2] = input(
                        "Enter New Student Name: "
                    )
                    data[3] = input(
                        "Enter New Subject: "
                    )
                    data[4] = input(
                        "Enter New Assignment Title: "
                    )
                    data[5] = float(
                        input("Enter New Marks: ")
                    )
                    data[6] = input(
                        "Enter New Status: "
                    )
                    print("Assignment updated.")
                    found = True
                    break
            if not found:
                print("Assignment not found.")
        elif choice == 4:
            assignment_id = int(
                input("Enter Assignment ID to delete: ")
            )
            found = False
            for data in assignments:
                if data[0] == assignment_id:
                    assignments.remove(data)
                    print("Assignment deleted.")
                    found = True
                    break
            if not found:
                print("Assignment not found.")
        elif choice == 5:
            assignment_id = int(
                input("Enter Assignment ID: ")
            )
            found = False
            for data in assignments:
                if data[0] == assignment_id:
                    print(
                        "Submission Status:",
                        data[6]
                    )
                    found = True
                    break
            if not found:
                print("Assignment not found.")
        elif choice == 6:
            break
        else:
            print("Invalid choice.")
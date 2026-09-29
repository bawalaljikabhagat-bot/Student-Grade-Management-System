print("=" * 70)
print("             WELCOME TO STUDENT GRADE MANAGEMENT")
print("                         SYSTEM")
print("=" * 70)
print("This system is made to manage student academic records.")
print("It can be used to store student details, marks, grades,")
print("attendance, assignments and overall performance.")
print("\nModules available:")
print("✦ Student Information")
print("✦ Subject Information")
print("✦ Marks Management")
print("✦ Grade Management")
print("✦ Attendance")
print("✦ Teacher Information")
print("✦ Result Management")
print("✦ Assignment Management")
print("✦ Performance Analysis")
from student_info import *
from subject_info import *
from marks_info import *
from grade_info import *
from attendance_info import *
from teacher_info import *
from result_info import *
from assignment_info import *
from performance_info import *
while True:
    print("\n" + "=" * 70)
    print("              STUDENT MANAGEMENT DASHBOARD")
    print("=" * 70)
    print("1. Student Information")
    print("2. Subject Information")
    print("3. Marks Management")
    print("4. Grade Management")
    print("5. Attendance")
    print("6. Teacher Information")
    print("7. Result Management")
    print("8. Assignment Management")
    print("9. Performance Analysis")
    print("=" * 70)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        student_info()
    elif choice == 2:
        subject_info()
    elif choice == 3:
        marks_info()
    elif choice == 4:
        grade_info()
    elif choice == 5:
        attendance_info()
    elif choice == 6:
        teacher_info()
    elif choice == 7:
        result_info()
    elif choice == 8:
        assignment_info()
    elif choice == 9:
          performance_info()
    else:
        print("Invalid choice. Please select from 1 to 9.")
    print("\nDo you want to return to the dashboard?")
    answer = input("Enter Yes or No: ")
    if answer.lower() == "no":
        print("\n" + "=" * 70)
        print("Thank you for using Student Grade Management System.")
        print("Have a great day!")
        print("Developed by: Varinder Aggarwal")
        print("=" * 70)
        break
    elif answer.lower() == "yes":
        continue
    else:
        print("\nSorry, I did not understand that.")
        print("Program is closing.")
        break
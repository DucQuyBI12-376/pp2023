# Define Directory
students = {}
course = {}
marks = {}
# ----------------------------- #
# Input number of student
##  Define Function to input students info
def input_students():
    NumofStudent = int(input("Input Number Of Student: "))
# Input Id, name, DOB
    for i in range(1, NumofStudent):
        student_id = input("Enter Student ID: ")
        student_name = input("Enter the student name: ")
        student_DoB = input("Enter the student DoB: ")
        students [student_id] = {'name': student_name, 'dob': student_DoB}
        return student_id, student_name, student_DoB
# Input number of course
##  Define Function to input course info
def input_course():
    NumofCourse = int(input("Input Number Of Course: "))
# Input course info
    for k in range(NumofCourse):
        course_id = input("Input Course ID: ")
        course_name = input("Input Course Name: ")
        course[course_id] = {'Name': course_name}
        return course_id, course_name
# Select course
##  Define Function to select course, input marks
def input_marks():
    course_id = input("Select a course ID: ")
    if course_id not in course:
        print("Invalid Course ID, please try again")
        return course_id
    for student_id in students:
        mark = int(input(f"Enter the mark for {students[student_id]['name']}: "))
    if student_id not in marks:
        marks[student_id] = {}
    marks[student_id][course_id] = mark
# Define function to list courses
def list_courses():
    for course_id in course:
        print(f"{course_id}: {course[course_id]['name']}" + "\n")
        print(" ------------------------------ \n")

# Define function to list students
def list_students():
    for student_id in students:
        print(f"{student_id}: {students[student_id]['name']}" + "\n")
        print(" ------------------------------ \n")

# Define function to show marks for a given course
def show_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in course:
        print("Invalid course ID")
        return
    for student_id in students:
        if student_id in marks and course_id in marks[student_id]:
            print(f"{students[student_id]['name']}: {marks[student_id][course_id]}")
        else:
            print(f"{students[student_id]['name']}: N/A")
            
while True:
        print(" --------------------- \n")
        print("1. Add students")
        print("2. Add courses")
        print("3. Add marks")
        print("4. View students")
        print("5. View courses")
        print("6. View marks")
        print("7. Quit")  
        choice = input("Enter your choice: ")
        if choice == "1":
            input_students()
        elif choice == "2":
            input_course()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks()
        elif choice == "7":
            break
        else:
            print("Invalid choice, Choose again")
    
    

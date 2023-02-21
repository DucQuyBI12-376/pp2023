# Define Directory
students = {}
course = {}
marks = {}
# Define menu
def display_menu():
    print("1. Add students")
    print("2. Add courses")
    print("3. Add marks")
    print("4. View students")
    print("5. View courses")
    print("6. View marks")
    print("7. Quit")
# ----------------------------- #
# Input number of student
##  Define Function to input students info
def input_students():
    NumofStudent = int(input("Input Number Of Student: "))
# Input Id, name, DOB
    for i in range(NumofStudent):
        student_id = input("Enter Student ID: ")
        student_name = input("Enter the student name: ")
        student_DoB = input("Enter the student DoB: ")
        students [student_id] = {'name': student_name, 'dob': student_DoB} 
# Input number of course
##  Define Function to input course info
def input_course():
    NumofCourse = int(input("Input Number Of Course: "))
# Input course info
    for k in range(NumofCourse):
        course_id = input("Input Course ID: ")
        course_name = input("Input Course Name: ")
        course[course_id] = {'Name': course_name}
# Select course
##  Define Function to select course, input marks
def input_marks():
    course_id = input("Select a course ID: ")
    if course_id not in course:
        print("Invalid Course ID, please try again")
        return course_id
    for student_id in students:
        mark = int(input(f"Enter the mark for {students[student_id]['name']}: "))
        
def view_students():
    

def view_course():
    

def view_marks():
    




    while True:
        display_menu()
 
        choice = input("Enter your choice: ")
        while choice in range(1,7):
            if choice == '1':
                input_students()
            elif choice == '2':
                input_course()
            elif choice == '3':
                input_marks()
            elif choice == '4':
                view_students()
            elif choice == '5':
                view_course()
            elif choice == '6':
                view_marks()
            else:
                break
        else:
            print("Error, Try again: ")
            break
        
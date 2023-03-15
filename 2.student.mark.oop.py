#BI12-476 Nguyen Tran Duc Quy
# ------------------------------------------------- #
# Add a students class
class Student:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
        self.courses = {}
        # Input name, id, DoB, and courses that students are in

    def add_course(self, course):
        self.courses[course.id] = course

    def add_mark(self, course_id, mark):
        self.courses[course_id].marks[self.id] = mark

    def get_marks(self, course_id):
        return self.courses[course_id].marks.get(self.id)

    def __str__(self):
        return f"Student Name: {self.name}\nStudent ID: {self.id}\nDate of Birth: {self.dob}"
    # Function to print students

# Add a Courses class
class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.marks = {}
    # Input name, id, and marks for each student in the course

    def __str__(self):
        return f"Course Name: {self.name}\nCourse ID: {self.id}"
    # Function to print courses 

# Main function
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
    # Set an array for the students and courses

    def add_student(self, name, id, dob):
        student = Student(name, id, dob)
        self.students[id] = student

    def add_course(self, name, id):
        course = Course(name, id)
        self.courses[id] = course

    def add_mark(self):
        course_id = input("Enter the course ID: ")
        course = self.courses[course_id]
        if course is None:
            print("Course not found!")
            return
        student_id = input("Enter the student ID: ")
        student = self.students[student_id]
        if student is None:
            print("Student not found!")
            return
        mark = input("Enter the mark: ")
        course.marks[student_id] = mark
        print("Mark added successfully!")
# View Course, Students and Marks
    def view_students(self):
        print("List of students:")
        for student in self.students.values():
            print(student)

    def view_courses(self):
        print("List of courses:")
        for course in self.courses.values():
            print(course)

    def view_marks(self):
        while True:
            course_id = input("Enter the course ID to view marks (or 'q' to exit): ")
            if course_id == 'q':
                break
            elif course_id not in self.courses:
                print("Invalid course ID!")
                continue

            course = self.courses[course_id]
            print(f"Marks for course '{course.name}':")
            for student_id, mark in course.marks.items():
                student = self.students[student_id]
                print(f" - {student.name}: {mark}")

# Function to enter Students and Courses
if __name__ == '__main__':
    system = StudentManagementSystem()

    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        name = input(f"Enter name for student {i+1}: ")
        id = input(f"Enter ID for student {i+1}: ")
        dob = input(f"Enter date of birth (DD/MM/YYYY) for student {i+1}: ")
        system.add_student(name, id, dob)

    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        name = input(f"Enter name for course {i+1}: ")
        id = input(f"Enter ID for course {i+1}: ")
        system.add_course(name, id)
        
# Main table to add and view marks,  students, courses.
while True:
        print("1. Add marks\n2. View students\n3. View courses\n4. View marks\n5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            system.add_mark()
        elif choice == '2':
            system.view_students()
        elif choice == '3':
            system.view_courses()
        elif choice == '4':
            system.view_marks()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")


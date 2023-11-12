import logging

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def __str__(self):
        return f"Classroom {self.name}"

    def add_student(self, student):
        self.students.append(student)
        logging.info(f"Student {student.id} has been enrolled in {self.name}.")

    def schedule_assignment(self, assignment):
        self.assignments.append(assignment)
        logging.info(f"Assignment for {self.name} has been scheduled.")

    def submit_assignment(self, student_id, assignment_details):
        student = next((s for s in self.students if s.id == student_id), None)
        if student:
            logging.info(f"Assignment submitted by Student {student_id} in {self.name}.")
        else:
            logging.error(f"Student with ID {student_id} not found in {self.name}.")

class Student:
    student_count = 0

    def __init__(self):
        Student.student_count += 1
        self.id = Student.student_count

class Assignment:
    def __init__(self, details):
        self.details = details

def add_classroom(classrooms, class_name):
    new_classroom = Classroom(class_name)
    classrooms.append(new_classroom)
    logging.info(f"Classroom {class_name} has been created.")

def add_student(classrooms, student_id, class_name):
    classroom = find_classroom(classrooms, class_name)
    if classroom:
        student = Student()
        classroom.add_student(student)
    else:
        logging.error(f"Classroom {class_name} not found.")

def schedule_assignment(classrooms, class_name, assignment_details):
    classroom = find_classroom(classrooms, class_name)
    if classroom:
        assignment = Assignment(assignment_details)
        classroom.schedule_assignment(assignment)
    else:
        logging.error(f"Classroom {class_name} not found.")

def submit_assignment(classrooms, student_id, class_name, assignment_details):
    classroom = find_classroom(classrooms, class_name)
    if classroom:
        classroom.submit_assignment(student_id, assignment_details)
    else:
        logging.error(f"Classroom {class_name} not found.")

def find_classroom(classrooms, class_name):
    for classroom in classrooms:
        if classroom.name == class_name:
            return classroom
    return None

def main():
    logging.basicConfig(filename='virtual_classroom.log', level=logging.INFO)

    classrooms = []

    while True:
        print("\nOptions:")
        print("1. Add Classroom")
        print("2. Add Student")
        print("3. Schedule Assignment")
        print("4. Submit Assignment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            class_name = input("Enter the class name: ")
            add_classroom(classrooms, class_name)
        elif choice == "2":
            student_id = int(input("Enter the student ID: "))
            class_name = input("Enter the class name: ")
            add_student(classrooms, student_id, class_name)
        elif choice == "3":
            class_name = input("Enter the class name: ")
            assignment_details = input("Enter the assignment details: ")
            schedule_assignment(classrooms, class_name, assignment_details)
        elif choice == "4":
            student_id = int(input("Enter the student ID: "))
            class_name = input("Enter the class name: ")
            assignment_details = input("Enter the assignment details: ")
            submit_assignment(classrooms, student_id, class_name, assignment_details)
        elif choice == "5":
            print("Exiting the Virtual Classroom Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

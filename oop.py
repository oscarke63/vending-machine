class Student:
    def __init__(self, name, age, student_id, grades):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = grades

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(data):
        return Student(data['name'], data['age'], data['student_id'], data['grades'])


students = []


def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    student_id = input("Enter student ID: ")
    grades = input("Enter grades (comma-separated): ").split(",")
    student = Student(name, age, student_id, grades)
    students.append(student)
    print("Student added successfully.")


def view_students():
    if not students:
        print("No students found.")
    for student in students:
        print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grades: {student.grades}")


def search_student():
    student_id = input("Enter student ID to search: ")
    for student in students:
        if student.student_id == student_id:
            print(f"Found: {student.name}, Age: {student.age}, Grades: {student.grades}")
            return
    print("Student not found.")


def update_student():
    student_id = input("Enter student ID to update: ")
    for student in students:
        if student.student_id == student_id:
            student.name = input("Enter new name: ")
            student.age = input("Enter new age: ")
            student.grades = input("Enter new grades (comma-separated): ").split(",")
            print("Student updated.")
            return
    print("Student not found.")


def save_to_file():
    with open("students.json", "w") as f:
        json.dump([s.to_dict() for s in students], f)
    print("Data saved to file.")


def load_from_file():
    global students
    try:
        with open("students.json", "r") as f:
            data = json.load(f)
            students = [Student.from_dict(d) for d in data]
            print("Data loaded from file.")
    except FileNotFoundError:
        print("No saved data found.")


def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            save_to_file()
        elif choice == '6':
            load_from_file()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
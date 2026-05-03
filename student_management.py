"""Student Management System - CLI Based."""

students = {}


def add_student():
    """Add a new student to the system."""
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if student_id in students:
        print(f"Student with ID '{student_id}' already exists.")
        return
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    age_input = input("Enter Age: ").strip()
    try:
        age = int(age_input)
        if age <= 0:
            raise ValueError
    except ValueError:
        print("Age must be a positive integer.")
        return
    grade = input("Enter Grade: ").strip()
    students[student_id] = {"name": name, "age": age, "grade": grade}
    print(f"Student '{name}' added successfully.")


def view_students():
    """Display all students in the system."""
    if not students:
        print("No students found.")
        return
    print("\n{:<10} {:<20} {:<5} {:<10}".format("ID", "Name", "Age", "Grade"))
    print("-" * 47)
    for student_id, info in students.items():
        print(
            "{:<10} {:<20} {:<5} {:<10}".format(
                student_id, info["name"], info["age"], info["grade"]
            )
        )
    print()


def update_student():
    """Update details of an existing student."""
    student_id = input("Enter Student ID to update: ").strip()
    if student_id not in students:
        print(f"Student with ID '{student_id}' not found.")
        return
    info = students[student_id]
    print(f"Current Name: {info['name']}  Age: {info['age']}  Grade: {info['grade']}")
    name = input("Enter new Name (leave blank to keep current): ").strip()
    age = input("Enter new Age (leave blank to keep current): ").strip()
    grade = input("Enter new Grade (leave blank to keep current): ").strip()
    if name:
        info["name"] = name
    if age:
        try:
            age = int(age)
            if age <= 0:
                raise ValueError
            info["age"] = age
        except ValueError:
            print("Invalid age; keeping current value.")
    if grade:
        info["grade"] = grade
    print("Student details updated successfully.")


def delete_student():
    """Remove a student from the system."""
    student_id = input("Enter Student ID to delete: ").strip()
    if student_id not in students:
        print(f"Student with ID '{student_id}' not found.")
        return
    name = students.pop(student_id)["name"]
    print(f"Student '{name}' deleted successfully.")


def main():
    """Run the Student Management System menu loop."""
    menu = (
        "\n--- Student Management System ---\n"
        "1. Add Student\n"
        "2. View All Students\n"
        "3. Update Student\n"
        "4. Delete Student\n"
        "5. Exit\n"
        "Enter your choice: "
    )
    actions = {
        "1": add_student,
        "2": view_students,
        "3": update_student,
        "4": delete_student,
    }
    while True:
        choice = input(menu).strip()
        if choice == "5":
            print("Exiting the system. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

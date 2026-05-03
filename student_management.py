"""Student Management System - CLI Based."""

import json
import os

DATA_FILE = "students_data.json"

students = {}


# ── Persistence ────────────────────────────────────────────────────────────────

def load_data():
    """Load student records from the JSON data file."""
    global students
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                students = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: '{DATA_FILE}' is corrupt. Starting with an empty record set.")
            students = {}
        except OSError as e:
            print(f"Warning: Could not read '{DATA_FILE}': {e}. Starting with an empty record set.")
            students = {}


def save_data():
    """Persist student records to the JSON data file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(students, f, indent=4)
    except OSError as e:
        print(f"Warning: Could not save data to '{DATA_FILE}': {e}")


# ── Helpers ────────────────────────────────────────────────────────────────────

def _print_table(subset):
    """Print a formatted table for a dict subset of students."""
    print("\n{:<10} {:<25} {:<5} {:<10}".format("ID", "Name", "Age", "Grade"))
    print("-" * 52)
    for student_id, info in subset.items():
        print(
            "{:<10} {:<25} {:<5} {:<10}".format(
                student_id, info["name"], info["age"], info["grade"]
            )
        )
    print()


# ── Core operations ────────────────────────────────────────────────────────────

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
    save_data()
    print(f"✔  Student '{name}' added successfully.")


def view_students():
    """Display all students in the system."""
    if not students:
        print("No students found.")
        return
    _print_table(students)


def search_student():
    """Search for a student by ID or name (case-insensitive partial match)."""
    query = input("Enter Student ID or Name to search: ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return
    results = {
        sid: info
        for sid, info in students.items()
        if query in sid.lower() or query in info["name"].lower()
    }
    if not results:
        print("No matching students found.")
        return
    print(f"\n{len(results)} result(s) found:")
    _print_table(results)


def update_student():
    """Update details of an existing student."""
    student_id = input("Enter Student ID to update: ").strip()
    if student_id not in students:
        print(f"Student with ID '{student_id}' not found.")
        return
    info = students[student_id]
    print(f"Current  →  Name: {info['name']}  |  Age: {info['age']}  |  Grade: {info['grade']}")
    name = input("Enter new Name  (leave blank to keep current): ").strip()
    age = input("Enter new Age   (leave blank to keep current): ").strip()
    grade = input("Enter new Grade (leave blank to keep current): ").strip()
    if name:
        info["name"] = name
    if age:
        try:
            age_val = int(age)
            if age_val <= 0:
                raise ValueError
            info["age"] = age_val
        except ValueError:
            print("Invalid age; keeping current value.")
    if grade:
        info["grade"] = grade
    save_data()
    print("✔  Student details updated successfully.")


def delete_student():
    """Remove a student from the system."""
    student_id = input("Enter Student ID to delete: ").strip()
    if student_id not in students:
        print(f"Student with ID '{student_id}' not found.")
        return
    name = students.pop(student_id)["name"]
    save_data()
    print(f"✔  Student '{name}' deleted successfully.")


def show_statistics():
    """Display summary statistics about the student records."""
    total = len(students)
    if total == 0:
        print("No students found.")
        return
    ages = [info["age"] for info in students.values()]
    avg_age = sum(ages) / total
    grade_counts = {}
    for info in students.values():
        grade_counts[info["grade"]] = grade_counts.get(info["grade"], 0) + 1

    print("\n========== Statistics ==========")
    print(f"  Total students : {total}")
    print(f"  Average age    : {avg_age:.1f}")
    print(f"  Youngest       : {min(ages)}")
    print(f"  Oldest         : {max(ages)}")
    print("\n  Students per grade:")
    for grade, count in sorted(grade_counts.items()):
        print(f"    {grade:<12} : {count}")
    print("=================================\n")


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    """Run the Student Management System menu loop."""
    load_data()
    menu = (
        "\n╔══════════════════════════════════╗\n"
        "║   Student Management System      ║\n"
        "╠══════════════════════════════════╣\n"
        "║  1. Add Student                  ║\n"
        "║  2. View All Students            ║\n"
        "║  3. Search Student               ║\n"
        "║  4. Update Student               ║\n"
        "║  5. Delete Student               ║\n"
        "║  6. Statistics                   ║\n"
        "║  7. Exit                         ║\n"
        "╚══════════════════════════════════╝\n"
        "Enter your choice: "
    )
    actions = {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
        "6": show_statistics,
    }
    while True:
        choice = input(menu).strip()
        if choice == "7":
            print("Exiting the system. Goodbye! 👋")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

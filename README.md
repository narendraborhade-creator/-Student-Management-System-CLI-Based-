# 🎓 Student Management System — CLI Based

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)

A clean, menu-driven **Student Management System** built with Python.  
Manage student records right from your terminal — add, view, search, update, delete, and analyse, with automatic **JSON persistence** so your data survives between sessions.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Add Student** | Register a new student with ID, name, age, and grade |
| 2 | **View All Students** | Display every record in a formatted table |
| 3 | **Search Student** | Find students by ID or name (partial, case-insensitive) |
| 4 | **Update Student** | Edit any field of an existing record |
| 5 | **Delete Student** | Remove a student record permanently |
| 6 | **Statistics** | Show total count, average age, youngest/oldest, and students per grade |
| 7 | **Data Persistence** | Records are auto-saved to `students_data.json` |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Storage:** JSON file (`students_data.json`)
- **Interface:** Command-Line Interface (CLI)
- **Libraries:** `json`, `os` (standard library only — no external dependencies)

---

## 📁 Project Structure

```
Student-Management-System-CLI-Based/
├── student_management.py   # Main application
├── students_data.json      # Auto-generated data file (created on first run)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed ([Download](https://www.python.org/downloads/))

### Run the App

```bash
git clone https://github.com/narendraborhade-creator/-Student-Management-System-CLI-Based-.git
cd -Student-Management-System-CLI-Based-
python student_management.py
```

---

## 🖥️ Demo

```
╔══════════════════════════════════╗
║   Student Management System      ║
╠══════════════════════════════════╣
║  1. Add Student                  ║
║  2. View All Students            ║
║  3. Search Student               ║
║  4. Update Student               ║
║  5. Delete Student               ║
║  6. Statistics                   ║
║  7. Exit                         ║
╚══════════════════════════════════╝
Enter your choice: 1

Enter Student ID: 01
Enter Name: Narendra Borhade
Enter Age: 23
Enter Grade: MCA
✔  Student 'Narendra Borhade' added successfully.

Enter your choice: 2

ID         Name                      Age   Grade
----------------------------------------------------
01         Narendra Borhade          23    MCA

Enter your choice: 6

========== Statistics ==========
  Total students : 1
  Average age    : 23.0
  Youngest       : 23
  Oldest         : 23

  Students per grade:
    MCA          : 1
=================================

Enter your choice: 7
Exiting the system. Goodbye! 👋
```

---

## 📌 Key Concepts Demonstrated

- **CRUD Operations** (Create, Read, Update, Delete)
- **File I/O** — reading and writing JSON for data persistence
- **Input Validation** — empty-field checks, type enforcement for age
- **Modular Design** — each operation is an independent, reusable function
- **Formatted CLI Output** — tabular display with aligned columns
- **Dictionary-based Data Modelling** — efficient in-memory record management

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome!  
Feel free to fork the repo and open a pull request.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👨‍💻 Author

**Narendra Borhade**  
🔗 [GitHub](https://github.com/narendraborhade-creator) • [LinkedIn](https://www.linkedin.com/in/narendra-borhade)

---

> _"The best way to learn programming is to build real projects."_ 🚀

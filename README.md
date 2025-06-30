##🎓 Student Grade Management System
- A simple Python console-based application to manage student grades. It allows users to add, update, delete, and view student records     using a menu-driven interface.

- 📋 Features

  ✅ Add new student and their grade
  🔁 Update existing student's grade
  ❌ Delete a student record
  📃 Display all student records
  🚪 Exit the program gracefully

No external libraries required.

- 🧑‍💻 Usage

  When the program runs, you’ll be presented with a menu:
  | STUDENT GRADE MANAGEMENT SYSTEM |
  1. Add student.
  2. Update student.
  3. Delete student.
  4. Display all students.
  5. Exit.
  Example Workflow:
  Enter the number of the command : 1
  Enter the name of the student : Alice
  Enter student's grades : 92
  Added Alice with 92 grade.
  
  Enter the number of the command : 4
  Alice : 92

- 🧾 Notes

  Student names are used as unique keys in a dictionary.
  Grades must be entered as integers.
  No persistent storage (like files or databases) is used in this version — data exists only while the program is running.

- 🧱 Future Improvements (Suggestions)

  Add data persistence using files or databases.
  Input validation (e.g., prevent invalid grade inputs).
  GUI version using Tkinter or PyQt.
  Support for multiple subjects and average grade calculation.

- 🖊️ Author

  Made by Arya Madiwale.
  Feel free to modify and expand the project as you like!

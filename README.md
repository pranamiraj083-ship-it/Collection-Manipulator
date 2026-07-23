#collection manipulator
# Student Data Organizer

A simple Python console-based application to manage student records using Python collections such as Lists and Dictionaries. This project demonstrates CRUD (Create, Read, Update, Delete) operations through a menu-driven interface.

## Features

- Add new student records
- Display all students
- Update student information
- Delete student records
- Display available subjects
- Easy menu-driven interface
- Uses Python Lists and Dictionaries

---

## Technologies Used

- Python 3.x
- Lists
- Dictionaries
- Loops
- Match-Case
- Conditional Statements

---

## Project Structure

```
Student-Data-Organizer/
│
├── student_data_organizer.py
├── README.md
└── LICENSE (Optional)
```

---

## Project Overview

This application allows users to store and manage student information from the terminal. Every student record contains:

- Student ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

The records are stored inside a Python list where each student is represented as a dictionary.

---

## Menu Options

### 1. Add Student

Enter the following details:

- Student ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

The student record is stored successfully.

---

### 2. Display All Students

Displays all student records in a formatted manner.

Example:

```
Student ID : 101
Name       : Raj
Age        : 22
Grade      : A
Subjects   : Math, Science
```

---

### 3. Update Student Information

Update an existing student's information using the Student ID.

You can modify:

- Name
- Age
- Grade
- Date of Birth
- Subjects

---

### 4. Delete Student

Deletes a student record based on the Student ID.

---

### 5. Display Subjects Offered

Displays the available subjects.

```
Math
Science
English
```

---

### 6. Exit

Closes the application with a thank-you message.

---

## Sample Output

```
Welcome to the Student Data Organizer!

Select an Option

1. Add Student
2. Display All Student
3. Update Student Information
4. Delete Student
5. Display Subject Offered
6. Exit

Enter your choice: 1

Enter Student Details

Student ID: 101
Name: raj
Age: 22
Grade: A
Date of Birth: 2004/02/12
Subjects: Math, Science

Student added successfully!
```

---

## Python Concepts Used

- Variables
- User Input
- Lists
- Dictionaries
- Loops
- Match-Case
- Conditional Statements
- CRUD Operations
- String Formatting

---

## Future Improvements

- Store records permanently using JSON or CSV
- Search student by ID
- Add duplicate ID validation
- Better error handling
- Use Sets for subject management
- Improve user interface

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/Student-Data-Organizer.git
```

2. Open the project folder

```bash
cd Student-Data-Organizer
```

3. Run the program

```bash
python student_data_organizer.py
```

---

## Author

**Pranami Raj**

GitHub: https://github.com/pranamiraj083-ship-it

---

## License

This project is open-source and available under the **MIT License**.

---

```
# Python DAO-Service School Management System

## Overview
This Python-based school management system is designed to manage teacher and student data using a MySQL database. It leverages the Data Access Object (DAO) design pattern to abstract and encapsulate all access to the data source, facilitating CRUD operations for both students and teachers via a clear, menu-driven interface.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
```

exercise2/
├── dao/ # Data Access Objects for abstracting database interactions
│ ├── **init**.py
│ ├── abc_student_dao.py
│ ├── abc_teacher_dao.py
│ ├── student_dao_impl.py
│ ├── teacher_dao_impl.py
├── service/ # Service layer to define business logic
│ ├── **init**.py
│ ├── student_service.py
│ ├── teacher_service.py
├── tests/ # Unit tests for DAO and service layers
│ ├── **init**.py
│ ├── test_student_dao.py
│ ├── test_student_service.py
│ ├── test_teacher_dao.py
│ ├── test_teacher_service.py
├── venv/ # Virtual environment for project dependencies
├── main.py # Main application file with menu-driven interface
├── requirements.txt # Project dependencies
├── schoolapp.sql # SQL script for database schema setup
└── README.md # Documentation file

````

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- MySQL Server

### Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd exercise2
````

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Use `venv\\Scripts\\activate` on Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```bash
   mysql -u root -p
   source schoolapp.sql
   ```

### Running the Application

Execute the main script to start the application:

```bash
python main.py
```

## Usage

The application provides a menu-driven interface with options to manage teachers and students:

- Add, retrieve, update, and delete teachers.
- Add, retrieve, update, and delete students.
- List all teachers or all students.

Choose the appropriate menu item number to perform operations.

## Running Tests

To run the automated tests for this system, execute:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

```

```

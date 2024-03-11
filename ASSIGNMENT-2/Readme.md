# Academic Unit System

The Academic Unit System is a simple Python-based application with a graphical user interface (GUI) implemented using the Tkinter library. This system allows users to register as teachers, postgraduate (PG) students, or undergraduate (UG) students, log in, update their details, and deactivate their accounts.

## Features

- **User Registration:**
  - Users can register as Teachers, PG Students, or UG Students.
  - Password strength is enforced for security.

- **Login and Account Management:**
  - Users can log in using their credentials.
  - Teachers, PG Students, and UG Students have specific details associated with their accounts.
  - Users can update their details and deactivate their accounts.

- **Data Persistence:**
  - User data is stored in a JSON file (`data.json`).
  - Data is loaded at the start of the application and saved after any modifications.

## How to Use

1. **Registration:**
   - Click on "Register User."
   - Select the role (Teacher, PG Student, UG Student) and fill in the required information.
   - Click "Register" to create an account.

2. **Login:**
   - Click on "Sign In."
   - Enter your User ID and Password.
   - Click "Submit" to log in.

3. **Account Management:**
   - After logging in, you can update your details or deactivate your account.

## Project Structure

- **`main.py`:**
  - The main script that launches the Tkinter application.
  - Defines the Person, Teacher, Student, PGStudent, and UGStudent classes.
  - Contains functions for user registration, login, updating details, and deactivation.

- **`data.json`:**
  - JSON file storing user data.

## Dependencies

- **Tkinter:** Python's standard GUI library.
- **json:** For reading and writing JSON files.

## Future Improvements

- Enhanced error handling for various scenarios.
- Improved password security measures, such as hashing.
- GUI design enhancements for a better user experience.
- More thorough input validation for user data.
- Logging for better debugging and monitoring.

Feel free to contribute or provide feedback to enhance the functionality and usability of the Academic Unit System.

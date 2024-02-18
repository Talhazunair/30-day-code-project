# Django Note Taking Web Application

This is a note-taking web application implemented using Django, a high-level Python web framework. The application allows users to create, view, edit, and delete notes after authentication.

## Features
- User authentication (sign up, login, logout)
- CRUD operations on notes (Create, Read, Update, Delete)
- Password hashing for security
- Error handling for invalid credentials and password mismatch
- Flash messages for successful actions
- Form validation
- User-specific note management

## Requirements
- Python 3.x
- Django
- Pillow (for image field support, if any)
- Database (e.g., SQLite, PostgreSQL)

## How to Run
1. Ensure you have Python installed on your system.
2. Install Django using pip:
   ```
   pip install django
   ```
3. Clone or download this repository to your local machine.
4. Navigate to the project directory in a terminal or command prompt.
5. Run the following command to apply migrations and create the database:
   ```
   python manage.py migrate
   ```
6. Start the Django development server by running:
   ```
   python manage.py runserver
   ```
7. Open a web browser and go to `http://localhost:8000` to access the application.
8. Sign up for a new account or log in with existing credentials.
9. Start creating, viewing, editing, and deleting notes.

## Project Structure
- **`Notes`**: Django app containing models, views, and templates related to note management.
- **`Signup.html`**: Template for user signup page.
- **`Home.html`**: Template for the homepage.
- **`Login.html`**: Template for user login page.
- **`User_View.html`**: Template for displaying user-specific notes.
- **`Add_Notes.html`**: Template for adding new notes.
- **`View_Note.html`**: Template for viewing individual notes.
- **`Edit_Notes.html`**: Template for editing existing notes.

## Customization
- You can customize the templates, such as adding styling or additional features.
- Extend the functionality by adding more fields to the Note model or implementing additional features like categories, tags, or sharing notes with other users.

Feel free to contribute to this project by submitting pull requests or reporting issues. Thank you for using the Django Note Taking Web Application!
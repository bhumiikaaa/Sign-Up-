# Sign-Up System with Flask and SQL Connectivity

This is a simple sign-up system built using **Flask** for the backend and an **SQL database** (such as MySQL or SQLite) for data storage. Users can register with their name, email, and password, which will be securely stored in the database.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (preferably Python 3.x)
- Flask (Web Framework)
- SQLAlchemy (SQL ORM for Python)
- MySQL or SQLite (for the database)

How It Works
User Registration Form:

The user fills out the registration form with their name, email, and password.
The form is validated using Flask-WTF to ensure that the data is in the correct format.
Form Submission:

Once the form is submitted, the data is sent to the Flask route, where it is processed.
The system checks if the email already exists in the database.
If the email is unique, the user is added to the database.
Password Hashing:

The user's password is hashed using Werkzeug's generate_password_hash() function to ensure security before storing it in the database.
Database:

User details (name, email, and hashed password) are stored in the database (MySQL or SQLite), using SQLAlchemy for ORM functionality.

Running the Application:
Run the Flask Development Server:
python run.py
Visit http://127.0.0.1:5000/ in your browser to access the sign-up page.

Example Usage:

Start the Application: Run the server using python run.py.

Navigate to the Sign-Up Page: Go to http://127.0.0.1:5000/.

Fill out the Registration Form:

Enter a name, email, and password.

After submitting the form, the user will be added to the database if the email is unique.

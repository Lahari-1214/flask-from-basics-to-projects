## Project Abstract
This project is a basic user authentication system developed using Flask (Python) and MySQL database.
The system allows users to register, log in, and then view their profile information.
1. Registration Module
The registration page contains input fields such as:
- First Name
- Last Name
- Email
- Username
- Password
- Confirm Password
When the user fills the form and submits it:
The application verifies that password and confirm password match.
The user details are then inserted into the MySQL database.
A success message is displayed directing the user to the login page.
2. Login Module
The login page contains:
- Username
- Password
When the user submits the login form:
The application checks the credentials in the users table inside the MySQL database.
If the details are correct, the user is logged in and redirected to the Profile Page.
If the credentials are incorrect, an error message is displayed.
3. Profile Page
After a successful login:
The user’s stored information (Name, Email, Username) is retrieved from the database.
These details are displayed on the Profile Page.
This profile page is rendered without using sessions; instead, the user data is passed directly from the login validation function to the profile page.

### Objective
The main goal of this project is to demonstrate:
How to create forms in Flask
How to collect user input
How to connect and interact with a MySQL database
How to validate user login and display personalized information

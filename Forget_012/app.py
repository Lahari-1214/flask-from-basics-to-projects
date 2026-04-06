from flask import Flask, render_template, request, redirect, flash, session
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
# Create Flask application
app = Flask(__name__)
app.secret_key = "mysecretkey"   # Secret key for session and token encryption

# ---------------- EMAIL CONFIGURATION ----------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'   # Gmail SMTP server
app.config['MAIL_PORT'] = 587                 # Mail server port
app.config['MAIL_USE_TLS'] = True             # Use TLS encryption
app.config['MAIL_USERNAME'] = "janicode249@gmail.com"  # Sender email
app.config['MAIL_PASSWORD'] = "emfx fkdl xfly yzry"     # App Password from Gmail

mail = Mail(app)  # Initialize Flask-Mail with app

# Token Serializer (used for generating secure reset password links)
s = URLSafeTimedSerializer(app.secret_key)

# Dummy Database (Dictionary for example only — no real DB)
users = {"janicode249@gmail.com": {"password": "abc123"}}

# ---------------- ROUTES ----------------

# Login Page
@app.route('/')
def home():
    return render_template("login.html")


# Login Handling
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']        # Get user email from form
    password = request.form['password']  # Get password from form
 
    # Check if user exists and password matches
    if email in users and users[email]["password"] == password:
        session['email'] = email  # Store email in session (User stays logged in)
        return redirect("/dashboard")  # Redirect to dashboard
    else:
        flash("Invalid Login!")  # Show error message
        return redirect("/")     # Redirect back to login page

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
    

# Dashboard Page (Accessible only if logged in)
@app.route('/dashboard')
def dashboard():
    if 'email' in session:   # If user is logged in
        return render_template("dashboard.html", user=session['email'])
    return redirect('/')     # If not logged in → go to login


# Forgot Password Page
@app.route('/forgot_password')
def forgot_password():
    return render_template("forgot_password.html")
# Sending Reset Password Email Link
@app.route('/send_reset_link', methods=['POST'])
def send_reset_link():
    email = request.form['email']  # Get entered email
    
    # If email is not present in dummy database
    if email not in users:
        flash("Email not registered!")
        return redirect('/forgot_password')
    
    # Create secure token containing user's email
    token = s.dumps(email, salt='password-reset-salt')
    
    # Generate reset link using token
    link = f"http://localhost:5000/reset_password/{token}"
    
    # Create email message
    msg = Message("Password Reset Request", 
                  sender="janicode249@gmail.com",
                  recipients=[email])
    msg.body = f"Click the link to reset your password: {link}"
    mail.send(msg)  # Send email
    
    flash("Reset link sent to your email!")
    return redirect('/')

# Reset Password Page (User clicks the link from email)
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        # Decode token to get user's email
        email = s.loads(token, salt='password-reset-salt', max_age=300)  
        # max_age=300 → link valid for 5 minutes
    except SignatureExpired:
        return "Link expired! Try again."
    
    # After form submission → Save new password
    if request.method == 'POST':
        new_password = request.form['password']
        users[email]["password"] = new_password  # Update password in dummy DB
        flash("Password reset successful! Please login.")
        return redirect('/')
    
    # Show Reset Password Form
    return render_template("reset_password.html")


# Logout
@app.route('/logout')
def logout():
    session.pop('email', None)  # Remove user session
    return redirect('/')        # Go back to login page


# Run server
app.run(debug=True)





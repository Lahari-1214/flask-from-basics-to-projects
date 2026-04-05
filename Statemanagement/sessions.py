from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "abc123"

@app.route('/login')
def login():
    session['user'] = "Jani"
    return "Logged in!"
@app.route('/profile')
def profile():
    return f"Welcome {session['user']}"

@app.route('/logout')
def logout():
    session.pop('user')
    return "Logged out!"

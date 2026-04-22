# server side session management
from flask import Flask, render_template, request, redirect, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "mysecret123"
app.permanent_session_lifetime = timedelta(minutes=2)

# Hardcoded username & password
USER = {"username": "admin", "password": "1234"}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if username == USER["username"] and password == USER["password"]:
            session.permanent = True
            session['username'] = username
            return redirect("/dashboard")
        else:
            return "Invalid Credentials. Try Again!"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if 'username' in session:
        return render_template("dashboard.html", user=session['username'])
    else:
        return redirect("/")


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

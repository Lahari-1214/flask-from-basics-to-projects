from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your_password",
    database = "your_database"

)
@app.route('/')
def register_page():
    return render_template("register.html")


@app.route('/register',methods = ['POST'])
def Register():
    fname = request.form['firstname']
    lname = request.form['lastname']
    email = request.form['email']
    uname = request.form['username']
    pwd = request.form['password']
    cpwd = request.form['cpassword']

    if pwd != cpwd:
        return "Confirm the password"
    
    query = "INSERT INTO users(firstname, lastname, email, username, password) VALUES (%s,%s,%s,%s,%s)"
    cursor = mydb.cursor()
    cursor.execute(query, (fname, lname, email, uname, pwd,))
    mydb.commit()
    return " Registration Successful! <br><a href='/login'>Go to Login</a>"

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/logincheck', methods = ['POST'])
def login_check():
    uname = request.form['username']
    pwd = request.form['password']

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor = mydb.cursor()
    cursor.execute(query, (uname, pwd,))
    result = cursor.fetchone()

    if result:
        return "Login Successful!"
    else:
        return "Invalid username or password. Please try again."




if __name__ == "__main__":
    app.run(debug = True)


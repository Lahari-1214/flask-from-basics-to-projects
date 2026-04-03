from flask import Flask, render_template, request,jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'yourpassword',
    database = 'yourdatabase'
)

# Testing the database connection
@app.route('/')
def Home():
    return "DB connection is Success...... "


# Retrieving all users from the database and returning them as JSON
@app.route('/getusers',methods=['GET'])
def Getallusers():
    cursor = mydb.cursor()
    cursor.execute("select * from users")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

# Retrieving a specific user by ID from the database and returning it as JSON
@app.route('/getuser/<int:id>',methods=['GET'])
def Getuser(id):
    cursor = mydb.cursor()
    cursor.execute("select * from users where id = %s",(id,))
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)

# Adding a new user to the database using data from a POST request
@app.route('/adduser',methods=['POST'])
def Adduser():
    data = request.get_json()
    name = data['name']
    email = data['email']
    cursor = mydb.cursor()
    cursor.execute("insert into users (name,email) values (%s,%s)",(name,email))
    mydb.commit()
    cursor.close()
    return jsonify({'message':'User added successfully'})





if __name__ == '__main__':
    app.run(debug=True)

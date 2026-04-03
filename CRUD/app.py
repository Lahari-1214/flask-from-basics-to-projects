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





if __name__ == '__main__':
    app.run(debug=True)

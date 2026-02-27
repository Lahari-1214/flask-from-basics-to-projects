from flask import Flask,redirect,url_for,request
app = Flask(__name__)
@app.route('/')
def Home():
    return "Welcome Home"

# Get request # url:http://127.0.0.1:5000/get_data?name=Jani&age=24 
@app.route('/getdata',methods=['GET'])
def GetData():
    name = request.args.get('name')
    return f"How can I help you!{name}"

# POST Request
from flask import Flask, request

app = Flask(__name__)

@app.route('/postdata', methods=['GET', 'POST'])
def postdata():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        return f"Hello {username} and your registered email is {email}"
    else:
        return """
            <form action='/postdata' method='post'>
                <input type='text' name='username' placeholder='Enter username' required>
                <input type='email' name='email' placeholder='Enter email' required>
                <button type='submit'>Submit</button>
            </form>
        """

if __name__ == '__main__':
    app.run(debug=True)
    
 




from flask import Flask,redirect,url_for,request,jsonify
app = Flask(__name__)

# Mock data for PUT request
data = {
    "name":"Jani",
    "age":24
}


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
# PUT Request URL: http://127.0.0.1:5000/update in POSTMAN with JSON body {"name":"Jani","age":24}
@app.route('/update',methods=['PUT'])
def Update():
    nname = request.json.get('name')
    nage = request.json.get('age')

    data['name'] = nname
    data['age'] = nage
    return jsonify({"new data":data})

# DELETE Request URL: http://127.0.0.1.5000/delete in POSTMAN with JSON body {"name":"Jani"}
@app.route('/delete',methods=['DELETE'])
def Delete():
    name = request.json.get('name')
    if data['name'] == name:
        data['name'] = None
        data['age'] = None
        return jsonify({"message":"Data deleted successfully"})
    else:
        return jsonify({"message":"Name not found in data"})
if __name__ == '__main__':
    app.run(debug=True)
    
 




from flask import Flask,redirect,url_for,request
app = Flask(__name__)
@app.route('/')
def Home():
    return "Welcome Home"

# Get request
@app.route('/getdata',methods=['GET'])
def GetData():
    name = request.args.get('name')
    return f"How can I help you!{name}"

if __name__ == '__main__':
    app.run(debug=True)
    
# url:http://127.0.0.1:5000/get_data?name=Jani&age=24  


# POST Request

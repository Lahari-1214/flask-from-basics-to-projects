from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome home"

@app.route('/INT/<int:num>')
def Number(num):
    #if you give any other type of data except integer it won't accept
    return f"Your integer number is {num}"

@app.route('/FLOAT/<float:num>')
def Number2(num):
    #if you give any other type of data except float it won't accept
    return f"Your floating number is {num}"

@app.route('/STR/<num>')
def Number3(num):
    #by default route accepts string values
    return f"Your number is {num}"

@app.route('/PATH/<path:num>')
def Number4(num):
    #it accepts the data which contains slash(/)
    return f"Your number is {num}"

@app.route('/UUID/<uuid:num>')
def Number5(num):
    #it accepts the data in form of 8-4-4-4-12 which contains only a-e/0-9
    return f"Your number is {num}"

if __name__ == '__main__':
    app.run(debug=True)






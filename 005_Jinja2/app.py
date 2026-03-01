from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def Home():
    return f'''
    <h1>What you want to Learn:</h1><br>
    <h2>/variable</h2><br>
    <h2>/loop</h2>
    '''
# Variables in JINJA2
@app.route('/variable')
def Variable():
    return render_template("index.html",name="Leela",age = "23")

# Loops in JINJA2
@app.route('/loop')
def Loops():
    user_list = ['Leela','Surya','Satya','Abhi']
    return render_template("users.html",users=user_list)

if __name__ == '__main__':
    app.run(debug = True)
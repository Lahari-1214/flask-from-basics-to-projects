from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def Home():
    return f'''
    <h1>What you want to Learn:</h1><br>
    <h2>1./variable</h2><br>
    <h2>2./loop</h2><br>
    <h2>3./check<h2>
    <h2>4./Profile</h2>
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


# Conditionals in JINJA2
@app.route("/check")
def check():
    return render_template("check.html", age=20)

#Accessing Dictionary elements
@app.route('/Profile')
def Profile():
    user = {'name':"leela",'ID':210,'Branch':'CSE'}
    return render_template("profile.html",user = user)

if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def Home():
    return "want you want to learn"
# Variables in JINJA2
@app.route('/variable')
def Variable():
    return render_template("index.html",name="Leela",age = "23")
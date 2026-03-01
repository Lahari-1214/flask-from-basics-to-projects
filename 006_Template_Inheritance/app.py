from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def Login():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('home',username=username))
    return render_template("login.html")

@app.route("/home",methods=['POST'])
def home():
    username = request.form['username']
    return render_template("home.html", username=username)




if __name__ == "__main__":
    app.run(debug = True)
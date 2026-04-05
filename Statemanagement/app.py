from flask import Flask, session,redirect,request,render_template

from datetime import timedelta


app=Flask(__name__)

app.secret_key='xyz1236'




# hardcoded data 

user={"uname":"admin",'pwrd':"123"}

# route for login

@app.route("/",methods=['GET','POST'])
def Login():
    if request.method=='POST':
        uname=request.form['uname']
        pwrd=request.form['pwrd']

        if uname==user['uname'] and pwrd==user['pwrd']:
            session.permanent=True
            session['uname']=uname  # {'uname':"admin"}
            return redirect("/dashboard")
        else:
            return "Invalid credentials Please try again <br><br> <a href='/'>Login</a>"


    return render_template("login.html")


# route for dashboard

@app.route('/dashboard')
def Dashboard():
    if 'uname' in session:
        return render_template("dashboard.html",username=session['uname'])
    return redirect("/")




if __name__=='__main__':
    app.run(debug=True)
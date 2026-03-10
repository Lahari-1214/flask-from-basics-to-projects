from flask import Flask, render_template, request,session,redirect,url_for
from Generate_otp import Generate_otp
app = Flask(__name__)

app.secret_key = '123abc'
@app.route('/', methods=['GET', 'POST'])
def sendpage():
    return render_template('send.html')

@app.route('/sendotp',methods=['POST'])
def Sendotp():
    otp=Generate_otp()
    session['otp']=otp
    print("Generated OTP is:",otp)
    return redirect(url_for('Verifypage'))

@app.route("/verifypage")
def Verifypage():
    return render_template('verify.html')

@app.route('/checkotp',methods=['POST'])
def VerifyOTP():
    otp=request.form['otp']

    if str(session['otp'])==otp:
        return "✅ OTP is verified "
    else:
        return "❌ Invalid OTP"


if __name__=='__main__':
    app.run(debug=True)
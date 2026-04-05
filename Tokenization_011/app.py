from flask import Flask,request,render_template

from itsdangerous import URLSafeTimedSerializer,BadSignature,SignatureExpired

app=Flask(__name__)

serializer=URLSafeTimedSerializer("abc123",salt='otp')

# route for login page

@app.route('/')
def Login():
    return render_template('login.html')

#  route for send otp

@app.route('/sendotp', methods=['POST'])
def Sendpage():
    email=request.form['email']

    #  how to convert email into token
    token=serializer.dumps(email)
    return render_template('verify.html',token=token)


# route for verify otp
@app.route('/verifyotp',methods=['POST'])
def Verify():
    token=request.form['entertoken']

    try:
        email=serializer.loads(token,max_age=20)
        return f"OTP IS verified for the email : {email}"
    
    except SignatureExpired:
        return "Time is expired......."
    except BadSignature:
        return "Invalid OTP Token......"
    
if __name__=='__main__':
    app.run(debug=True)
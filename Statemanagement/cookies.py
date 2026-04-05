from flask import Flask, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    res = make_response("Cookie Set")
    res.set_cookie("username", "Jani")
    return res

@app.route('/get_cookie')
def get_cookie():
    from flask import request
    user = request.cookies.get("username")
    return f"Cookie Value = {user}"

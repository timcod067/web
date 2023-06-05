import os
from flask import Flask, render_template, redirect, session, url_for
# from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def firstpage():  # put application's code here
    return render_template('firstpage.html')

@app.route('/checi')
def checi():  # put application's code here
    return render_template('checi.html')

@app.route('/money')
def money():  # put application's code here
    return render_template('money.html')

@app.route('/outlink')
def outlink():  # put application's code here
    return render_template('page4.html')

@app.route('/aboutus')
def aboutus():  # put application's code here
    return render_template('finalpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
        # account = request.form["account"]
        # user_password = user.check(account)
        # password = request.form["password"]
        # bcrypt = Bcrypt()
        # check = bcrypt.check_password_hash(user_password[0], password)
        # if check == True:
            useData = ['timping', 1]
            session['userData'] = useData
            return redirect(url_for('getsession'))
    # return render_template('login.html')

@app.route('/login1', methods=['GET', 'POST'])
def login1():
    # if request.method == 'POST':
        # account = request.form["account"]
        # user_password = user.check(account)
        # password = request.form["password"]
        # bcrypt = Bcrypt()
        # check = bcrypt.check_password_hash(user_password[0], password)
        # if check == True:
            useData = ['jone', 2]
            session['userData'] = useData
            return redirect(url_for('getsession'))
    # return render_template('login.html')

@app.route('/getsession')
def getsession():
    if 'userData' in session:
        print (session['userData'])
        return session['userData'][0]
    return "Not logged in!"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = '12389!)!834913*&*&*&*'
    app.run()

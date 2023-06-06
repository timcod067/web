import os
from flask import Flask, render_template, redirect, session, url_for,request
from register import Data
from favorite import Favorite
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def firstpage():  # put application's code here
    return render_template('firstpage.html')


@app.route('/checi')
def checi():  # put application's code here
    if 'userData' in session:
            favs = Favorite.get(session['userData'][0])
            return render_template('checi.html', favs=favs)
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

@app.route('/userpage')
def userpage():  # put application's code here
    user = Data.getUserData(session['userData'][1])
    return render_template('userpage.html', user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        account = request.form["account"]
        password = request.form["password"]
        email = request.form["email"]
        bcrypt = Bcrypt()
        hashed_password = bcrypt.generate_password_hash(password=password)
        users = Data.register(account, hashed_password, email)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        account = request.form["account"]
        user_password = Data.check(account)
        password = request.form["password"]
        bcrypt = Bcrypt()
        check = bcrypt.check_password_hash(user_password[0], password)
        if check == True:
            user = Data.getUserData(account)
            useData = [user[0], user[1]]
            session['userData'] = useData
            return redirect(url_for('firstpage'))
    return render_template('login.html')

@app.route('/getsession')
def getsession():
    if 'userData' in session:
        return session['userData'][0]
    return "Not logged in!"

@app.route('/logout')
def logout():
    session.pop('userData',None)
    return render_template('firstpage.html')

@app.route('/addfav', methods=['POST'])
def addfav():  # put application's code here
    trainid = request.form["trainid"]
    if 'userData' in session:
        favs = Favorite.add(trainid, session['userData'][0])
        favs = Favorite.get(session['userData'][1])
        return redirect(url_for('checi'))
    return "Not logged in!"

@app.route('/delfav', methods=['POST'])
def delfav():  # put application's code here
    trainid = request.form["trainid"]
    if 'userData' in session:
        favs = Favorite.delete(trainid, session['userData'][0])
        return redirect(url_for('checi'))
    return "Not logged in!"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = '12389!)!834913*&*&*&*'
    app.run()

from flask import Flask, render_template

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()

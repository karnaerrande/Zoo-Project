from flask import Flask, render_template, request, jsonify

import MySQLdb

#create flask object, __name__ is the name of module
app = Flask(__name__,static_url_path='/static')

#MYSQL Config
db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    db="applegatezoo"
    )

cur=db.cursor()

#frontend
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/animals')
def animals():
    return render_template("animals.html")


#backend
@app.route('/allanimals')
def allanimals():
    return 0;

#if we run this file directly(python run.py), enter into debug mode
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


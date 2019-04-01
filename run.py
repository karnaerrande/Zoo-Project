#!/usr/bin/env python
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

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/admin')
def admin():
    return render_template("admin.html");


#backend
@app.route('/allanimals')
def allanimals():
    return 0;

#add routes for getting, removing, and adding animals

#if we run this file directly(python run.py), enter into debug mode
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

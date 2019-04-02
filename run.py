#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify

import MySQLdb

#create flask object, __name__ is the name of module
app = Flask(__name__,static_url_path='/static')

#MYSQL Config
db = MySQLdb.connect(
    host="10.34.84.35:3306",
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
    query="SELECT * FROM animals;"
    cur.execute(query)
    anlist=cur.fetchall()

    jsonlist = []

    for entry in anlist:
        anid = entry[0]
        anname = entry[1]

        rec = {"idanimal":anid,"nameanimal":anname}

        jsonlist.append(rec)

    return jsonify(jsonlist);

#add routes for getting, removing, and adding animals
@app.route('/get')
def getAnim(id):
    id = request.args.get('id')
    query="SELECT * FROM animals WHERE idanimal="+id+";"
    cur.execute(query)
    anlist=cur.fetchall()

    jsonlist = []

    for entry in anlist:
        anid = entry[0]
        anname = entry[1]

        rec = {"idanimal":anid,"nameanimal":anname}

        jsonlist.append(rec)

    return jsonify(jsonlist);

@app.route('/remove')
def removeAnim(id):
    id = request.args.get('id')
    query="DELETE FROM animals WHERE idanimal="+id+";"
    return 0;

def addAnim(name):
    id = request.args.get('name')
    query="INSERT INTO `applegatezoo`.`animals`(`nameanimal`) VALUES (\'"+name+"\');"
    return 0;

#if we run this file directly(python run.py), enter into debug mode
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

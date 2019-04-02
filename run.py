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
    myanimals = allanimals()
    return render_template("animals.html", myanimals=myanimals)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/admin')
def admin():
    
    return render_template("admin.html")


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

    return jsonify(jsonlist)

@app.route('/get')
def getAnim():
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

    return jsonify(jsonlist)

@app.route('/remove')
def removeAnim():
    id = request.args.get('id')
    query="DELETE FROM animals WHERE idanimal="+id+";"
    cur.execute(query)
    return cur.fetchall()

@app.route('/addAnim')
def addAnim():
    name = request.args.get('name')
    query="INSERT INTO animals (nameanimal) VALUES (\'"+name+"\');"
    cur.execute(query)
    return cur.fetchall()

#if we run this file directly(python run.py), enter into debug mode
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

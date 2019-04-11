#!/usr/bin/env python
#from flask_cors import CORS
from flask import Flask, render_template, request, jsonify
import MySQLdb, os, shutil, json

#create flask object, __name__ is the name of module
app = Flask(__name__,static_url_path='/static')
# cors = CORS(app)

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
        name = entry[1]

        rec = {"id_animal": anid,"name_animal": name}

        jsonlist.append(rec)

    return jsonify(jsonlist)

@app.route('/get/<string:id>')
def getAnim(id):
    query="SELECT * FROM animals WHERE id_animal="+id+";"
    cur.execute(query)
    anlist=cur.fetchall()

    jsonlist = []

    for entry in anlist:
        anid = entry[0]
        name = entry[1]

        rec = {"id_animal":anid,"name_animal":name}

        jsonlist.append(rec)

    return jsonify(jsonlist)

@app.route('/remove/<string:id>')
def removeAnim(id):
    query="DELETE FROM animals WHERE id_animal = "+id+";"
    cur.execute(query)
    return cur.fetchall()

def removeAnimalFolder(name):
    try:
        if os.path.exists('./static/animals/'+name):
            shutil.rmtree('./static/animals/'+name)
    except OSError:
        print('Unable to remove the directory at ./static/animals/'+name)

def createAnimalFolder(name):
    try:
        if not os.path.exists('./static/animals/'+name):
            os.makedirs('./static/animals/'+name)
    except OSError:
        print('Couldn\'t create directory at ./static/animals/'+name)

#backend
@app.route("/process", methods =['GET','POST'])
def process():
    name = request.form.get('animal-name')
    createAnimalFolder(name)
    endangered = request.form.get("animal-end")
    desc = request.form.get("animal-desc")
    query="INSERT INTO animals (name_animal) VALUES (\'"+name+"\');"
    cur.execute(query)
    query="SELECT * FROM animals WHERE name_animal = \'"+name+"\';"
    cur.execute(query)
    animal = cur.fetchall() 
    animal_id = animal[0]
    myObj = {"id":animal_id, "name":name, "endangered": endangered, "description": desc}
    data = jsonify(myObj)
    jsfn = "./static/animals/"+name+"/"+name+".json"
    with open(jsfn, 'w') as outfile:
        json.dump(data, outfile)
    return myObj

#if we run this file directly(python run.py), enter into debug mode
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

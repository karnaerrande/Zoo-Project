from flask import Flask, render_template, request, jsonify

import MySQLdb

#create flask object, __name__ is the name of module
app = Flask(__name__)
        
#MYSQL Config
db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    db="uni"
    )

cur=db.cursor()

#frontend
@app.route('/')
def home():
    return render_template("index.html")



#backend
#@app.route('/')
#def allAnimals():
    #arr
    #return jsonify(arr);

#if we run this file directly(python run.py), enter into debug mode
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

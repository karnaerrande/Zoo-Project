#!/usr/bin/env python
from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import AnimalForm

app = Flask(__name__)
app.config['SECRET_KEY']='tFXcmRsHfxl3kyaA4b59'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Animal(db.Model):
    id_animal = db.Column(db.Integer, primary_key=True)
    name_animal = db.Column(db.String(20), unique=True, nullable = False)
    desc_animal = db.Column(db.String(2000), unique=True, nullable = False)
    endangered_animal = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return "Animal('{}','{}','{}')".format(self.id_animal,self.name_animal,self.endangered_animal)

#frontend
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin/config", methods=['GET', 'POST'])
def animconfig():
    return 0

@app.route("/admin", methods =['GET','POST'])
def admin():
    allAnim=Animal.query.all()
    animForm = AnimalForm()
    if animForm.validate_on_submit():
        temp = Animal(name_animal=animForm.name_animal.data,desc_animal=animForm.desc_animal.data,endangered_animal=animForm.endangered_animal.data)
        db.session.add(temp)
        db.session.commit()
        flash('Animal created for {}!'.format(animForm.name_animal.data),'success')
        return redirect("/admin")
    return render_template("admin.html", animForm=animForm, allAnim=allAnim)

@app.route("/animals")
def animals():
    allAnim=Animal.query.all()
    return render_template("animals.html", allAnim=allAnim)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/map")
def map():
    return render_template("map.html")




if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)

from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, TextAreaField, StringField, SubmitField, validators
from wtforms.validators import DataRequired, Length

"""
Args:
    self(animal): animal object
    fields(string[]): fields for the animal
    args(string[]): args for each field
"""
class Animal:
    def _init_(self,name, desc, fields, args):
        #TODO: Implement 
        return 0

class AnimalForm(FlaskForm):
    name_animal = StringField('Name of Animal:',
                                validators=[DataRequired(), Length(min=2, max=20)])
    
    desc_animal = TextAreaField()

    submit = SubmitField('Post Animal')

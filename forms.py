from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, TextAreaField, StringField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email
from wtforms.fields.html5 import EmailField

"""
Args:
    self(animal): animal object
    fields(string[]): fields for the animal
    args(string[]): args for each field
"""
class Animal:
    def _init_(self,name, desc, endangered, fields, args):
        #TODO: Implement
        return 0

class AnimalForm(FlaskForm):
    name_animal = StringField('Name of Animal:',
                                validators=[DataRequired(), Length(min=2, max=20)])

    desc_animal = TextAreaField()

    endangered_animal = BooleanField()

    submit = SubmitField('Post Animal')

class Contact:
    def _init(self, name, email, subject, message):
        # TODO: Implement
        return 0

class ContactForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired(), Length(min=2, max=40)])

    # email = StringField("Your email",  validators=[DataRequired(), Email("This field requires a valid email address")])
    email = EmailField('Your email', validators=[DataRequired(), Email("This field requires a valid email address")])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=40)])

    message = TextAreaField('Message', validators=[DataRequired()]);

    submit = SubmitField('Post Contact');

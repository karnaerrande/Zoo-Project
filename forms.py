from flask_wtf import FlaskForm
from wtforms import Form, PasswordField, BooleanField, TextAreaField, StringField, SubmitField, validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import EqualTo,DataRequired, Length, Email
from wtforms.fields.html5 import EmailField



class AnimalForm(FlaskForm):
    name_animal = StringField(u'Animal Name',
                                validators=[validators.optional(),Length(min=2, max=100)])
    names =  StringField(u'Names',
                                validators=[validators.optional(),Length(min=2, max=100)])
    img = FileField(validators=[validators.optional()])
    dist_animal = TextAreaField(u'Distribution', [validators.optional(), validators.length(max=2000)])
    desc_animal = TextAreaField(u'Description', [validators.optional(), validators.length(max=2000)])

    breed_animal = TextAreaField(u'Breeding', [validators.optional(), validators.length(max=2000)])
    diet_animal = TextAreaField(u'Diet', [validators.optional(), validators.length(max=2000)])
    behavior_animal = TextAreaField(u'Behavior', [validators.optional(), validators.length(max=2000)])
    status_animal = StringField(u'Animal Status',
                                validators=[validators.optional(), Length(min=2, max=100)])

    fact_animal = TextAreaField(u'Fact', [validators.optional(), validators.length(max=2000)])

    submit = SubmitField('Post')

class UpdateAnimalForm(FlaskForm):
    name_animal = StringField(u'Animal Name',
                                validators=[validators.optional(),Length(min=2, max=100)])
    names =  StringField(u'Names',
                                validators=[validators.optional(),Length(min=2, max=100)])
    img = FileField()
    dist_animal = TextAreaField(u'Distribution', [validators.optional(), validators.length(max=2000)])
    desc_animal = TextAreaField(u'Description', [validators.optional(), validators.length(max=2000)])

    breed_animal = TextAreaField(u'Breeding', [validators.optional(), validators.length(max=2000)])
    diet_animal = TextAreaField(u'Diet', [validators.optional(), validators.length(max=2000)])
    behavior_animal = TextAreaField(u'Behavior', [validators.optional(), validators.length(max=2000)])
    status_animal = StringField(u'Animal Status',
                                validators=[validators.optional(), Length(min=2, max=100)])

    fact_animal = TextAreaField(u'Fact', [validators.optional(), validators.length(max=2000)])

    submit = SubmitField('Post')

class ContactForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired(), Length(min=2, max=40)])
    email = EmailField('Your email', validators=[DataRequired(), Email("This field requires a valid email address")])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=40)])

    message = TextAreaField('Message', validators=[DataRequired()]);

    submit = SubmitField('Post Contact')


class LoginForm(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Log in')
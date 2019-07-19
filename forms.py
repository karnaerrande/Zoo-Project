from flask_wtf import FlaskForm
from wtforms import Form, FileField, BooleanField, TextAreaField, StringField, SubmitField, validators
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField

"""
Args:
    self(animal): animal object
    fields(string[]): fields for the animal
    args(string[]): args for each field
"""
class Animal:
    def _init_(self, name, img_url, dist, desc, breeding, diet, behavior, status, fact):
        #TODO: Implement
        return 0

class AnimalForm(FlaskForm):
    name_animal = StringField(u'Animal Name',
                                validators=[DataRequired(), Length(min=2, max=30)])
    names =  StringField(u'Names',
                                validators=[DataRequired(), Length(min=2, max=30)])
    img_url = FileField()
    dist_animal = TextAreaField(u'Distribution', [validators.optional(), validators.length(max=400)])
    desc_animal = TextAreaField(u'Description', [validators.optional(), validators.length(max=400)])

    breed_animal = TextAreaField(u'Breeding', [validators.optional(), validators.length(max=1000)])
    diet_animal = TextAreaField(u'Diet', [validators.optional(), validators.length(max=300)])
    behavior_animal = TextAreaField(u'Behavior', [validators.optional(), validators.length(max=400)])
    status_animal = StringField(u'Animal Status',
                                validators=[DataRequired(), Length(min=2, max=30)])

    fact_animal = TextAreaField(u'Fact', [validators.optional(), validators.length(max=300)])

    submit = SubmitField('Post')


    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)

    def upload(request):
        form = UploadForm(request.POST)

        if form.image.data:
            image_data = request.FILES[form.image.name].read()
            open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)



class ContactForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired(), Length(min=2, max=40)])

    # email = StringField("Your email",  validators=[DataRequired(), Email("This field requires a valid email address")])
    # email = EmailField('Your email', validators=[DataRequired(), Email("This field requires a valid email address")])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=2, max=40)])

    message = TextAreaField('Message', validators=[DataRequired()]);

    submit = SubmitField('Post Contact')

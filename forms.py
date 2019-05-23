from flask_wtf import FlaskForm
from wtforms import Form, FileField, BooleanField, TextAreaField, StringField, SubmitField, validators
from wtforms.validators import DataRequired, Length

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

    desc_animal = TextAreaField(u'Animal Description', [validators.optional(), validators.length(max=400)])
    
    submit = SubmitField('Post Animal')

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)
    
    def upload(request):
        form = UploadForm(request.POST)

        if form.image.data:
            image_data = request.FILES[form.image.name].read()
            open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)
    
from wtforms import Form, StringField, TextAreaField, validators

class SubmissionForm(Form):
    subdeslen = StringField('deslen', [validators.Length(min=0, max=50)])
    subprice_range = StringField('price_range', [validators.Length(min=0, max=50)])
    subvariety = StringField('variety', [validators.Length(min=0, max=50)])
    subprovince = StringField('province', [validators.Length(min=0, max=50)])
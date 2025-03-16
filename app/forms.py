from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    poster = FileField("Poster", validators=[FileAllowed(['jpg', 'jpeg', 'png'], "Only JPG, PNG and JPEG Files Allowed!")])

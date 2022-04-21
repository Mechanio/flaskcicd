from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class MainForm(FlaskForm):
    text = StringField(validators=[InputRequired()])

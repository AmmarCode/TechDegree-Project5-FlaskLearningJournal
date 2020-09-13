from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

from models import Post

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    date = DateTimeField("Date", format="%m/%d/%Y", validators=[DataRequired()])
    time_spent = IntegerField("Time Spent (Minutes)", validators=[DataRequired()])
    learned = TextAreaField('What You Learned', validators=[DataRequired()])
    resources = TextAreaField('Resources to remember', validators=[DataRequired()])
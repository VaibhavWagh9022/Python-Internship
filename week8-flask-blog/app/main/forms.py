from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SearchForm(FlaskForm):
    q      = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')


class ContactForm(FlaskForm):
    name    = StringField('Name',    validators=[DataRequired(), Length(1, 100)])
    email   = StringField('Email',   validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(1, 200)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(10, 2000)])
    submit  = SubmitField('Send Message')

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class PostForm(FlaskForm):
    title     = StringField('Title',   validators=[DataRequired(), Length(1, 200)])
    slug      = StringField('Slug (URL-friendly)', validators=[DataRequired(), Length(1, 200)])
    summary   = TextAreaField('Summary (optional)', validators=[Optional(), Length(0, 500)])
    content   = TextAreaField('Content', validators=[DataRequired()])
    category  = SelectField('Category', coerce=int, validators=[Optional()])
    tags      = StringField('Tags (comma-separated)', validators=[Optional()])
    image     = FileField('Cover Image', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webp'], 'Images only!')
    ])
    published = BooleanField('Publish immediately', default=True)
    submit    = SubmitField('Save Post')

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    content = TextAreaField(
        'Leave a comment',
        validators=[DataRequired(), Length(1, 1000)],
        render_kw={"rows": 4, "placeholder": "Write your comment here…"}
    )
    submit = SubmitField('Post Comment')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    email       = StringField('Email',    validators=[DataRequired(), Email()])
    password    = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username         = StringField('Username',        validators=[DataRequired(), Length(3, 64)])
    email            = StringField('Email',           validators=[DataRequired(), Email(), Length(1, 120)])
    password         = PasswordField('Password',      validators=[DataRequired(), Length(8, 128)])
    password2        = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match.')
    ])
    submit           = SubmitField('Register')

    # Custom validators — called automatically by WTForms
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken. Please choose a different one.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered. Please use a different one.')


class EditProfileForm(FlaskForm):
    username  = StringField('Username', validators=[DataRequired(), Length(3, 64)])
    about_me  = TextAreaField('About Me', validators=[Length(0, 500)])
    submit    = SubmitField('Save Changes')

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, field):
        if field.data != self.original_username:
            if User.query.filter_by(username=field.data).first():
                raise ValidationError('Username already taken.')


class ChangePasswordForm(FlaskForm):
    old_password  = PasswordField('Current Password', validators=[DataRequired()])
    new_password  = PasswordField('New Password',     validators=[DataRequired(), Length(8, 128)])
    new_password2 = PasswordField('Confirm New Password', validators=[
        DataRequired(), EqualTo('new_password', message='Passwords must match.')
    ])
    submit        = SubmitField('Update Password')

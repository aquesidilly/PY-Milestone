
from flask import Flask
from flask import FlaskForm
from flask import WTforms
from flask_wtf import FlaskForm
from WTForms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=4, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Repeat Password')
    email = StringField('Email Address', validators=[Length(min=6, max=35), Email()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')


class CreateMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    short_description = TextAreaField('Short Description', validators=[DataRequired()])
    collections = TextAreaField('collections (one per line please)', validators=[DataRequired()])
    method = TextAreaField('Instructions', validators=[DataRequired()])
    tags = StringField('Tags (separate by comma please)', validators=[DataRequired()])
    image = StringField('Image Link (full path)', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class EditMovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    short_description = TextAreaField('Short Description', validators=[DataRequired()])
    Ingredients = TextAreaField('Collections (one per line please)', validators=[DataRequired()])
    method = TextAreaField('Instructions', validators=[DataRequired()])
    tags = StringField('Tags (separate by comma please)', validators=[DataRequired()])
    image = StringField('Image Link (full path)', validators=[DataRequired()])
    submit = SubmitField('Update Movie')


class ConfirmDelete(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Delete this Movie')
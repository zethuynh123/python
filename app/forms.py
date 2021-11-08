from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  
    password = PasswordField('Password', validators=[DataRequired()])
    repassword = PasswordField('Repeat Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submitt = SubmitField('Sign Up')
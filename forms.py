from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationFrom(FlaskForm):
	
	username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Length(min=2, max=50),Email()])
	password = PasswordField('password', validators=[DataRequired(), Length(min=2, max=50)])
	confirm_password = PasswordField('confirm_password', validators=[DataRequired(), Length(min=2, max=50),EqualTo('password')])
	submit = SubmitField('Sign up')
    

class LoginFrom(FlaskForm):
	
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('login')


from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationFrom, LoginFrom
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '221b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	username= db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.png')
	post = db.relationship('Post', backref='author', lazy=True)
	
    
def __repr__(self):

    	return f"User('{self.username}', '{self.email}', '{self.image_file}')"
 

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text , nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
   

def __repr__(self):
        return  f"Post('{self.title}',  '{self.date_posted}')"







posts = [

{
	'author':'john titor',
	'title':'blog post 1',
	'content': 'First post',
	'date':'18.01.2000'

},
{
	'author':'abhil',
	'title':"2 nd post",
	'content':'second post',
	'date':'10.12.1999'
}


]


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)




@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
    	if form.email.data == 'admin@blog.com' and form.password.data == '123456':
    		flash(f'You have been logged in successfully ', 'success')
    		return redirect(url_for('home'))
    	else:
    		flash('WTF something is wrong ', 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationFrom()
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data} !', 'success')
    	return redirect(url_for('home'))
    return render_template('registration.html', title="Register", form=form)


if __name__=='__main__':
	app.run(debug=True)
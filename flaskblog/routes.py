# This file job is create routes only
from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Verappan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Sep 10, 2020'
    },
    {
        'author': 'Harikrishna',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Sep 11, 2018'
    },
    {
        'author': 'Prabhakaran',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'Sep 12, 2018'
    },
    {
        'author': 'Verappan',
        'title': 'Blog Post 4',
        'content': 'First post content',
        'date_posted': 'Sep 13, 2020'
    },
    {
        'author': 'Harikrishna',
        'title': 'Blog Post 5',
        'content': 'Second post content',
        'date_posted': 'Sep 13, 2018'
    },
    {
        'author': 'Prabhakaran',
        'title': 'Blog Post 6',
        'content': 'Third post content',
        'date_posted': 'Sep 14, 2018'
    }

]


# urls part in flask
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


# url for about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')


# url for register page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


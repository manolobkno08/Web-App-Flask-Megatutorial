#!/usr/bin/python3
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Master'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Redirect and capture data from form submitted"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f'Login requested for user: {form.username.data}, remember_me: {form.remember_me.data}')
        print("Data capture successful")
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)

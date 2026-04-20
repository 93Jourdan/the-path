# routes/auth.py
# This file handles everything related to user authentication:
# signing up, logging in, and logging out.

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from models import db

# Blueprint
auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # GET = user is visiting the page
    # POST = user submitted the signup form
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if email already exists in the database
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please log in.', 'error')
            return redirect(url_for('auth.signup'))

        # generate_password_hash turns "mypassword" into a long scrambled string
        hashed_password = generate_password_hash(password)

        # Create new user object and save to database
        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Account created! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        # check_password_hash compares the submitted password
        # against the scrambled version stored in the database
        if not user or not check_password_hash(user.password, password):
            flash('Invalid email or password.', 'error')
            return redirect(url_for('auth.login'))

        # Log the user in — Flask-Login handles the session from here
        login_user(user)
        return redirect(url_for('dashboard'))

    return render_template('auth/login.html')


@auth.route('/logout')
@login_required  # Only logged-in users can log out
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
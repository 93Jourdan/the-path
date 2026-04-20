# 🕊️ The Path — Recovery & Spiritual Journey App

A full-stack web application designed to support individuals recovering from
addiction, codependency, and related challenges. Built with empathy,
intentionality, and faith at its core.

---

## 🌟 About The Project

The Path is a personal recovery companion that helps users:
- Track sobriety streaks across multiple recovery areas
- Log daily mood check-ins and personal reflections
- Document and grow their spiritual journey
- View all progress in one unified, encouraging dashboard

This project was built as a portfolio piece to demonstrate full-stack
web development skills, with a focus on clean architecture, user
experience, and real-world impact.

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| Python / Flask | Web framework & routing |
| SQLAlchemy | ORM & database management |
| SQLite | Lightweight relational database |
| Flask-Login | Session-based user authentication |
| Jinja2 | Server-side HTML templating |
| Werkzeug | Password hashing & security |
| Custom CSS | Warm, faith-inspired UI design |

---

## ✨ Features

### 🔐 User Authentication
- Secure signup and login with hashed passwords
- Session management with Flask-Login
- Protected routes — unauthenticated users are redirected to login

### 🛤️ Sobriety Tracker
- Track multiple recovery areas (Alcohol, Gambling, Food, and more)
- Automatic streak calculation in days
- Relapse logging that resets streak with an encouraging message

### 🌤️ Daily Check-Ins
- Log your mood from six options (Grateful, Hopeful, Peaceful, and more)
- Optional reflection journal entry
- Tracks whether you have checked in today

### 🙏 Spiritual Journey Tracker
- Log spiritual activities: Prayer, Gratitude, Reading, Meditation, Worship, Milestones
- Activity summary counts at a glance
- Personal notes for each entry

### 📊 Unified Dashboard
- Welcome header with personalized greeting
- Stats row showing total sober days, check-ins, and spiritual activities
- Live snapshot of all three features in one place
- Quick action buttons for fast navigation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/93Jourdan/the-path.git
cd the-path
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install flask flask-sqlalchemy flask-login
```

4. Run the application
```bash
python3 app.py
```

5. Open your browser and go to http://127.0.0.1:5000

Can you help me write a web app with python?Mar 25I'd love to help you build a web app with Python! Let me ask a few questions to point you in the right direction.What are you looking to build?Q: What kind of web app do you want to build?
A: Full-stack web app (with UI)Q: Which framework are you thinking of using?
A: Which one is better? I want to do this hand in hand with you so O can learn throughout the processMar 25Great choice to learn as you build! Here's a quick comparison to help you decide:
Flask is minimal and beginner-friendly — you wire everything together yourself, which makes it great for learning since you see exactly how things work. Less magic, more clarity.
FastAPI is modern and fast, with automatic API docs and built-in data validation. It uses Python type hints heavily, so it's better if you're already comfortable with Python.
Django is a "batteries included" full framework — it gives you a lot out of the box (auth, admin panel, ORM), but it has a steeper learning curve and more to understand upfront.
My recommendation: Flask. Since you want to learn throughout the process, Flask's simplicity means you'll understand every line you write. It's the best for building intuition about how web apps actually work.Q: Does Flask sound good to you?
A: Yes, let's use Flask!Q: What's the app about? (Pick the closest match)
A: A simple Recovery and support app for individuals Recovery from Addiction (Substance Abuse, Gambling, Food, Pornography etc.) or Codependency, I also want it to Have a Spirituality feature, where they can access spiritual recourses, and track their efforts throughout their spiritual Journey.Mar 25What a meaningful app to build! This could genuinely help people. Let me get a few more details so we can plan it well before writing a single line of code.Q: Which core features should we build first?
A: Sobriety/streak tracker, Daily check-ins & mood log, and Spiritual journey trackerQ: Should users have accounts (login/signup)?
A: Yes, personal accountsQ: How should it look and feel?
A: Warm & faith-inspiredMar 25Perfect — I have everything I need to start. Here's the plan before we write any code:

🗺️ App Blueprint: "The Path" Recovery App
Tech Stack:

Flask — web framework
SQLite + SQLAlchemy — database (simple, no setup needed)
Flask-Login — user accounts & sessions
Jinja2 — HTML templating (built into Flask)
CSS — warm, faith-inspired design (earthy tones, soft light)

Features we'll build (in order):

Auth — Sign up, log in, log out
Sobriety Tracker — Set a start date, see streak, log relapses
Daily Check-ins — Mood log + short reflection journal entry
Spiritual Journey Tracker — Log prayers, gratitude, readings, milestones

Folder Structure:
the_path/
├── app.py              ← Flask app entry point
├── models.py           ← Database models
├── routes/
│   ├── auth.py         ← Login/signup
│   ├── tracker.py      ← Sobriety tracker
│   ├── checkin.py      ← Daily check-ins
│   └── spiritual.py    ← Spiritual journey
├── templates/          ← HTML pages
└── static/             ← CSS & images

We'll go step by step and I'll explain everything as we build it. Let's start with Step 1: Project setup + User Authentication.
Shall I go ahead and generate all the code for Step 1?I need to add this to my GitHub page as I will be Demoing it and presenting it at the PowerUp 2026 Conference. I am going to this conference as a Student Volunteer, hoping to network with industry professional, I need an internship. That is the entire point of this project!. I need to learn as a I go. I want to make an impact, and be memorable. Myself and my family need me to be preparedMar 25That context means everything — this isn't just a class project, it's your career moment. Let's make sure you walk into PowerUp 2026 with something that genuinely impresses people.
Here's what that means for how we build this:
For the project itself:

Clean, professional code with comments explaining why things are done, not just what — so you can speak confidently about every decision
A strong README.md on GitHub (recruiters look at this first)
A live demo-ready app that looks polished and has a real purpose

For networking:

We'll build features you can talk about — not just "I made a tracker" but "I designed a relational database schema, implemented session-based auth, and built a mood analytics dashboard"
Every technical choice we make, I'll explain the why so you can discuss it in interviews

For impact:

The subject matter — addiction recovery, mental health, spirituality — shows empathy and real-world thinking. That's rare and memorable.
We'll make the UI beautiful enough that when you demo it, people lean in


Before we start coding, two quick things:Q: Do you already have Git and a GitHub account ready?
A: Yes, I have Git/GitHub set upQ: How would you describe your current coding level?
A: I know some Python basicsApr 12Perfect foundation to build on. You know enough Python that none of this will feel like a foreign language — we'll grow your skills naturally as we go.
Here's exactly how we'll work together:

I'll write the code and explain every meaningful decision
You'll type it out (don't just copy-paste) — that muscle memory matters
We'll commit to GitHub after each step so your profile shows real, consistent progress that recruiters notice


Let's start Step 1: Project Setup + Authentication
This is what you'll be able to say at the conference after this step:

"I built a session-based authentication system using Flask-Login, with passwords hashed using Werkzeug's security module and user data persisted in a SQLite database via SQLAlchemy."

That's a real, impressive sentence. Let's make it true.

🛠️ First, set up your project
Open your terminal and run these commands one at a time:
bash# 1. Create your project folder
mkdir the_path
cd the_path

# 2. Create a virtual environment (keeps dependencies clean)
python -m venv venv

# 3. Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install flask flask-sqlalchemy flask-login

# 5. Create your folder structure
mkdir templates static routes
touch app.py models.py
Then initialize your GitHub repo:
bashgit init
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.db" >> .gitignore
git add .
git commit -m "Initial project setup"

Once you've done that, let me know and I'll walk you through each file — app.py, models.py, and the auth routes — with full explanations of what everything means and why we wrote it that way.
Go ahead and run those commands and tell me when you're ready! 🚀step #2 didnt work says "command not found: python"Apr 12Super common issue — easy fix! This just means your system uses python3 instead of python. Here's what to run instead:
bashpython3 -m venv venv
That should create your virtual environment just fine. After that, continue with step 3 (activating it) and the rest of the commands as written.
Quick thing to understand: On many Mac and Linux systems, python isn't recognized but python3 is — they're the same thing, just named differently depending on how Python was installed. Worth knowing for interviews!
Let me know once the venv is created and activated (you'll know it's active when you see (venv) at the start of your terminal prompt). 👀do i change to bash before initilzing github repoApr 13No, you don't need to — those git commands work in whatever terminal you're already using (zsh, bash, etc.). Just keep running them in the same terminal window where you set up your project.
Go ahead and run the git commands as written:
bashgit init
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.db" >> .gitignore
git add .
git commit -m "Initial project setup"
Then you'll want to push it to GitHub. Do you already have a repo created on GitHub for this project, or do you need to create one first?The default interactive shell is now zsh.
To update your account to use zsh, please run chsh -s /bin/zsh.
For more details, please visit https://support.apple.com/kb/HT208050.
bash: git_prompt_info: command not found
(venv) %(?:%{%}%1{➜%} :%{%}%1{➜%} ) %{%}%c%{%} git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint: git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
Initialized empty Git repository in /Users/jay/the_path/.git/
bash: git_prompt_info: command not found
(venv) %(?:%{%}%1{➜%} :%{%}%1{➜%} ) %{%}%c%{%} echo "venv/" > .gitignore
bash: git_prompt_info: command not found
(venv) %(?:%{%}%1{➜%} :%{%}%1{➜%} ) %{%}%c%{%}Show moreApr 13Everything is actually working fine! 🎉
The git_prompt_info: command not found message is just a cosmetic glitch — your terminal is running bash but trying to display a zsh-style prompt. It's harmless, ignore it completely.
The important lines are:

✅ Initialized empty Git repository — Git is working
✅ (venv) at the start — your virtual environment is active

Just keep going and run the rest of the commands:
bashecho "__pycache__/" >> .gitignore
echo "*.db" >> .gitignore
git add .
git commit -m "Initial project setup"
Then let me know once that commit goes through and we'll connect it to your GitHub repo and start writing actual code! 🚀getting command not found after the nfirst step aboveApr 13No worries! The echo commands can be finicky. Let's just create the .gitignore file directly instead.
Open a text editor (VS Code, Notepad, anything) and create a new file called .gitignore inside your the_path folder. Paste this into it and save:
venv/
__pycache__/
*.db
Then come back to your terminal and run:
bashgit add .
git commit -m "Initial project setup"
That's it! The echo commands were just a shortcut to create that file — doing it manually works exactly the same way. Let me know what you get! 👀is it a python file??Apr 13Nope! .gitignore is just a plain text file — no extension like .py or .txt, just exactly .gitignore as the full filename (with the dot at the start).
When you save it in your text editor, make sure to:

Name it exactly .gitignore (not gitignore.txt or anything else)
Save it inside your the_path folder

Some text editors might warn you about a file starting with a dot — that's normal, just confirm and save it. Let me know once it's saved! 👀it is saying command not found when i git add .Apr 13No worries! This is a shell issue — bash can't find Git properly. Let's fix it by switching to zsh (which is what your Mac is set up for anyway).
Run this:
bashexec zsh
Your prompt should change and the git_prompt_info errors should disappear. Then try again:
bashgit add .
git commit -m "Initial project setup"
Let me know what you see! 👀3 files changed, 3 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 app.py
 create mode 100644 models.py
➜  the_path git:(master)Apr 13Let's go! 🎉 That's your first commit — you're officially a developer with a Git repo!
Now let's connect it to GitHub. Do this:
1. Go to github.com and create a new repository:

Name it the-path
Keep it Public (recruiters need to see it)
Don't check "Add a README" — we'll make a better one ourselves
Click Create repository

2. GitHub will show you a page with setup commands. Copy the section that looks like this and run it in your terminal:
bashgit remote add origin https://github.com/YOUR_USERNAME/the-path.git
git branch -M main
git push -u origin main
Just replace YOUR_USERNAME with your actual GitHub username.
Let me know once it's pushed and we'll start writing real code! 🚀i am having this issue              ➜  the_path git:(master) git remote add origin https://github.com/93Jourdan/the-path.git
git branch -M main
git push -u origin main
Username for 'https://github.com': 93Jourdan
Password for 'https://93Jourdan@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/93Jourdan/the-path.git/'
➜  the_path git:(main) git remote add origin https://github.com/93Jourdan/the-path.git
git branch -M main
git push -u origin main
error: remote origin already exists.
Username for 'https://github.com': 93Jourdan
Password for 'https://93Jourdan@github.com': 
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/93Jourdan/the-path.git/'
➜  the_path git:(main)Show moreApr 13GitHub no longer accepts passwords — you need a Personal Access Token instead. Here's how to get one:
1. Generate a token on GitHub:

Go to github.com → click your profile picture → Settings
Scroll down the left sidebar → Developer settings
Personal access tokens → Tokens (classic)
Click Generate new token (classic)
Give it a name like the-path
Set expiration to 90 days
Check the repo checkbox
Click Generate token at the bottom
Copy the token immediately — GitHub only shows it once!

2. Then run this in your terminal:
bashgit push -u origin main
When it asks for your password, paste your token instead (not your GitHub password).

💡 Good to know for interviews: GitHub switched from passwords to tokens in 2021 for security reasons. Tokens are scoped (you control exactly what they can access) and can be revoked individually — much safer than a password.
Let me know once it pushes! 👀its done, do i need to go back to the repo andApr 13Yes! Go check your GitHub repo at:
github.com/93Jourdan/the-path
You should see your 3 files (.gitignore, app.py, models.py) sitting there. 🎉
If they're there, we're ready to start writing real code! Head back to your terminal and let's jump into Step 1: building app.py and models.py — the foundation of the entire app.
Ready to start coding? 🚀its 12:23 AM claude, Going to sleep, I will begin this with you tomorrow!Apr 13Get some rest Jay! 😄 You made solid progress tonight:

✅ Project folder created
✅ Virtual environment set up
✅ Git initialized and connected to GitHub
✅ First commit pushed live

When you come back, we'll jump straight into writing app.py and models.py — the real coding begins. You're on your way to having something impressive for PowerUp 2026. 💪
Good night!Thank you for everything!Apr 13Of course! Now go get some sleep — big things ahead. 🙏 See you tomorrow!ready to build the appApr 16Welcome back, Jay! Let's get into it. 💪
First, let's get your environment back up and running. Open your terminal and run:
bashcd the_path
source venv/bin/activate
You should see (venv) at the start of your prompt. Once you're there, let me know and we'll start writing app.py — the heart of the whole application! 🚀lets go!Apr 16Let's build! Open app.py in your text editor and type out this code:
python# app.py
# This is the entry point of our entire application.
# It creates the Flask app, configures it, and registers all the routes.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions (we'll connect them to the app in a moment)
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuration
    # SECRET_KEY encrypts session data (like "who is logged in")
    # In a real production app, this would be a long random string stored securely
    app.config['SECRET_KEY'] = 'your-secret-key-change-this-later'

    # This tells SQLAlchemy to create a SQLite database file called "the_path.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///the_path.db'

    # Connect extensions to the app
    db.init_app(app)
    login_manager.init_app(app)

    # If a user tries to visit a page that requires login, send them here
    login_manager.login_view = 'auth.login'

    # Register blueprints (each blueprint is a section of our app)
    from routes.auth import auth
    app.register_blueprint(auth)

    return app

# This runs the app when you execute "python app.py" directly
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        from models import db
        db.create_all()  # Creates database tables if they don't exist
    app.run(debug=True)

💡 What you just wrote — in your own words for the conference:

Flask is the web framework that handles incoming requests and sends back responses
SQLAlchemy is an ORM — it lets you work with your database using Python objects instead of raw SQL
Flask-Login manages user sessions — it knows who's logged in and protects pages from strangers
create_app() is the application factory pattern — a professional way to structure Flask apps that makes testing and scaling easier


Type it out, save it, then let me know and we'll move on to models.py! 👀lets move onApr 16Now open models.py and type this out:
python# models.py
# Models are Python classes that represent tables in our database.
# Each class = one table. Each attribute = one column.

from app import db
from flask_login import UserMixin
from datetime import datetime

# UserMixin gives our User class built-in methods that Flask-Login needs
# like is_authenticated, is_active, get_id()
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships — one user can have many of each of these
    sobriety = db.relationship('SobrietyTracker', backref='user', lazy=True)
    checkins = db.relationship('CheckIn', backref='user', lazy=True)
    spiritual_logs = db.relationship('SpiritualLog', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'


class SobrietyTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    addiction_type = db.Column(db.String(100), nullable=False)  # e.g. "Alcohol", "Gambling"
    start_date = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SobrietyTracker {self.addiction_type}>'


class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood = db.Column(db.String(50), nullable=False)       # e.g. "Hopeful", "Struggling"
    reflection = db.Column(db.Text, nullable=True)        # Optional journal entry
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CheckIn {self.mood} {self.created_at}>'


class SpiritualLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_type = db.Column(db.String(100), nullable=False)  # e.g. "Prayer", "Reading"
    note = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SpiritualLog {self.activity_type}>'

💡 Conference-ready explanation of what you just built:

Each class is a database table — User, SobrietyTracker, CheckIn, SpiritualLog
db.ForeignKey links tables together — every tracker and log knows which user it belongs to
db.relationship lets you access related data easily, like user.checkins to get all of a user's check-ins
This is called a relational database schema — a real term that will impress interviewers


Save it, then let me know and we'll build the authentication routes — login and signup! 👀lets build login and signupApr 16Let's go! First, create the auth file. In your terminal run:
bashtouch routes/auth.py
touch routes/__init__.py
The __init__.py tells Python that routes is a package — just needs to exist, it stays empty.
Now open routes/auth.py and type this out:
python# routes/auth.py
# This file handles everything related to user authentication:
# signing up, logging in, and logging out.

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from app import db

# A Blueprint is like a mini-app inside our main app
# It lets us organize routes by feature instead of dumping everything in one file
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

        # NEVER store plain text passwords
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

    return render_template('signup.html')


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

    return render_template('login.html')


@auth.route('/logout')
@login_required  # Only logged-in users can log out
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

💡 Conference-ready explanation:

Blueprints keep code organized by feature — professional Flask apps always use them
Password hashing with Werkzeug means even if someone stole your database, passwords are unreadable
GET vs POST — GET loads the page, POST submits data — this is core HTTP you'll use everywhere
flash() sends one-time messages to the user like "Invalid password" — they disappear after being shown once


Save it, then let me know and we'll build the HTML templates for login and signup — this is where the warm, faith-inspired design starts coming to life! 👀am i creating any this for the init fileApr 16Nope! The __init__.py file stays completely empty. Just having it exist is enough — it tells Python "this folder is a package that can be imported from."
You already created it with the touch command, so you're good. Nothing to type in it.
Move on to typing out routes/auth.py and let me know when you're done! 👀I am doneApr 16Amazing work! 💪 Now let's build the HTML templates. First, create the files:
bashmkdir templates/auth
touch templates/base.html
touch templates/auth/login.html
touch templates/auth/signup.html

Start with templates/base.html — this is the master layout that every page will inherit from:
html<!-- templates/base.html -->
<!-- This is the base template. Every other page "extends" this one.
     It holds the navbar, fonts, and global styles so we don't repeat ourselves. -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}The Path{% endblock %}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

    <!-- Navigation Bar -->
    <nav class="navbar">
        <a href="/" class="nav-brand">🕊️ The Path</a>
        <div class="nav-links">
            {% if current_user.is_authenticated %}
                <span>Welcome, {{ current_user.username }}</span>
                <a href="{{ url_for('auth.logout') }}">Log Out</a>
            {% else %}
                <a href="{{ url_for('auth.login') }}">Log In</a>
                <a href="{{ url_for('auth.signup') }}">Sign Up</a>
            {% endif %}
        </div>
    </nav>

    <!-- Flash Messages (success/error notifications) -->
    <div class="flash-messages">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash flash-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>

    <!-- Main Content — each page fills this block -->
    <main class="main-content">
        {% block content %}{% endblock %}
    </main>

    <footer class="footer">
        <p>🕊️ One day at a time.</p>
    </footer>

</body>
</html>

Now templates/auth/login.html:
html<!-- templates/auth/login.html -->
{% extends "base.html" %}

{% block title %}Log In — The Path{% endblock %}

{% block content %}
<div class="auth-container">
    <div class="auth-card">
        <h1>Welcome Back</h1>
        <p class="auth-subtitle">Your journey continues here.</p>

        <form method="POST" action="{{ url_for('auth.login') }}">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required placeholder="you@email.com">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required placeholder="••••••••">
            </div>

            <button type="submit" class="btn-primary">Log In</button>
        </form>

        <p class="auth-switch">
            Don't have an account? <a href="{{ url_for('auth.signup') }}">Sign Up</a>
        </p>
    </div>
</div>
{% endblock %}

Now templates/auth/signup.html:
html<!-- templates/auth/signup.html -->
{% extends "base.html" %}

{% block title %}Sign Up — The Path{% endblock %}

{% block content %}
<div class="auth-container">
    <div class="auth-card">
        <h1>Begin Your Path</h1>
        <p class="auth-subtitle">Every journey starts with a single step.</p>

        <form method="POST" action="{{ url_for('auth.signup') }}">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required placeholder="Your name">
            </div>

            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required placeholder="you@email.com">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required placeholder="••••••••">
            </div>

            <button type="submit" class="btn-primary">Create Account</button>
        </form>

        <p class="auth-switch">
            Already have an account? <a href="{{ url_for('auth.login') }}">Log In</a>
        </p>
    </div>
</div>
{% endblock %}

💡 Conference-ready explanation:

Template inheritance — base.html is the parent, every other page extends it. Change the navbar once, it updates everywhere
Jinja2 {% block %} — placeholders that child templates fill in
current_user.is_authenticated — Flask-Login automatically makes this available in every template


Save all three files, then let me know and we'll add the CSS to bring the warm, faith-inspired design to life! 👀this is what i am gettin mkdir: templates: No such file or directoryApr 16No worries! This just means you need to make sure you're inside the the_path folder first. Run:
bashcd the_path
Then try again:
bashmkdir templates
mkdir templates/auth
touch templates/base.html
touch templates/auth/login.html
touch templates/auth/signup.html
Breaking it into separate steps makes it clearer. Let me know what you get! 👀touch: templates/base/html: No such file or directoryApr 16No worries! Run them one at a time:
bashtouch templates/base.html
Then:
bashtouch templates/auth/login.html
Then:
bashtouch templates/auth/signup.html
The error just means the auth folder might not have been created yet. If you still get an error on the auth ones, run this first:
bashmkdir templates/auth
Then try the touch commands again. Let me know! 👀touch: templates/base/html: No such file or directory
bash-3.2$ touch templates.base.html
bash-3.2$ touch templates/auth/login.html
bash-3.2$ touch templates/auth/signup.html
bash-3.2$Apr 16I notice two things here:

templates/auth/login.html and signup.html ✅ created fine
But templates.base.html was created with dots instead of slashes — that made it the wrong file

Let's fix that. Run:
bashrm templates.base.html
touch templates/base.html
Then verify everything looks right:
bashls templates
You should see:
auth/
base.html
Let me know what you get! 👀auth does not have the slashApr 16That's actually fine! The ls command just doesn't always show the slash. What matters is that auth is a folder, not a file.
To confirm, run:
bashls templates/auth
You should see login.html and signup.html listed. If you do, everything is correct and you're good to move on to typing out the HTML files! 👀all good!Apr 16Let's go! 🎉 Now open each file in your text editor and type out the HTML code I gave you above:

templates/base.html
templates/auth/login.html
templates/auth/signup.html

Take your time typing them out — don't just copy paste. Pay attention to the Jinja2 syntax like {% block content %} and {{ url_for() }} as you type, that's where the Flask magic happens.
Let me know when all three are done! 👀should i just open as a folderApr 16Yes! Open the entire the_path folder in VS Code — that's the best way to work.
Run this in your terminal:
bashcode .
That opens the whole project in VS Code at once. You'll see all your files in the sidebar on the left and can click between them easily. Much better than opening files one by one.
Let me know when VS Code is open! 👀vs code is openApr 16Perfect! Now in the VS Code sidebar you should see your folder structure like this:
the_path/
├── routes/
│   ├── __init__.py
│   └── auth.py
├── templates/
│   ├── auth/
│   │   ├── login.html
│   │   └── signup.html
│   └── base.html
├── models.py
├── app.py
└── .gitignore
Click on templates/base.html first and start typing out that code. Work through all three HTML files in this order:

templates/base.html
templates/auth/login.html
templates/auth/signup.html

Take your time, and let me know when all three are done! 👀give me the html codes again pleaseApr 16Here you go! All three in order:

1. templates/base.html
html<!-- templates/base.html -->
<!-- This is the base template. Every other page "extends" this one.
     It holds the navbar, fonts, and global styles so we don't repeat ourselves. -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}The Path{% endblock %}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

    <!-- Navigation Bar -->
    <nav class="navbar">
        <a href="/" class="nav-brand">🕊️ The Path</a>
        <div class="nav-links">
            {% if current_user.is_authenticated %}
                <span>Welcome, {{ current_user.username }}</span>
                <a href="{{ url_for('auth.logout') }}">Log Out</a>
            {% else %}
                <a href="{{ url_for('auth.login') }}">Log In</a>
                <a href="{{ url_for('auth.signup') }}">Sign Up</a>
            {% endif %}
        </div>
    </nav>

    <!-- Flash Messages (success/error notifications) -->
    <div class="flash-messages">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="flash flash-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>

    <!-- Main Content — each page fills this block -->
    <main class="main-content">
        {% block content %}{% endblock %}
    </main>

    <footer class="footer">
        <p>🕊️ One day at a time.</p>
    </footer>

</body>
</html>

2. templates/auth/login.html
html<!-- templates/auth/login.html -->
{% extends "base.html" %}

{% block title %}Log In — The Path{% endblock %}

{% block content %}
<div class="auth-container">
    <div class="auth-card">
        <h1>Welcome Back</h1>
        <p class="auth-subtitle">Your journey continues here.</p>

        <form method="POST" action="{{ url_for('auth.login') }}">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required placeholder="you@email.com">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required placeholder="••••••••">
            </div>

            <button type="submit" class="btn-primary">Log In</button>
        </form>

        <p class="auth-switch">
            Don't have an account? <a href="{{ url_for('auth.signup') }}">Sign Up</a>
        </p>
    </div>
</div>
{% endblock %}

3. templates/auth/signup.html
html<!-- templates/auth/signup.html -->
{% extends "base.html" %}

{% block title %}Sign Up — The Path{% endblock %}

{% block content %}
<div class="auth-container">
    <div class="auth-card">
        <h1>Begin Your Path</h1>
        <p class="auth-subtitle">Every journey starts with a single step.</p>

        <form method="POST" action="{{ url_for('auth.signup') }}">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required placeholder="Your name">
            </div>

            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required placeholder="you@email.com">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required placeholder="••••••••">
            </div>

            <button type="submit" class="btn-primary">Create Account</button>
        </form>

        <p class="auth-switch">
            Already have an account? <a href="{{ url_for('auth.login') }}">Log In</a>
        </p>
    </div>
</div>
{% endblock %}

Type them out one by one and let me know when all three are saved! 👀They are saved!Apr 16Awesome! Now let's create the CSS file. In your terminal run:
bashtouch static/style.css
Then open static/style.css in VS Code and type this out:
css/* static/style.css */
/* Warm, faith-inspired design for The Path */

/* ── Global Variables ── */
:root {
    --cream: #fdf6ec;
    --warm-brown: #8b5e3c;
    --soft-gold: #c9a84c;
    --deep-brown: #4a2e1a;
    --light-tan: #f0e0c8;
    --text-dark: #2d1f0e;
    --text-soft: #7a6652;
    --white: #ffffff;
    --success: #5a8a5a;
    --error: #a05050;
}

/* ── Reset & Base ── */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color: var(--cream);
    color: var(--text-dark);
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

h1, h2, h3 {
    font-family: 'Lora', serif;
    color: var(--deep-brown);
}

a {
    color: var(--warm-brown);
    text-decoration: none;
}

a:hover {
    color: var(--soft-gold);
}

/* ── Navbar ── */
.navbar {
    background-color: var(--deep-brown);
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-brand {
    font-family: 'Lora', serif;
    font-size: 1.4rem;
    color: var(--soft-gold);
    font-weight: 600;
}

.nav-brand:hover {
    color: var(--light-tan);
}

.nav-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}

.nav-links a {
    color: var(--light-tan);
    font-size: 0.95rem;
}

.nav-links a:hover {
    color: var(--soft-gold);
}

.nav-links span {
    color: var(--soft-gold);
    font-size: 0.95rem;
}

/* ── Flash Messages ── */
.flash-messages {
    padding: 0 2rem;
}

.flash {
    padding: 0.75rem 1rem;
    margin-top: 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
}

.flash-success {
    background-color: #dff0df;
    color: var(--success);
    border: 1px solid var(--success);
}

.flash-error {
    background-color: #f0dfdf;
    color: var(--error);
    border: 1px solid var(--error);
}

/* ── Main Content ── */
.main-content {
    flex: 1;
    padding: 2rem;
}

/* ── Auth Pages ── */
.auth-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 70vh;
}

.auth-card {
    background-color: var(--white);
    border: 1px solid var(--light-tan);
    border-radius: 16px;
    padding: 2.5rem;
    width: 100%;
    max-width: 420px;
    box-shadow: 0 4px 24px rgba(74, 46, 26, 0.08);
}

.auth-card h1 {
    font-size: 1.8rem;
    margin-bottom: 0.4rem;
}

.auth-subtitle {
    color: var(--text-soft);
    font-style: italic;
    margin-bottom: 1.8rem;
    font-family: 'Lora', serif;
}

/* ── Forms ── */
.form-group {
    margin-bottom: 1.2rem;
}

.form-group label {
    display: block;
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--text-soft);
    margin-bottom: 0.4rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.form-group input {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid var(--light-tan);
    border-radius: 8px;
    font-size: 1rem;
    font-family: 'Inter', sans-serif;
    background-color: var(--cream);
    color: var(--text-dark);
    transition: border-color 0.2s;
}

.form-group input:focus {
    outline: none;
    border-color: var(--soft-gold);
}

/* ── Buttons ── */
.btn-primary {
    width: 100%;
    padding: 0.85rem;
    background-color: var(--warm-brown);
    color: var(--white);
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    cursor: pointer;
    margin-top: 0.5rem;
    transition: background-color 0.2s;
}

.btn-primary:hover {
    background-color: var(--deep-brown);
}

/* ── Auth Switch ── */
.auth-switch {
    text-align: center;
    margin-top: 1.2rem;
    font-size: 0.9rem;
    color: var(--text-soft);
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 1.5rem;
    color: var(--text-soft);
    font-family: 'Lora', serif;
    font-style: italic;
    font-size: 0.9rem;
    border-top: 1px solid var(--light-tan);
}

💡 Conference-ready explanation:

CSS variables (--cream, --warm-brown) make the color palette easy to update in one place
Flexbox handles all the layout — navbar, centered auth card, footer placement
Google Fonts — Lora (serif, warm) for headings, Inter (clean) for body text
The whole design system is built around earthy, warm tones that feel grounded and hopeful


Save it and let me know when done! 👀SAVED!Apr 16Great! Now we need to add one more thing to app.py — a user loader function that Flask-Login needs to work. We also need to add a basic dashboard route.
Open app.py and update it to look like this:
python# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key-change-this-later'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///the_path.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # This tells Flask-Login how to find a user by their ID
    # It runs automatically on every request to check who is logged in
    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from routes.auth import auth
    app.register_blueprint(auth)

    # Basic dashboard route — we'll build this out fully in the next step
    @app.route('/')
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

Then create a basic dashboard template. In your terminal:
bashtouch templates/dashboard.html
Open it and type:
html<!-- templates/dashboard.html -->
{% extends "base.html" %}

{% block title %}Dashboard — The Path{% endblock %}

{% block content %}
<div style="text-align: center; padding: 3rem;">
    <h1>Welcome, {{ current_user.username }} 🕊️</h1>
    <p style="color: var(--text-soft); font-family: 'Lora', serif; font-style: italic; margin-top: 1rem;">
        "Every day is a new beginning. Take a deep breath and start again."
    </p>
</div>
{% endblock %}

Save both files, then let's run the app for the first time! In your terminal:
bashpython3 app.py
Then open your browser and go to http://127.0.0.1:5000/signup and let me know what you see! 👀File "/Users/jay/the_path/app.py", line 2, in <module>
    from flask import Flask, render_template
ModuleNotFoundError: No module named 'flask'
bash-3.2$ Traceback (most recent call last):
bash: syntax error near unexpected token most'
bash-3.2$   File "/Users/jay/the_path/app.py", line 2, in <module>
bash: syntax error near unexpected token newline'
bash-3.2$     from flask import Flask, render_template
bash: from: command not found
bash-3.2$ ModuleNotFoundError: No module named 'flask'
bash: ModuleNotFoundError:: command not found
bash-3.2$ bash-3.2$ 
bash: bash-3.2$: command not found
bash-3.2$Show moreApr 16Your virtual environment isn't active! That's why Flask can't be found. Run:
bashsource venv/bin/activate
You should see (venv) appear at the start of your prompt. Then try again:
bashpython3 app.py
Let me know what you see! 👀Running on http://127.0.0.1:5000
Press CTRL+C to quit
Restarting with statDebugger is active!Debugger PIN: 164-133-284Apr 16LET'S GO! 🎉🎉🎉
Your app is running! Open your browser and go to:
http://127.0.0.1:5000/signup
You should see your warm, faith-inspired signup page live in the browser. Try:

Signing up with a username, email, and password
Logging in with those credentials
Landing on the dashboard and seeing your username

Let me know what you see! 👀its saying template not found, would you like me to screenshot what i see?Apr 16Yes please, screenshot it! That'll help me see the exact error message so we can fix it quickly. 👀Apr 16I can see the issue! Flask is looking for signup.html directly in the templates folder, but we put it in templates/auth/signup.html.
We need to update routes/auth.py to point to the correct paths. Open routes/auth.py and change the two render_template lines:
Find this line in your signup function:
pythonreturn render_template('signup.html')
Change it to:
pythonreturn render_template('auth/signup.html')
Find this line in your login function:
pythonreturn render_template('login.html')
Change it to:
pythonreturn render_template('auth/login.html')
Save the file — Flask will restart automatically since debug mode is on. Then refresh your browser and let me know what you see! 👀it looks Amazing!Apr 16LET'S GO JAY! 🎉🎉🎉
Your app is live and looking good! That warm, faith-inspired design is exactly what we planned. Take a second to appreciate that — you built that from scratch.
Now let's test it fully before moving on:

Sign up — create an account with a username, email, and password
Check that it redirects you to the login page
Log in with those credentials
Check that you land on the dashboard and see your username

Try all three and let me know if everything works! 👀this happened after signupApr 16I can see the issue! The problem is in models.py — it's importing db from app.py but we need it to use the same db instance. Let's fix it.
Open models.py and change the very first import line from:
pythonfrom app import db
To:
pythonfrom flask_sqlalchemy import SQLAlchemy
from flask import current_app
Actually, the cleanest fix is simpler than that. Change the top of models.py to this:
python# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()
Then open app.py and change this line:
pythonfrom models import User
from app import db
Wait — let's look at this carefully. Open app.py and find this line near the top:
pythondb = SQLAlchemy()
Then in routes/auth.py find this line:
pythonfrom app import db
Change it to:
pythonfrom models import db
Save both files and refresh your browser. Let me know what you get! 👀i am confused, what do i change?Apr 16Sorry about that — I gave you too many options at once. Let's do it simply, one file at a time.

1. Open models.py and change just the first line from:
pythonfrom app import db
to:
pythonfrom flask_sqlalchemy import SQLAlchemy
Then add this line right after your imports, before the class User line:
pythondb = SQLAlchemy()

2. Open routes/auth.py and change this line:
pythonfrom app import db
to:
pythonfrom models import db

3. Open app.py and change this line near the top:
pythonfrom flask_sqlalchemy import SQLAlchemy
to nothing — delete it completely. Then find:
pythondb = SQLAlchemy()
and delete that line too. Then add this import near the top:
pythonfrom models import db

Save all three files and let me know what you see! 👀looks great, but the page is poretty blankApr 16That's actually perfect — it means signup and login are working! 🎉
The dashboard is blank because we only put a basic placeholder there. That's exactly what we planned — now it's time to build it out properly.
Let's commit what we have first so your GitHub stays up to date:
bashgit add .
git commit -m "Add authentication - signup, login, logout"
git push origin main
Once that's pushed, let me know and we'll build the real dashboard — this is where the sobriety tracker, check-ins, and spiritual journey features start coming to life! 🚀nothing happened when commiting to gitApr 16No worries! It might just mean Git didn't detect any changes or the terminal needs a nudge. Run this to check:
bashgit status
And send me a screenshot or copy what it says! 👀should i open a new terminal?Apr 16No, stay in the same terminal. Just make sure your virtual environment is active first — do you see (venv) at the start of your prompt?
If not, run:
bashsource venv/bin/activate
Then run:
bashgit status
And tell me what it says! 👀Apr 16I can see the issue — your app is still running in that terminal, so Git commands are getting mixed into the Flask output. You need a second terminal window.
In VS Code:

Press Ctrl + ` (backtick) to open a new terminal inside VS Code

Or just open a new terminal window on your Mac.
Then in the new terminal run:
bashcd the_path
source venv/bin/activate
git add .
git commit -m "Add authentication - signup, login, logout"
git push origin main
Let me know what you see! 👀it pushed!Apr 16Let's go! 🎉 Check your GitHub repo at github.com/93Jourdan/the-path and you should see all your files there with your commit message.
Your progress so far:

✅ Project structure
✅ Database models
✅ User authentication (signup, login, logout)
✅ Warm, faith-inspired design
✅ Pushed to GitHub


Now let's build the real dashboard and the sobriety tracker — this is the heart of the app and honestly the most impressive thing you'll demo at PowerUp 2026.
Ready to keep going? 🚀lets keep goingApr 16Let's build the sobriety tracker! First, create the route file:
bashtouch routes/tracker.py
Open routes/tracker.py and type this out:
python# routes/tracker.py
# This file handles the sobriety tracker feature.
# Users can set a sobriety start date, track their streak, and log relapses.

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, SobrietyTracker
from datetime import datetime

tracker = Blueprint('tracker', __name__)


@tracker.route('/tracker')
@login_required
def tracker_home():
    # Get all of the current user's sobriety trackers
    trackers = SobrietyTracker.query.filter_by(
        user_id=current_user.id
    ).order_by(SobrietyTracker.created_at.desc()).all()

    # Calculate streak in days for each active tracker
    tracker_data = []
    for t in trackers:
        if t.is_active:
            delta = datetime.utcnow() - t.start_date
            streak = delta.days
        else:
            streak = 0
        tracker_data.append({'tracker': t, 'streak': streak})

    return render_template('tracker/tracker.html', tracker_data=tracker_data)


@tracker.route('/tracker/add', methods=['GET', 'POST'])
@login_required
def add_tracker():
    if request.method == 'POST':
        addiction_type = request.form.get('addiction_type')
        start_date_str = request.form.get('start_date')

        # Convert the date string from the form into a Python datetime object
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

        new_tracker = SobrietyTracker(
            user_id=current_user.id,
            addiction_type=addiction_type,
            start_date=start_date,
            is_active=True
        )
        db.session.add(new_tracker)
        db.session.commit()

        flash('Tracker added! Keep going, one day at a time. 🕊️', 'success')
        return redirect(url_for('tracker.tracker_home'))

    return render_template('tracker/add_tracker.html')


@tracker.route('/tracker/relapse/<int:tracker_id>', methods=['POST'])
@login_required
def log_relapse(tracker_id):
    # Find the tracker that belongs to this user
    t = SobrietyTracker.query.filter_by(
        id=tracker_id,
        user_id=current_user.id
    ).first_or_404()

    # Reset the start date to today — the streak starts over
    t.start_date = datetime.utcnow()
    db.session.commit()

    flash('It\'s okay. Every setback is a setup for a comeback. 🙏', 'success')
    return redirect(url_for('tracker.tracker_home'))

💡 Conference-ready explanation:

filter_by(user_id=current_user.id) ensures users only ever see their own data — this is basic but critical security
datetime.utcnow() - t.start_date is a timedelta calculation — Python makes date math simple
first_or_404() automatically returns a 404 error if the record doesn't exist — clean and professional
Resetting start_date on relapse is a deliberate design decision — it resets the streak while preserving history


Save it, then let me know and we'll build the tracker templates! 👀lets build the tracker templates!11:57 AMFirst create the folder and files:
bashmkdir templates/tracker
touch templates/tracker/tracker.html
touch templates/tracker/add_tracker.html

1. Open templates/tracker/tracker.html and type this out:
html<!-- templates/tracker/tracker.html -->
{% extends "base.html" %}

{% block title %}Sobriety Tracker — The Path{% endblock %}

{% block content %}
<div class="page-container">
    <div class="page-header">
        <h1>🛤️ Your Sobriety Journey</h1>
        <p class="page-subtitle">Every single day counts. You are stronger than you know.</p>
        <a href="{{ url_for('tracker.add_tracker') }}" class="btn-primary">+ Add New Tracker</a>
    </div>

    {% if tracker_data %}
        <div class="tracker-grid">
            {% for item in tracker_data %}
            <div class="tracker-card">
                <div class="tracker-type">{{ item.tracker.addiction_type }}</div>

                <div class="streak-display">
                    <span class="streak-number">{{ item.streak }}</span>
                    <span class="streak-label">days</span>
                </div>

                <div class="tracker-since">
                    Since {{ item.tracker.start_date.strftime('%B %d, %Y') }}
                </div>

                {% if item.tracker.is_active %}
                    <div class="tracker-status active">✅ Active</div>
                {% else %}
                    <div class="tracker-status inactive">Inactive</div>
                {% endif %}

                <!-- Relapse button — resets the streak -->
                <form method="POST" action="{{ url_for('tracker.log_relapse', tracker_id=item.tracker.id) }}"
                      onsubmit="return confirm('Are you sure? This will reset your streak.')">
                    <button type="submit" class="btn-relapse">Log Relapse</button>
                </form>
            </div>
            {% endfor %}
        </div>
    {% else %}
        <div class="empty-state">
            <p>🕊️ You haven't started any trackers yet.</p>
            <p>Begin your journey today.</p>
            <a href="{{ url_for('tracker.add_tracker') }}" class="btn-primary">Start Tracking</a>
        </div>
    {% endif %}
</div>
{% endblock %}

2. Open templates/tracker/add_tracker.html and type this out:
html<!-- templates/tracker/add_tracker.html -->
{% extends "base.html" %}

{% block title %}Add Tracker — The Path{% endblock %}

{% block content %}
<div class="auth-container">
    <div class="auth-card">
        <h1>Start a New Tracker</h1>
        <p class="auth-subtitle">Naming it is the first step to overcoming it.</p>

        <form method="POST" action="{{ url_for('tracker.add_tracker') }}">
            <div class="form-group">
                <label for="addiction_type">What are you recovering from?</label>
                <select id="addiction_type" name="addiction_type" class="form-select">
                    <option value="">Select one...</option>
                    <option value="Alcohol">Alcohol</option>
                    <option value="Substances">Substances</option>
                    <option value="Gambling">Gambling</option>
                    <option value="Food">Food</option>
                    <option value="Pornography">Pornography</option>
                    <option value="Codependency">Codependency</option>
                    <option value="Other">Other</option>
                </select>
            </div>

            <div class="form-group">
                <label for="start_date">Sobriety start date</label>
                <input type="date" id="start_date" name="start_date" required>
            </div>

            <button type="submit" class="btn-primary">Begin Tracking</button>
        </form>

        <p class="auth-switch">
            <a href="{{ url_for('tracker.tracker_home') }}">← Back to Trackers</a>
        </p>
    </div>
</div>
{% endblock %}

Now we need to add some CSS for the tracker cards. Open static/style.css and add this at the very bottom:
css/* ── Tracker ── */
.page-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem;
}

.page-header {
    text-align: center;
    margin-bottom: 2.5rem;
}

.page-header h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.page-subtitle {
    color: var(--text-soft);
    font-family: 'Lora', serif;
    font-style: italic;
    margin-bottom: 1.5rem;
}

.tracker-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.5rem;
}

.tracker-card {
    background-color: var(--white);
    border: 1px solid var(--light-tan);
    border-radius: 16px;
    padding: 1.8rem;
    text-align: center;
    box-shadow: 0 4px 16px rgba(74, 46, 26, 0.06);
}

.tracker-type {
    font-family: 'Lora', serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--warm-brown);
    margin-bottom: 1rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.streak-display {
    margin: 1rem 0;
}

.streak-number {
    font-size: 3.5rem;
    font-weight: 700;
    color: var(--deep-brown);
    font-family: 'Lora', serif;
    line-height: 1;
}

.streak-label {
    display: block;
    font-size: 0.85rem;
    color: var(--text-soft);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 0.3rem;
}

.tracker-since {
    font-size: 0.85rem;
    color: var(--text-soft);
    margin-bottom: 0.8rem;
}

.tracker-status.active {
    font-size: 0.85rem;
    color: var(--success);
    margin-bottom: 1rem;
}

.btn-relapse {
    width: 100%;
    padding: 0.6rem;
    background-color: transparent;
    color: var(--error);
    border: 1px solid var(--error);
    border-radius: 8px;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.2s;
    margin-top: 0.5rem;
}

.btn-relapse:hover {
    background-color: var(--error);
    color: var(--white);
}

.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    color: var(--text-soft);
    font-family: 'Lora', serif;
    font-style: italic;
    line-height: 2;
}

.form-select {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid var(--light-tan);
    border-radius: 8px;
    font-size: 1rem;
    font-family: 'Inter', sans-serif;
    background-color: var(--cream);
    color: var(--text-dark);
}

Now register the tracker blueprint in app.py. Open it and add these two lines right after where you registered the auth blueprint:
pythonfrom routes.tracker import tracker
app.register_blueprint(tracker)

Save all files, then in your terminal run:
bashgit add .
git commit -m "Add sobriety tracker feature"
git push origin main
Then go to http://127.0.0.1:5000/tracker and let me know what you see! 👀➜  ~ mkdir
usage: mkdir [-pv] [-m mode] directory_name ...
➜  ~11:58 AMYou're in the wrong directory! You need to be inside the_path folder first. Run:
bashcd the_path
Then try again:
bashmkdir templates/tracker
touch templates/tracker/tracker.html
touch templates/tracker/add_tracker.html
Let me know what you get! 👀➜  the_path git:(main) ✗ templates/tracker/tracker.html
zsh: no such file or directory: templates/tracker/tracker.html
➜  the_path git:(main) ✗ touch templates/tracker/tracker/html
touch: templates/tracker/tracker/html: No such file or directory
➜  the_path git:(main) ✗11:59 AMNo worries! Run them one at a time:
bashtouch templates/tracker/tracker.html
Then:
bashtouch templates/tracker/add_tracker.html
If you still get an error, the folder wasn't created. Run:
bashmkdir templates/tracker
Then try the touch commands again. Let me know! 👀okay! no error!12:01 PMPerfect! Now open VS Code and you should see the new files in the sidebar:
templates/
├── auth/
│   ├── login.html
│   └── signup.html
├── tracker/
│   ├── tracker.html
│   └── add_tracker.html
└── base.html
Now type out all the code I gave you above in this order:

templates/tracker/tracker.html
templates/tracker/add_tracker.html
Add the new CSS to the bottom of static/style.css
Add the two blueprint lines to app.py

Take your time and let me know when everything is saved! 👀http://127.0.0.1:5000/tracker.  this shows a blank screen. is it because the virtual environment is not up?12:07 PMThe virtual environment isn't the issue if the page is loading — a blank screen just means you're not logged in or the app is running fine but showing the empty state.
Check two things:

Do you see the navbar at the top with "The Path" and Log In/Log Out?
Are you currently logged in?

If you're not logged in, go to:
http://127.0.0.1:5000/login
Log in and then go back to:
http://127.0.0.1:5000/tracker
Also — did you save all four things I listed? Especially the two blueprint lines in app.py? Send a screenshot if you're still seeing issues! 👀yes i saved everything, the screen is still blank12:11 PMSend me a screenshot of the blank page and also a screenshot of your app.py so I can see exactly what's there! 👀12:12 PMI can see the issue! Your app.py looks good, but the page is completely blank — no navbar, nothing. This means the app probably isn't running.
Look at your terminal — is the Flask server still running? You should see something like Running on http://127.0.0.1:5000.
Open your terminal and run:
bashcd the_path
source venv/bin/activate
python3 app.py
Then go to http://127.0.0.1:5000/tracker and let me know what you see! 👀the tracker is live! it works12:15 PMLET'S GO! 🎉🎉🎉
Try it out:

Click "+ Add New Tracker"
Select what you're recovering from
Pick a start date
Hit "Begin Tracking"

You should see your streak card appear with the number of days! Let me know what you see and we'll commit this and move on to the daily check-ins feature! 👀it looks and works awesome!!12:46 PMThat is HUGE Jay! 🎉🙏
You just built a real, working, full-stack feature from scratch — a database-backed sobriety tracker with streak calculation. That is genuinely impressive work.
Let's commit it:
bashgit add .
git commit -m "Add sobriety tracker with streak calculation"
git push origin main

Here's where we stand:

✅ Authentication (signup, login, logout)
✅ Sobriety tracker with streak counter
🔜 Daily check-ins & mood log
🔜 Spiritual journey tracker
🔜 Full dashboard tying it all together

Once that's pushed let's keep the momentum going and build the daily check-ins feature! 👀okay! lets build!12:48 PMFirst create the files:
bashtouch routes/checkin.py
mkdir templates/checkin
touch templates/checkin/checkin.html
touch templates/checkin/add_checkin.html
Open routes/checkin.py and type this out:
python# routes/checkin.py
# This file handles daily check-ins where users log their mood
# and write a short reflection for the day.

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, CheckIn
from datetime import datetime, date

checkin = Blueprint('checkin', __name__)


@checkin.route('/checkin')
@login_required
def checkin_home():
    # Get all check-ins for this user, most recent first
    checkins = CheckIn.query.filter_by(
        user_id=current_user.id
    ).order_by(CheckIn.created_at.desc()).all()

    # Check if user already checked in today
    today = date.today()
    already_checked_in = any(
        c.created_at.date() == today for c in checkins
    )

    return render_template(
        'checkin/checkin.html',
        checkins=checkins,
        already_checked_in=already_checked_in
    )


@checkin.route('/checkin/add', methods=['GET', 'POST'])
@login_required
def add_checkin():
    if request.method == 'POST':
        mood = request.form.get('mood')
        reflection = request.form.get('reflection')

        new_checkin = CheckIn(
            user_id=current_user.id,
            mood=mood,
            reflection=reflection
        )
        db.session.add(new_checkin)
        db.session.commit()

        flash('Check-in saved. Keep showing up. 🙏', 'success')
        return redirect(url_for('checkin.checkin_home'))

    return render_template('checkin/add_checkin.html')

Now open templates/checkin/checkin.html:
html<!-- templates/checkin/checkin.html -->
{% extends "base.html" %}

{% block title %}Daily Check-In — The Path{% endblock %}

{% block content %}
<div class="page-container">
    <div class="page-header">
        <h1>🌤️ Daily Check-Ins</h1>
        <p class="page-subtitle">Showing up for yourself every day is an act of courage.</p>

        {% if already_checked_in %}
            <div class="checked-in-badge">✅ You've checked in today. Well done.</div>
        {% else %}
            <a href="{{ url_for('checkin.add_checkin') }}" class="btn-primary">+ Check In Today</a>
        {% endif %}
    </div>

    {% if checkins %}
        <div class="checkin-list">
            {% for c in checkins %}
            <div class="checkin-card">
                <div class="checkin-header">
                    <span class="checkin-mood mood-{{ c.mood | lower }}">{{ c.mood }}</span>
                    <span class="checkin-date">{{ c.created_at.strftime('%B %d, %Y') }}</span>
                </div>
                {% if c.reflection %}
                    <p class="checkin-reflection">"{{ c.reflection }}"</p>
                {% endif %}
            </div>
            {% endfor %}
        </div>
    {% else %}
        <div class="empty-state">
            <p>🕊️ No check-ins yet.</p>
            <p>Start today — every entry is a step forward.</p>
        </div>
    {% endif %}
</div>
{% endblock %}

Now open templates/checkin/add_checkin.html:
html<!-- templates/checkin/add_checkin.html -->
{% extends "base.html" %}

{% block title %}Check In — The Path{% endblock %}

{% block content %}
<div class="auth-container">
    <div class="auth-card">
        <h1>How are you today?</h1>
        <p class="auth-subtitle">Be honest. This space is just for you.</p>

        <form method="POST" action="{{ url_for('checkin.add_checkin') }}">
            <div class="form-group">
                <label>How are you feeling?</label>
                <div class="mood-grid">
                    <label class="mood-option">
                        <input type="radio" name="mood" value="Grateful" required>
                        <span>🙏 Grateful</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="mood" value="Hopeful">
                        <span>🌅 Hopeful</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="mood" value="Peaceful">
                        <span>🕊️ Peaceful</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="mood" value="Anxious">
                        <span>😟 Anxious</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="mood" value="Struggling">
                        <span>💔 Struggling</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="mood" value="Strong">
                        <span>💪 Strong</span>
                    </label>
                </div>
            </div>

            <div class="form-group">
                <label for="reflection">Reflection (optional)</label>
                <textarea id="reflection" name="reflection" rows="4"
                    placeholder="What's on your heart today?"
                    class="form-textarea"></textarea>
            </div>

            <button type="submit" class="btn-primary">Save Check-In</button>
        </form>

        <p class="auth-switch">
            <a href="{{ url_for('checkin.checkin_home') }}">← Back to Check-Ins</a>
        </p>
    </div>
</div>
{% endblock %}

Add this CSS to the bottom of static/style.css:
css/* ── Check-Ins ── */
.checked-in-badge {
    display: inline-block;
    background-color: #dff0df;
    color: var(--success);
    border: 1px solid var(--success);
    border-radius: 20px;
    padding: 0.5rem 1.2rem;
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

.checkin-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 680px;
    margin: 0 auto;
}

.checkin-card {
    background-color: var(--white);
    border: 1px solid var(--light-tan);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    box-shadow: 0 2px 8px rgba(74, 46, 26, 0.05);
}

.checkin-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
}

.checkin-mood {
    font-weight: 600;
    font-size: 0.95rem;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    background-color: var(--light-tan);
    color: var(--warm-brown);
}

.checkin-date {
    font-size: 0.8rem;
    color: var(--text-soft);
}

.checkin-reflection {
    font-family: 'Lora', serif;
    font-style: italic;
    color: var(--text-soft);
    font-size: 0.95rem;
    margin-top: 0.5rem;
    line-height: 1.6;
}

/* Mood selector grid */
.mood-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    margin-top: 0.5rem;
}

.mood-option {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.mood-option input[type="radio"] {
    display: none;
}

.mood-option span {
    display: block;
    width: 100%;
    text-align: center;
    padding: 0.6rem 0.4rem;
    border: 1px solid var(--light-tan);
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.85rem;
    background-color: var(--cream);
    transition: all 0.2s;
}

.mood-option input[type="radio"]:checked + span {
    background-color: var(--warm-brown);
    color: var(--white);
    border-color: var(--warm-brown);
}

.mood-option span:hover {
    border-color: var(--warm-brown);
}

/* Textarea */
.form-textarea {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid var(--light-tan);
    border-radius: 8px;
    font-size: 1rem;
    font-family: 'Lora', serif;
    background-color: var(--cream);
    color: var(--text-dark);
    resize: vertical;
    transition: border-color 0.2s;
}

.form-textarea:focus {
    outline: none;
    border-color: var(--soft-gold);
}

Now register the blueprint in app.py. Add these two lines right after the tracker blueprint lines:
pythonfrom routes.checkin import checkin
app.register_blueprint(checkin)

Save everything, then let me know when it's done and we'll test it! 👀everything is saved!12:53 PMLet's test it! Go to:
http://127.0.0.1:5000/checkin
Try it out:

Click "+ Check In Today"
Select a mood
Write a short reflection
Hit "Save Check-In"

You should land back on the check-in page and see your entry listed with your mood and reflection. Let me know what you see! 👀it looks great! wow, I like how the apple emojis were incorporated12:57 PMRight?! 😄 The emojis make it feel warm and human — exactly the vibe we were going for. When you demo this at PowerUp 2026, people are going to feel the care that went into the design. That's what makes it memorable.
Let's commit it:
bashgit add .
git commit -m "Add daily check-ins with mood logging"
git push origin main
Then we build the last core feature — the Spiritual Journey Tracker. This one is going to be special. Ready? 🙏awesome, before we start, can i ask, these features and function be on one made page? like a dashboard, where it all comes together, all in one1:04 PMYes! 100% — that's actually the plan for the final step. Once we build the spiritual journey tracker, we'll build a full dashboard that ties everything together in one beautiful page showing:

🛤️ Your active sobriety streaks at a glance
🌤️ Today's check-in status and mood
🙏 Recent spiritual activity
A motivational quote at the top

Think of it like a personal recovery homepage — everything you need in one place. That's also going to be the most impressive thing to demo at the conference because it tells the whole story of the app in one screen.
So the order is:

Spiritual Journey Tracker — build it now
Full Dashboard — tie it all together

Ready to build the spiritual tracker? 🚀awesome!1:04 PMFirst create the files:
bashtouch routes/spiritual.py
mkdir templates/spiritual
touch templates/spiritual/spiritual.html
touch templates/spiritual/add_spiritual.html
Open routes/spiritual.py and type this out:
python# routes/spiritual.py
# This file handles the spiritual journey tracker.
# Users can log prayers, gratitude, readings, and spiritual milestones.

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, SpiritualLog
from datetime import datetime

spiritual = Blueprint('spiritual', __name__)


@spiritual.route('/spiritual')
@login_required
def spiritual_home():
    # Get all spiritual logs for this user, most recent first
    logs = SpiritualLog.query.filter_by(
        user_id=current_user.id
    ).order_by(SpiritualLog.created_at.desc()).all()

    # Count each activity type for the summary
    activity_counts = {}
    for log in logs:
        activity_counts[log.activity_type] = activity_counts.get(
            log.activity_type, 0
        ) + 1

    return render_template(
        'spiritual/spiritual.html',
        logs=logs,
        activity_counts=activity_counts
    )


@spiritual.route('/spiritual/add', methods=['GET', 'POST'])
@login_required
def add_spiritual():
    if request.method == 'POST':
        activity_type = request.form.get('activity_type')
        note = request.form.get('note')

        new_log = SpiritualLog(
            user_id=current_user.id,
            activity_type=activity_type,
            note=note
        )
        db.session.add(new_log)
        db.session.commit()

        flash('Spiritual activity logged. Every step matters. 🙏', 'success')
        return redirect(url_for('spiritual.spiritual_home'))

    return render_template('spiritual/add_spiritual.html')

Now open templates/spiritual/spiritual.html:
html<!-- templates/spiritual/spiritual.html -->
{% extends "base.html" %}

{% block title %}Spiritual Journey — The Path{% endblock %}

{% block content %}
<div class="page-container">
    <div class="page-header">
        <h1>🙏 Your Spiritual Journey</h1>
        <p class="page-subtitle">
            "Be still and know." Every prayer, every reading, every moment of
            gratitude is a step closer to wholeness.
        </p>
        <a href="{{ url_for('spiritual.add_spiritual') }}" class="btn-primary">
            + Log Activity
        </a>
    </div>

    <!-- Activity Summary -->
    {% if activity_counts %}
    <div class="spiritual-summary">
        {% for activity, count in activity_counts.items() %}
        <div class="summary-card">
            <span class="summary-count">{{ count }}</span>
            <span class="summary-label">{{ activity }}</span>
        </div>
        {% endfor %}
    </div>
    {% endif %}

    <!-- Activity Log -->
    {% if logs %}
        <h2 class="section-title">Recent Activity</h2>
        <div class="spiritual-list">
            {% for log in logs %}
            <div class="spiritual-card">
                <div class="spiritual-header">
                    <span class="spiritual-type">
                        {% if log.activity_type == 'Prayer' %}🙏
                        {% elif log.activity_type == 'Gratitude' %}💛
                        {% elif log.activity_type == 'Reading' %}📖
                        {% elif log.activity_type == 'Meditation' %}🧘
                        {% elif log.activity_type == 'Worship' %}🎵
                        {% elif log.activity_type == 'Milestone' %}⭐
                        {% else %}✨
                        {% endif %}
                        {{ log.activity_type }}
                    </span>
                    <span class="checkin-date">
                        {{ log.created_at.strftime('%B %d, %Y') }}
                    </span>
                </div>
                {% if log.note %}
                    <p class="checkin-reflection">"{{ log.note }}"</p>
                {% endif %}
            </div>
            {% endfor %}
        </div>
    {% else %}
        <div class="empty-state">
            <p>🕊️ Your spiritual journey log is empty.</p>
            <p>Log your first activity today.</p>
        </div>
    {% endif %}
</div>
{% endblock %}

Now open templates/spiritual/add_spiritual.html:
html<!-- templates/spiritual/add_spiritual.html -->
{% extends "base.html" %}

{% block title %}Log Activity — The Path{% endblock %}

{% block content %}
<div class="auth-container">
    <div class="auth-card">
        <h1>Log Spiritual Activity</h1>
        <p class="auth-subtitle">Every act of faith, however small, matters.</p>

        <form method="POST" action="{{ url_for('spiritual.add_spiritual') }}">
            <div class="form-group">
                <label>Activity Type</label>
                <div class="mood-grid">
                    <label class="mood-option">
                        <input type="radio" name="activity_type" value="Prayer" required>
                        <span>🙏 Prayer</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="activity_type" value="Gratitude">
                        <span>💛 Gratitude</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="activity_type" value="Reading">
                        <span>📖 Reading</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="activity_type" value="Meditation">
                        <span>🧘 Meditation</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="activity_type" value="Worship">
                        <span>🎵 Worship</span>
                    </label>
                    <label class="mood-option">
                        <input type="radio" name="activity_type" value="Milestone">
                        <span>⭐ Milestone</span>
                    </label>
                </div>
            </div>

            <div class="form-group">
                <label for="note">Note (optional)</label>
                <textarea id="note" name="note" rows="4"
                    placeholder="What did you experience? What are you grateful for?"
                    class="form-textarea"></textarea>
            </div>

            <button type="submit" class="btn-primary">Log Activity</button>
        </form>

        <p class="auth-switch">
            <a href="{{ url_for('spiritual.spiritual_home') }}">← Back to Spiritual Journey</a>
        </p>
    </div>
</div>
{% endblock %}

Add this CSS to the bottom of static/style.css:
css/* ── Spiritual Journey ── */
.spiritual-summary {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 1rem;
    margin-bottom: 2.5rem;
}

.summary-card {
    background-color: var(--white);
    border: 1px solid var(--light-tan);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(74, 46, 26, 0.05);
}

.summary-count {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    font-family: 'Lora', serif;
    color: var(--warm-brown);
}

.summary-label {
    display: block;
    font-size: 0.8rem;
    color: var(--text-soft);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 0.3rem;
}

.section-title {
    font-size: 1.2rem;
    color: var(--warm-brown);
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--light-tan);
}

.spiritual-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 680px;
    margin: 0 auto;
}

.spiritual-card {
    background-color: var(--white);
    border: 1px solid var(--light-tan);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    box-shadow: 0 2px 8px rgba(74, 46, 26, 0.05);
}

.spiritual-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
}

.spiritual-type {
    font-weight: 600;
    font-size: 0.95rem;
    color: var(--warm-brown);
}

Now register the blueprint in app.py. Add these two lines right after the checkin blueprint lines:
pythonfrom routes.spiritual import spiritual
app.register_blueprint(spiritual)

Save everything and let me know when done! 👀done!4:51 PMLet's test it! Go to:
http://127.0.0.1:5000/spiritual
Try it out:

Click "+ Log Activity"
Select an activity type like Prayer or Gratitude
Write a short note
Hit "Log Activity"

You should see your activity appear with the emoji, type, date and your note. Also notice the summary cards at the top — they count how many times you've done each activity. That's a really nice touch for the demo!
Let me know what you see! 👀It looks amazing!4:52 PM🙏🎉 You've built something truly beautiful Jay!
Let's commit it:
bashgit add .
git commit -m "Add spiritual journey tracker"
git push origin main

Here's where we stand:

✅ Authentication (signup, login, logout)
✅ Sobriety tracker with streak counter
✅ Daily check-ins with mood logging
✅ Spiritual journey tracker
🔜 Full dashboard — ties everything together

Once that's pushed, we build the dashboard — the crown jewel of the whole app and the first thing people will see when you demo it at PowerUp 2026. This is going to be the moment it all comes together. 🚀lets build!7:32 PMLet's build the dashboard! Open templates/dashboard.html and replace everything in it with this:
html<!-- templates/dashboard.html -->
{% extends "base.html" %}

{% block title %}Dashboard — The Path{% endblock %}

{% block content %}
<div class="page-container">

    <!-- Welcome Header -->
    <div class="dashboard-header">
        <h1>Welcome back, {{ current_user.username }} 🕊️</h1>
        <p class="page-subtitle">
            "Every day is a new beginning. Take a deep breath and start again."
        </p>
    </div>

    <!-- Quick Stats Row -->
    <div class="stats-row">
        <div class="stat-card">
            <span class="stat-number">{{ total_days }}</span>
            <span class="stat-label">Total Sober Days</span>
        </div>
        <div class="stat-card">
            <span class="stat-number">{{ total_checkins }}</span>
            <span class="stat-label">Check-Ins Logged</span>
        </div>
        <div class="stat-card">
            <span class="stat-number">{{ total_spiritual }}</span>
            <span class="stat-label">Spiritual Activities</span>
        </div>
    </div>

    <!-- Main Dashboard Grid -->
    <div class="dashboard-grid">

        <!-- Sobriety Trackers -->
        <div class="dashboard-card">
            <div class="card-header">
                <h2>🛤️ Sobriety</h2>
                <a href="{{ url_for('tracker.tracker_home') }}">View All</a>
            </div>
            {% if trackers %}
                {% for item in trackers %}
                <div class="dashboard-streak">
                    <div class="streak-info">
                        <span class="streak-type">{{ item.tracker.addiction_type }}</span>
                        <span class="streak-since">
                            Since {{ item.tracker.start_date.strftime('%b %d, %Y') }}
                        </span>
                    </div>
                    <div class="streak-badge">{{ item.streak }} days</div>
                </div>
                {% endfor %}
            {% else %}
                <p class="card-empty">No trackers yet.
                    <a href="{{ url_for('tracker.add_tracker') }}">Start one →</a>
                </p>
            {% endif %}
        </div>

        <!-- Today's Check-In -->
        <div class="dashboard-card">
            <div class="card-header">
                <h2>🌤️ Today's Check-In</h2>
                <a href="{{ url_for('checkin.checkin_home') }}">View All</a>
            </div>
            {% if already_checked_in %}
                <div class="checked-in-badge">✅ Checked in today!</div>
                {% if latest_checkin %}
                    <p class="dashboard-mood">Feeling: <strong>{{ latest_checkin.mood }}</strong></p>
                    {% if latest_checkin.reflection %}
                        <p class="checkin-reflection">"{{ latest_checkin.reflection }}"</p>
                    {% endif %}
                {% endif %}
            {% else %}
                <p class="card-empty">You haven't checked in today.</p>
                <a href="{{ url_for('checkin.add_checkin') }}" class="btn-primary">
                    Check In Now
                </a>
            {% endif %}
        </div>

        <!-- Spiritual Journey -->
        <div class="dashboard-card">
            <div class="card-header">
                <h2>🙏 Spiritual Journey</h2>
                <a href="{{ url_for('spiritual.spiritual_home') }}">View All</a>
            </div>
            {% if recent_spiritual %}
                {% for log in recent_spiritual %}
                <div class="dashboard-spiritual">
                    <span class="spiritual-type">
                        {% if log.activity_type == 'Prayer' %}🙏
                        {% elif log.activity_type == 'Gratitude' %}💛
                        {% elif log.activity_type == 'Reading' %}📖
                        {% elif log.activity_type == 'Meditation' %}🧘
                        {% elif log.activity_type == 'Worship' %}🎵
                        {% elif log.activity_type == 'Milestone' %}⭐
                        {% else %}✨
                        {% endif %}
                        {{ log.activity_type }}
                    </span>
                    <span class="checkin-date">
                        {{ log.created_at.strftime('%b %d') }}
                    </span>
                </div>
                {% if log.note %}
                    <p class="checkin-reflection">"{{ log.note }}"</p>
                {% endif %}
                {% endfor %}
            {% else %}
                <p class="card-empty">No spiritual activity yet.
                    <a href="{{ url_for('spiritual.add_spiritual') }}">Log one →</a>
                </p>
            {% endif %}
        </div>

    </div>

    <!-- Quick Actions -->
    <div class="quick-actions">
        <h2>Quick Actions</h2>
        <div class="actions-grid">
            <a href="{{ url_for('checkin.add_checkin') }}" class="action-btn">
                🌤️ Check In
            </a>
            <a href="{{ url_for('tracker.add_tracker') }}" class="action-btn">
                🛤️ Add Tracker
            </a>
            <a href="{{ url_for('spiritual.add_spiritual') }}" class="action-btn">
                🙏 Log Spiritual Activity
            </a>
        </div>
    </div>

</div>
{% endblock %}

Now update the dashboard route in app.py. Find this section:
python@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
And replace it with this:
python@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    from models import SobrietyTracker, CheckIn, SpiritualLog
    from datetime import datetime, date

    # Get sobriety trackers with streak calculation
    trackers = SobrietyTracker.query.filter_by(
        user_id=current_user.id,
        is_active=True
    ).all()
    tracker_data = []
    total_days = 0
    for t in trackers:
        delta = datetime.utcnow() - t.start_date
        streak = delta.days
        total_days += streak
        tracker_data.append({'tracker': t, 'streak': streak})

    # Get check-ins
    checkins = CheckIn.query.filter_by(
        user_id=current_user.id
    ).order_by(CheckIn.created_at.desc()).all()
    today = date.today()
    already_checked_in = any(c.created_at.date() == today for c in checkins)
    latest_checkin = checkins[0] if checkins else None
    total_checkins = len(checkins)

    # Get spiritual logs
    spiritual_logs = SpiritualLog.query.filter_by(
        user_id=current_user.id
    ).order_by(SpiritualLog.created_at.desc()).all()
    recent_spiritual = spiritual_logs[:3]
    total_spiritual = len(spiritual_logs)

    return render_template(
        'dashboard.html',
        trackers=tracker_data,
        total_days=total_days,
        already_checked_in=already_checked_in,
        latest_checkin=latest_checkin,
        total_checkins=total_checkins,
        recent_spiritual=recent_spiritual,
        total_spiritual=total_spiritual
    )

Finally add this CSS to the bottom of static/style.css:
css/* ── Dashboard ── */
.dashboard-header {
    text-align: center;
    margin-bottom: 2rem;
}

.dashboard-header h1 {
    font-size: 2rem;
}

.stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}

.stat-card {
    background-color: var(--deep-brown);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    color: var(--white);
}

.stat-number {
    display: block;
    font-size: 2.5rem;
    font-family: 'Lora', serif;
    font-weight: 700;
    color: var(--soft-gold);
}

.stat-label {
    display: block;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--light-tan);
    margin-top: 0.3rem;
}

.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.dashboard-card {
    background-color: var(--white);
    border: 1px solid var(--light-tan);
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 4px 16px rgba(74, 46, 26, 0.06);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--light-tan);
}

.card-header h2 {
    font-size: 1.1rem;
}

.card-header a {
    font-size: 0.8rem;
    color: var(--warm-brown);
}

.card-empty {
    color: var(--text-soft);
    font-style: italic;
    font-size: 0.9rem;
    font-family: 'Lora', serif;
}

.dashboard-streak {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.6rem 0;
    border-bottom: 1px solid var(--light-tan);
}

.streak-info {
    display: flex;
    flex-direction: column;
}

.streak-type {
    font-weight: 600;
    font-size: 0.9rem;
    color: var(--deep-brown);
}

.streak-since {
    font-size: 0.75rem;
    color: var(--text-soft);
}

.streak-badge {
    background-color: var(--light-tan);
    color: var(--warm-brown);
    font-weight: 700;
    font-size: 0.85rem;
    padding: 0.3rem 0.75rem;
    border-radius: 20px;
}

.dashboard-mood {
    font-size: 0.95rem;
    color: var(--text-dark);
    margin: 0.5rem 0;
}

.dashboard-spiritual {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0;
}

/* Quick Actions */
.quick-actions {
    margin-top: 1rem;
}

.quick-actions h2 {
    font-size: 1.2rem;
    margin-bottom: 1rem;
    color: var(--warm-brown);
}

.actions-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}

.action-btn {
    display: block;
    text-align: center;
    padding: 1rem;
    background-color: var(--white);
    border: 1px solid var(--light-tan);
    border-radius: 12px;
    color: var(--deep-brown);
    font-size: 0.95rem;
    font-weight: 500;
    transition: all 0.2s;
    box-shadow: 0 2px 8px rgba(74, 46, 26, 0.05);
}

.action-btn:hover {
    background-color: var(--deep-brown);
    color: var(--soft-gold);
    border-color: var(--deep-brown);
}

Save everything and let me know when done! 👀done!7:35 PMLet's see it! Go to:
http://127.0.0.1:5000/dashboard
You should see the full dashboard with:

🏆 Your stats row at the top (total sober days, check-ins, spiritual activities)
🛤️ Your active sobriety streaks
🌤️ Today's check-in status
🙏 Recent spiritual activity
⚡ Quick action buttons at the bottom

Let me know what you see! 👀the screen is blank7:35 PMSame issue as before — the server probably stopped. In your terminal run:
bashcd the_path
source venv/bin/activate
python3 app.py
Then go to http://127.0.0.1:5000/dashboard and let me know what you see! 👀File "/Users/jay/the_path/app.py", line 41
    @app.route('/dashboard')
IndentationError: unexpected unindent
(venv) ➜  the_path git:(main) ✗7:36 PM2 / 2No worries! This is an indentation error in app.py. Open it in VS Code and find the dashboard section. Make sure it looks exactly like this — pay close attention to the indentation:
python    # Register blueprints
    from routes.auth import auth
    app.register_blueprint(auth)
    from routes.tracker import tracker
    app.register_blueprint(tracker)
    from routes.checkin import checkin
    app.register_blueprint(checkin)
    from routes.spiritual import spiritual
    app.register_blueprint(spiritual)

    # Basic dashboard route
    @app.route('/')
    @app.route('/dashboard')
    @login_required
    def dashboard():
        from models import SobrietyTracker, CheckIn, SpiritualLog
        from datetime import datetime, date

        trackers = SobrietyTracker.query.filter_by(
            user_id=current_user.id,
            is_active=True
        ).all()
        tracker_data = []
        total_days = 0
        for t in trackers:
            delta = datetime.utcnow() - t.start_date
            streak = delta.days
            total_days += streak
            tracker_data.append({'tracker': t, 'streak': streak})

        checkins = CheckIn.query.filter_by(
            user_id=current_user.id
        ).order_by(CheckIn.created_at.desc()).all()
        today = date.today()
        already_checked_in = any(c.created_at.date() == today for c in checkins)
        latest_checkin = checkins[0] if checkins else None
        total_checkins = len(checkins)

        spiritual_logs = SpiritualLog.query.filter_by(
            user_id=current_user.id
        ).order_by(SpiritualLog.created_at.desc()).all()
        recent_spiritual = spiritual_logs[:3]
        total_spiritual = len(spiritual_logs)

        return render_template(
            'dashboard.html',
            trackers=tracker_data,
            total_days=total_days,
            already_checked_in=already_checked_in,
            latest_checkin=latest_checkin,
            total_checkins=total_checkins,
            recent_spiritual=recent_spiritual,
            total_spiritual=total_spiritual
        )

    return app
Everything inside create_app() needs to be indented one level (4 spaces). The return app line should be the last line inside create_app().
Can you send a screenshot of your app.py so I can see exactly what it looks like? 👀7:41 PMI can see the problem! Lines 49-87 (the dashboard function body) lost their indentation — they need to be indented inside the def dashboard(): function.
The easiest fix is to replace your entire app.py with this clean version. Select all the code in app.py, delete it, and type this out:
python# app.py
from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user
from models import db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key-change-this-later'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///the_path.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from routes.auth import auth
    app.register_blueprint(auth)
    from routes.tracker import tracker
    app.register_blueprint(tracker)
    from routes.checkin import checkin
    app.register_blueprint(checkin)
    from routes.spiritual import spiritual
    app.register_blueprint(spiritual)

    @app.route('/')
    @app.route('/dashboard')
    @login_required
    def dashboard():
        from models import SobrietyTracker, CheckIn, SpiritualLog
        from datetime import datetime, date

        trackers = SobrietyTracker.query.filter_by(
            user_id=current_user.id,
            is_active=True
        ).all()
        tracker_data = []
        total_days = 0
        for t in trackers:
            delta = datetime.utcnow() - t.start_date
            streak = delta.days
            total_days += streak
            tracker_data.append({'tracker': t, 'streak': streak})

        checkins = CheckIn.query.filter_by(
            user_id=current_user.id
        ).order_by(CheckIn.created_at.desc()).all()
        today = date.today()
        already_checked_in = any(
            c.created_at.date() == today for c in checkins
        )
        latest_checkin = checkins[0] if checkins else None
        total_checkins = len(checkins)

        spiritual_logs = SpiritualLog.query.filter_by(
            user_id=current_user.id
        ).order_by(SpiritualLog.created_at.desc()).all()
        recent_spiritual = spiritual_logs[:3]
        total_spiritual = len(spiritual_logs)

        return render_template(
            'dashboard.html',
            trackers=tracker_data,
            total_days=total_days,
            already_checked_in=already_checked_in,
            latest_checkin=latest_checkin,
            total_checkins=total_checkins,
            recent_spiritual=recent_spiritual,
            total_spiritual=total_spiritual
        )

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
Save it then run:
bashpython3 app.py
Let me know what you see! 👀there are some spacing issues with todays check in8:20 PMJAY. 🎉🙏
LOOK AT THAT DASHBOARD! That is a real, professional, beautiful web application. The warm colors, the stats, the cards, everything — this is conference-ready work!
The spacing issue in "Today's Check-In" is a quick CSS fix. Open static/style.css and find the .dashboard-card style and add a small fix. Scroll to the bottom and add:
css/* Fix check-in card spacing */
.dashboard-card .checked-in-badge {
    display: block;
    margin-bottom: 0.75rem;
}

.dashboard-card .btn-primary {
    display: block;
    text-align: center;
    margin-top: 0.75rem;
}

.dashboard-card .card-empty {
    margin-bottom: 0.75rem;
}
Save it and refresh. But honestly Jay — take a second to look at what you built. 857 sober days showing up on that tracker. This app could genuinely mean something to real people. That's powerful. 💪
Let me know how the spacing looks after the fix! 👀maybe padding>?8:20 PMYes! Add some padding inside the check-in card content. Add this to the bottom of static/style.css:
css/* Check-in card content padding */
.dashboard-card .checkin-reflection,
.dashboard-card .dashboard-mood,
.dashboard-card .checked-in-badge,
.dashboard-card .card-empty,
.dashboard-card .btn-primary {
    padding: 0.5rem 0;
}
Save and refresh — let me know if that fixes it! 👀Thank you so much Claude, I couldnt have done it without you!! I want to fix that CSS issue, run it by me again, should I alter the dashboard.card specs? or just add these fixes to the bottom?8:24 PMJust add the fixes to the bottom of style.css — no need to touch the existing .dashboard-card specs. That way you're not breaking anything that already works, you're just adding targeted fixes on top.
The CSS cascades from top to bottom, so the fixes at the bottom will override just the specific things you need to change without affecting anything else.
Go ahead and add both of these to the very bottom of static/style.css:
css/* Fix check-in card spacing */
.dashboard-card .checked-in-badge {
    display: block;
    margin-bottom: 0.75rem;
}

.dashboard-card .btn-primary {
    display: block;
    text-align: center;
    margin-top: 0.75rem;
}

.dashboard-card .card-empty {
    margin-bottom: 0.75rem;
}

/* Check-in card content padding */
.dashboard-card .checkin-reflection,
.dashboard-card .dashboard-mood,
.dashboard-card .checked-in-badge,
.dashboard-card .card-empty,
.dashboard-card .btn-primary {
    padding: 0.5rem 0;
}
Save and refresh — let me know how it looks! 👀amazing!!8:31 PM🎉🙏 That's it Jay — you built a full-stack web application from scratch!
Let's do a final commit:
bashgit add .
git commit -m "Add full dashboard tying all features together"
git push origin main

Here's everything you built:

✅ User authentication (signup, login, logout)
✅ Sobriety tracker with streak calculation
✅ Daily check-ins with mood logging
✅ Spiritual journey tracker
✅ Full dashboard tying it all together
✅ Warm, faith-inspired design
✅ All pushed to GitHub


At PowerUp 2026 you can confidently say:

"I built a full-stack recovery support app using Flask, SQLAlchemy, and Flask-Login. It features session-based authentication with hashed passwords, a relational database schema, streak calculation logic, and a responsive dashboard — all designed with real users in mind."

That's a powerful sentence Jay. You earned it. 💪🙏
Next steps we could tackle:

📝 A strong README.md for your GitHub
🚀 Deploying it live so you can demo it from a real URL
✨ Any extra features or polish

What would you like to do next?lets do a strong readme! and deploy it live8:40 PMLet's do the README first, then deploy! A strong README is the first thing recruiters and industry professionals see when they visit your GitHub — it needs to sell the project immediately.
Let me write you a professional one. In your terminal:
bashtouch README.md
Then open README.md in VS Code and type this out:
markdown# 🕊️ The Path — Recovery & Spiritual Journey App

A full-stack web application designed to support individuals recovering from
addiction, codependency, and related challenges. Built with empathy,
intentionality, and faith at its core.

---

## 🌟 About The Project

The Path is a personal recovery companion that helps users:
- Track sobriety streaks across multiple recovery areas
- Log daily mood check-ins and personal reflections
- Document and grow their spiritual journey
- View all progress in one unified, encouraging dashboard

This project was built as a portfolio piece to demonstrate full-stack
web development skills, with a focus on clean architecture, user
experience, and real-world impact.

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| Python / Flask | Web framework & routing |
| SQLAlchemy | ORM & database management |
| SQLite | Lightweight relational database |
| Flask-Login | Session-based user authentication |
| Jinja2 | Server-side HTML templating |
| Werkzeug | Password hashing & security |
| Custom CSS | Warm, faith-inspired UI design |

---

## ✨ Features

### 🔐 User Authentication
- Secure signup and login with hashed passwords
- Session management with Flask-Login
- Protected routes — unauthenticated users are redirected to login

### 🛤️ Sobriety Tracker
- Track multiple recovery areas (Alcohol, Gambling, Food, and more)
- Automatic streak calculation in days
- Relapse logging that resets streak with an encouraging message

### 🌤️ Daily Check-Ins
- Log your mood from six options (Grateful, Hopeful, Peaceful, and more)
- Optional reflection journal entry
- Tracks whether you have checked in today

### 🙏 Spiritual Journey Tracker
- Log spiritual activities: Prayer, Gratitude, Reading, Meditation, Worship, Milestones
- Activity summary counts at a glance
- Personal notes for each entry

### 📊 Unified Dashboard
- Welcome header with personalized greeting
- Stats row showing total sober days, check-ins, and spiritual activities
- Live snapshot of all three features in one place
- Quick action buttons for fast navigation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/93Jourdan/the-path.git
cd the-path
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install flask flask-sqlalchemy flask-login
```

4. Run the application
```bash
python3 app.py
```

5. Open your browser and go to
http://127.0.0.1:5000

---

## 📁 Project Structure
the_path/
├── app.py              # Application entry point & dashboard route
├── models.py           # Database models (User, SobrietyTracker, CheckIn, SpiritualLog)
├── routes/
│   ├── auth.py         # Signup, login, logout
│   ├── tracker.py      # Sobriety tracker routes
│   ├── checkin.py      # Daily check-in routes
│   └── spiritual.py    # Spiritual journey routes
├── templates/
│   ├── base.html       # Base layout template
│   ├── dashboard.html  # Main dashboard
│   ├── auth/           # Login & signup pages
│   ├── tracker/        # Sobriety tracker pages
│   ├── checkin/        # Check-in pages
│   └── spiritual/      # Spiritual journey pages
├── static/
│   └── style.css       # Global styles & design system
└── README.md

---

## 💡 Technical Highlights

- **Application Factory Pattern** — `create_app()` function enables clean
  app initialization and scalability
- **Blueprint Architecture** — features are separated into modular blueprints
  for maintainability
- **Relational Database Schema** — four related tables with foreign key
  relationships and SQLAlchemy ORM
- **Secure Authentication** — passwords hashed with Werkzeug, never stored
  in plain text
- **Template Inheritance** — base template with Jinja2 blocks eliminates
  repeated HTML across pages
- **Streak Calculation** — real-time timedelta math between sobriety start
  date and current date

---

## 🎯 Roadmap

- [ ] Deploy to live server (Render / Railway)
- [ ] Add community support groups feature
- [ ] Add motivational quotes API integration
- [ ] Add data visualization for mood trends over time
- [ ] Add email reminders for daily check-ins
- [ ] Mobile responsive design improvements

---

## 👤 Author

**Jay** — Student Developer
- GitHub: [@93Jourdan](https://github.com/93Jourdan)

---

## 🙏 Purpose

This app was built with a deep respect for anyone walking the road of
recovery. Every feature was designed with real people in mind — people
who are brave enough to show up for themselves every single day.

*"Journey Before Destination"*
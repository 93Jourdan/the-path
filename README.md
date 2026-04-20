# 🕊️ The Path — Recovery & Spiritual Journey App

A full-stack web application designed to support individuals recovering from addiction, codependency, and related challenges. Built with empathy, intentionality, and faith at its core.

---

## 🌐 Live Demo

👉 **https://the-path.onrender.com/**

> Replace the URL above with your actual Render URL before saving!

---

## 🌟 About The Project

The Path is a personal recovery companion that helps users:
- Track sobriety streaks across multiple recovery areas
- Log daily mood check-ins and personal reflections
- Document and grow their spiritual journey
- View all progress in one unified, encouraging dashboard

This project was built as a portfolio piece to demonstrate full-stack web development skills, with a focus on clean architecture, user experience, and real-world impact.

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
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
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
```

---

## 💡 Technical Highlights

- **Application Factory Pattern** — `create_app()` function enables clean app initialization and scalability
- **Blueprint Architecture** — features are separated into modular blueprints for maintainability
- **Relational Database Schema** — four related tables with foreign key relationships and SQLAlchemy ORM
- **Secure Authentication** — passwords hashed with Werkzeug, never stored in plain text
- **Template Inheritance** — base template with Jinja2 blocks eliminates repeated HTML across pages
- **Streak Calculation** — real-time timedelta math between sobriety start date and current date

---

## 🎯 Roadmap

- [x] Deploy to live server (Render)
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

This app was built with a deep respect for anyone walking the road of recovery. Every feature was designed with real people in mind — people who are brave enough to show up for themselves every single day.

*"Journey Before Destination"*

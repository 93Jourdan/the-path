# 🕊️ The Path — Recovery & Spiritual Journey App

A full-stack web application designed to support individuals recovering from addiction, codependency, and related challenges. Built with empathy, intentionality, and faith at its core.

---

## 🌐 Live Demo

👉 **https://the-path.onrender.com/**

---

## 🌟 About The Project

The Path is a personal recovery companion that helps users:
- Track sobriety streaks across multiple recovery areas
- Log daily mood check-ins and personal reflections
- Document and grow their spiritual journey
- Connect with others through public profiles and a Wall of Encouragement
- View all progress in one unified, encouraging dashboard

This project was built as a portfolio piece to demonstrate full-stack web development skills, with a focus on clean architecture, user experience, and real-world impact.

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| Python / Flask | Web framework & routing |
| SQLAlchemy | ORM & database management |
| PostgreSQL | Production relational database (Render) |
| Flask-Login | Session-based user authentication |
| Jinja2 | Server-side HTML templating |
| Werkzeug | Password hashing & security |
| Cloudinary | Cloud-based profile image storage & transformation |
| Gunicorn | Production WSGI server |
| Custom CSS | Warm, faith-inspired UI design system |

---

## ✨ Features

### 🔐 User Authentication
- Secure signup and login with hashed passwords (Werkzeug PBKDF2)
- Session management with Flask-Login
- Protected routes — unauthenticated users are redirected to login
- Authorization logic separates who is logged in from what they're allowed to do

### 🛤️ Sobriety Tracker
- Track multiple recovery areas (Alcohol, Gambling, Food, and more)
- Automatic streak calculation in days using real-time timedelta math
- Relapse logging that resets streak with an encouraging message

### 🌤️ Daily Check-Ins
- Log your mood from six options (Grateful, Hopeful, Peaceful, and more)
- Optional reflection journal entry
- Tracks whether you have already checked in today

### 🙏 Spiritual Journey Tracker
- Log spiritual activities: Prayer, Gratitude, Reading, Meditation, Worship, Milestones
- Activity summary counts at a glance
- Personal notes for each entry

### 👤 Public User Profiles
- Public profile page at `/user/<username>` — viewable by anyone
- Avatar with Cloudinary image upload — persistent across deployments, face-detected and cropped server-side
- Sobriety streak displayed on profile
- Editable display name and bio

### 🕊️ Wall of Encouragement
- Any logged-in user can leave an encouraging message on another user's profile
- Messages stored using a self-referential foreign key pattern in SQLAlchemy (author → recipient, both referencing the User table)
- Newest messages displayed first

### 📊 Unified Dashboard
- Personalized greeting with link to user profile
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
pip install -r requirements.txt
```

4. Set environment variables
```bash
export SECRET_KEY=your-secret-key
export DATABASE_URL=your-database-url        # defaults to SQLite locally
export CLOUDINARY_CLOUD_NAME=your-cloud-name
export CLOUDINARY_API_KEY=your-api-key
export CLOUDINARY_API_SECRET=your-api-secret
```

5. Run the application
```bash
flask run
```

6. Open your browser and go to
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
the_path/
├── app.py                  # Application factory, blueprint registration, dashboard route
├── models.py               # Database models (User, SobrietyTracker, CheckIn, SpiritualLog, WallMessage)
├── routes/
│   ├── auth.py             # Signup, login, logout
│   ├── tracker.py          # Sobriety tracker routes
│   ├── checkin.py          # Daily check-in routes
│   ├── spiritual.py        # Spiritual journey routes
│   └── profile.py          # User profiles, Wall of Encouragement, avatar upload
├── templates/
│   ├── base.html           # Base layout template
│   ├── dashboard.html      # Main dashboard
│   ├── auth/               # Login & signup pages
│   ├── tracker/            # Sobriety tracker pages
│   ├── checkin/            # Check-in pages
│   ├── spiritual/          # Spiritual journey pages
│   └── profile/            # User profile & edit profile pages
├── static/
│   └── style.css           # Global styles & CSS variable design system
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn startup command for Render
└── README.md
```

---

## 💡 Technical Highlights

- **Application Factory Pattern** — `create_app()` enables clean app initialization, scalability, and testability
- **Blueprint Architecture** — features are separated into modular blueprints for maintainability, mirroring production Flask patterns
- **Self-Referential Foreign Keys** — `WallMessage` model references the `User` table twice (author and recipient), requiring explicit `foreign_keys=[...]` disambiguation in SQLAlchemy
- **Secure Authentication** — passwords hashed with Werkzeug PBKDF2, never stored in plain text
- **Cloud Media Storage** — profile images uploaded to Cloudinary with server-side face detection and cropping, persisting across deployments
- **Live Schema Migrations** — new columns added to a live PostgreSQL database using `ALTER TABLE ... ADD COLUMN IF NOT EXISTS` without data loss
- **Template Inheritance** — Jinja2 base template with blocks eliminates repeated HTML across pages
- **Production Deployment** — Gunicorn WSGI server with environment-variable-based secrets, zero sensitive data in codebase

---

## 🎯 Roadmap

- [x] User authentication (signup, login, logout)
- [x] Sobriety streak tracker
- [x] Daily mood check-ins with reflection journal
- [x] Spiritual journey tracker
- [x] Unified dashboard
- [x] Deploy to live server (Render + PostgreSQL)
- [x] Public user profiles with Cloudinary avatar upload
- [x] Wall of Encouragement between users
- [ ] Community support group feed
- [ ] Private messaging between users
- [ ] Motivational quotes API integration
- [ ] Data visualization for mood trends over time
- [ ] Email reminders for daily check-ins

---

## 👤 Author

**Jay** — Student Developer
- GitHub: [@93Jourdan](https://github.com/93Jourdan)

---

## 🙏 Purpose

This app was built with a deep respect for anyone walking the road of recovery. Every feature was designed with real people in mind — people who are brave enough to show up for themselves every single day.

*"Journey Before Destination"*

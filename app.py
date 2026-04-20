# app.py
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
# app.py
from flask import Flask, app, render_template
from flask_login import LoginManager, login_required, current_user
from models import db
from routes import spiritual

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
    
    from routes.tracker import tracker
    app.register_blueprint(tracker)
    
    from routes.checkin import checkin
    app.register_blueprint(checkin)

    from routes.spiritual import spiritual
    app.register_blueprint(spiritual)

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
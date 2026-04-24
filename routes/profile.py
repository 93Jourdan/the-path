# routes/profile.py
import cloudinary.uploader
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import db, User, WallMessage, SobrietyTracker
from datetime import datetime

profile = Blueprint('profile', __name__)

@profile.route('/user/<username>')
def view_profile(username):
    user = User.query.filter_by(username=username).first_or_404()

    tracker = SobrietyTracker.query.filter_by(
        user_id=user.id, is_active=True
    ).first()
    streak = None
    if tracker:
        streak = (datetime.utcnow() - tracker.start_date).days

    wall_messages = WallMessage.query.filter_by(
        recipient_id=user.id
    ).order_by(WallMessage.timestamp.desc()).all()

    return render_template('profile/profile.html',
        profile_user=user,
        streak=streak,
        wall_messages=wall_messages
    )

@profile.route('/user/<username>/encourage', methods=['POST'])
@login_required
def post_encouragement(username):
    user = User.query.filter_by(username=username).first_or_404()
    body = request.form.get('body', '').strip()

    if not body:
        flash('Message cannot be empty.', 'error')
        return redirect(url_for('profile.view_profile', username=username))
    if len(body) > 280:
        flash('Message too long (280 chars max).', 'error')
        return redirect(url_for('profile.view_profile', username=username))

    msg = WallMessage(
        body=body,
        author_id=current_user.id,
        recipient_id=user.id
    )
    db.session.add(msg)
    db.session.commit()
    flash('Encouragement posted!', 'success')
    return redirect(url_for('profile.view_profile', username=username))

@profile.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        display_name = request.form.get('display_name', '').strip()
        bio = request.form.get('bio', '').strip()

        current_user.display_name = display_name if display_name else None
        current_user.bio = bio if bio else None

        # Handle avatar upload
        avatar_file = request.files.get('avatar')
        if avatar_file and avatar_file.filename:
            result = cloudinary.uploader.upload(
                avatar_file,
                folder='the_path/avatars',
                public_id=f'user_{current_user.id}',
                overwrite=True,
                transformation=[
                    {'width': 200, 'height': 200, 'crop': 'fill', 'gravity': 'face'}
                ]
            )
            current_user.avatar_url = result['secure_url']

        db.session.commit()
        flash('Profile updated!', 'success')
        return redirect(url_for('profile.view_profile', username=current_user.username))

    return render_template('profile/edit_profile.html')
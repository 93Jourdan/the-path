# routes/tracker.py
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
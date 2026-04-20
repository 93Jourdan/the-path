# routes/spiritual.py
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
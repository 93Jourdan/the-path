# routes/checkin.py
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
from flask import render_template, redirect, url_for
from .auth import login_required
from .models import MaintenanceTask

@app.route('/dashboard')
@login_required
def dashboard():
    tasks = MaintenanceTask.query.all()
    return render_template('dashboard.html', tasks=tasks)

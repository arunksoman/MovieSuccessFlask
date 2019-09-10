# admin.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return render_template('index.html')

@admin.route('/Adminprofile')
@login_required
def Adminprofile():
    return render_template('AdminPanel.html', name=current_user.name)

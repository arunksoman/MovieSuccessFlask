# admin.py

from flask import Blueprint, render_template, session, request, url_for, redirect
from flask_login import login_required, current_user
from imdb import IMDb


ia = IMDb()
admin = Blueprint('admin', __name__)

@admin.route('/Admin')
def Admin():
    return render_template('AdminPanel.html', name=current_user.name)


@admin.route('/Adminprofile')
@login_required
def Adminprofile():
    return render_template('AdminPanel.html', name=current_user.name)


@admin.route('/AddMovie', methods=['GET','POST'])
@login_required
def AddMovie():
    if request.form.get('txtname'):
        search_for = request.form.get('txtname')
        movies = ia.search_movie(search_for)
        movieID = movies[0].movieID
        print(movieID)
        session['movieID'] = movieID
        session['movieName'] = search_for
        return redirect(url_for('admin.AddMore'))
    return render_template('AddDetails.html')
    # return render_template('Error.html')


@admin.route('/AddMore', methods=['GET','POST'])
@login_required
def AddMore():
    moviesession = session.get('movieID', None)
    movieName = session.get('movieName', None)
    print(movieName)
    print('Movie ID from Session %s'%(moviesession))
    return render_template('AddDetails.html', movieName=movieName)

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.Admin'))

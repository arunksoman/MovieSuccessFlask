# admin.py

from flask import Blueprint, render_template, session, request, url_for, redirect
from flask_login import login_required, current_user
from imdb import IMDb
from pandas import DataFrame


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
    if request.method == 'POST':
        search_for = request.form.get('txtname')
        movies = ia.search_movie(search_for)
        movieID = movies[0].movieID
        print(movieID)
        session['movieID'] = movieID
        session['movieName'] = search_for
        return redirect(url_for('admin.AddMore'))
        # return render_template('AddDetails.html')
    return render_template('AddMovie.html')
    #


@admin.route('/AddMore', methods=['GET','POST'])
@login_required
def AddMore():
    moviesession = session.get('movieID', None)
    movieName = session.get('movieName', None)
    #print(movieName)
    #print('Movie ID from Session %s'%(moviesession))
    movie = ia.get_movie(moviesession)

    gen=''
    for genre in movie['genres']:
        if gen == '':
            gen = gen + genre
        else:
            gen = gen + '|' + genre

    tdata = str(movie['color info'][0]) + ',' + str(movie['title']) + ',' + str(movie['year']) + ',' + str(
        movie['directors'][0]) + ',' + str(movie['runtimes'][0]) + ',' + gen + ',' + str(movie['cast'][0]) + ',' + str(
        movie['cast'][1]) + ',' + str(movie['cast'][2]) + ',' + str(movie['languages'][0]) + ',' + str(
        movie['countries'][0]) + ',' + str(movie['votes']) + ',' + str(movie['rating'])
    moviedata = list(tdata.split(","))

    color = request.form.get('color')
    title = request.form.get('title')
    year = request.form.get('year')
    director = request.form.get('director')
    runtime = request.form.get('runtime')
    genre = request.form.get('genre')
    actor1 = request.form.get('actor1')
    actor2 = request.form.get('actor2')
    actor3 = request.form.get('actor3')
    language = request.form.get('language')
    country = request.form.get('country')
    numvotes = request.form.get('numvotes')
    rating = request.form.get('rating')
    actor1fb = request.form.get('actor1fb')
    actor2fb = request.form.get('actor2fb')
    actor3fb = request.form.get('actor3fb')
    directorfb = request.form.get('directorfb')
    moviefb = request.form.get('moviefb')
    poster = request.form.get('poster')
    budget = request.form.get('budget')
    gross = request.form.get('gross')
    aspectratio = request.form.get('aspectratio')
    contentrating = request.form.get('contentrating')
    userreviews = request.form.get('userreviews')

    if title:
        savedata = {
            "color": [color],
            "movie_title": [title],
            "title_year": [year],
            "director_name": [director],
            "duration": [runtime],
            "genres": [genre],
            "actor_1_name": [actor1],
            "actor_2_name": [actor2],
            "actor_3_name": [actor3],
            "language": [language],
            "country": [country],
            "num_voted_users": [numvotes],
            "imdb_score": [rating],
            "actor_1_facebook_likes": [actor1fb],
            "actor_2_facebook_likes": [actor2fb],
            "actor_3_facebook_likes": [actor3fb],
            "director_facebook_likes": [directorfb],
            "movie_facebook_likes": [moviefb],
            "facenumber_in_poster": [poster],
            "budget": [budget],
            "gross": [gross],
            "aspect_ratio": [aspectratio],
            "content_rating": [contentrating],
            "num_user_for_reviews": [userreviews]
        }
        df = DataFrame(savedata, columns = ['color', 'movie_title', 'title_year', 'director_name', 'duration', 'genres', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'language', 'country', 'num_voted_users', 'imdb_score', 'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'movie_facebook_likes', 'facenumber_in_poster', 'budget', 'gross', 'aspect_ratio', 'content_rating', 'num_user_for_reviews'])

        export_csv = df.to_csv('dataframe.csv', mode='a', index=None, header=False)
        return redirect(url_for('admin.AddMovie'))
    return render_template('AddDetails.html', moviedata=moviedata)

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.Admin'))

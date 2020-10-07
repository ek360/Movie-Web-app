from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session
from movie.adapters.memory_repository import MemoryRepository
from movie.domain.movie import Movie
from movie.domain.actor import Actor
from movie.domain.genre import Genre
from movie.domain.director import Director
import movie.adapters.repository as repo
import movie.movies.services as services

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


# Configure Blueprint.
movies_blueprint = Blueprint(
    'movies_bp', __name__)


@movies_blueprint.route('/movies', methods=['GET'])
def movies():
    # Read query parameters.
    target_rank = request.args.get('rank')

    rank_one = services.get_first_movie(repo.repo_instance)
    rank_hundread = services.get_last_movie(repo.repo_instance)

    if target_rank is None:
        target_rank = rank_one['rank']
    else:
        target_rank = int(target_rank)
    movies, previous_rank, next_rank = services.get_movie_by_rank(target_rank,repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if previous_rank is not None:
        prev_movie_url = url_for('movies_bp.movies', rank=previous_rank)
        first_movie_url = url_for('movies_bp.movies', rank=1)

    if next_rank is not None:
        next_movie_url = url_for('movies_bp.movies', rank=next_rank)
        last_movie_url = url_for('movies_bp.movies', rank= 1000)




        # Generate the webpage to display the articles.
    return render_template(
        'news/articles.html',
        title='Movie Rankings',
        movies=movies[0],
        first_movie_url = first_movie_url,
        last_movie_url = last_movie_url,
        prev_movie_url = prev_movie_url,
        next_movie_url = next_movie_url
        )

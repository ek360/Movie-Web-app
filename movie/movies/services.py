from typing import List, Iterable

from movie.adapters.repository import AbstractRepository
from movie.domain.movie import Movie
from movie.domain.actor import Actor
from movie.domain.genre import Genre
from movie.domain.director import Director

def get_first_movie(repo):
    movie = repo.get_first_movie()
    return movie_to_dict(movie)

def get_last_movie(repo):
    movie = repo.get_last_movie()
    return movie_to_dict(movie)

def get_movie(movie_rank: int,repo: AbstractRepository):
    movie = repo.get_movie(movie_rank)

    return movie_to_dict(movie)

def get_movie_by_rank(rank,repo):

    movie = repo.get_movie_by_rank(rank)


    movies_ranked = []
    next_movie = previous_movie = None

    if len(movie) > 0:
        previous_movie = repo.get_rank_of_previous_movie(movie[0])
        next_movie = repo.get_rank_of_next_movie(movie[0])

        movies_ranked = movies_to_dict(movie)
    return movies_ranked, previous_movie, next_movie

def movie_to_dict(movie):
    movie_dict = {
        'rank': movie.rank,
        'title': movie.title,
        'year': movie.year,
        'description': movie.description,
        'director': movie.director,
        "runtime": movie.runtime_minutes,
        "rating": movie.rating,
        "metascore": movie.metascore}
    return movie_dict

def movies_to_dict(movies):
    return [movie_to_dict(movie) for movie in movies]
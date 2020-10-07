import abc

from movie.domain.movie import Movie
from movie.domain.actor import Actor
from movie.domain.genre import Genre
from movie.domain.director import Director

repo_instance = None

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self, actor) -> Actor:
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self, director) -> Director:
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self, genre) ->Genre:
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, id) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_rank(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_rank_of_previous_movie(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_rank_of_next_movie(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username):
        raise NotImplementedError
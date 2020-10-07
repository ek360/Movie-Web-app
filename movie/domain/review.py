from datetime import datetime

from movie.domain.movie import Movie

class Review:
    def __init__(self,movie,review_text,rating):
        self.__movie = movie
        self.__review_text = review_text
        if rating > 0 and rating < 11:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.today()
        
    @property
    def movie(self):
        return self.__movie
        
    @property
    def review_text(self):
        return self.__review_text
        
    @property
    def rating(self):
        return self.__rating
        
    @property
    def timestamp(self):
        return self.__timestamp
        
        
    def __repr__(self):
        return f"<Movie {self.__movie}, Timestamp {self.__timestamp}>"
        
    def __eq__(self, other):
        if self.__movie == other.__movie and self.__review_text == other.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp:
            return True
        else:
            return False

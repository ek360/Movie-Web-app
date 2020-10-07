from movie.domain.genre import Genre
from movie.domain.actor import Actor
from movie.domain.director import Director

class Movie:
    
    def __init__(self,rank,title: str,year: int,description,director,runtime_minutes,rating,metascore):
        self.__rank = rank
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        
        if year < 1900:
            self.__year = None
        else:
            self.__year = year
            
        self.__description: str = description
        self.__director: Director = director
        self.__actors: list[Actors] = []
        self.__genres: list[Genres] = []
        self.__runtime_minutes: int = runtime_minutes
        self.__rating: float = rating
        self.__metascore: str = metascore

    @property
    def metascore(self):
        return self.__metascore

    @property
    def rating(self):
        return self.__rating

    @property
    def rank(self):
        return self.__rank
        
    @property   
    def title(self):
        return self.__title
        
    @title.setter
    def title(self, title):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
            
    @property        
    def year(self):
        return self.__year
        
    @year.setter
    def year(self, year):
        if year < 1900:
            self.__year = None
        else:
            self.__year = year
            
    @property
    def description(self):
        return self.__description
        
    @description.setter
    def description(self, description):
        if description == "" or type(description) is not str:
            self.__description = None
        else:
            self.__description = description
            
    @property
    def director(self):
        return self.__director
        
    @director.setter
    def director(self,director):
        if type(director) == Director:
            self.__director = director
        else:
            self.__director = None
            
    @property
    def actors(self):
        return self.__actors
        
    @actors.setter
    def actors(self,actors):
        for act in actors:
            if type(act) == Actor:
                self.__actors.append(act)
                
    @property
    def genres(self):
        return self.__genres
    
    @genres.setter
    def genres(self,genres):
        for gen in genres:
            if type(gen) == Genre:
                self.__genres.append(gen)
                
    @property
    def runtime_minutes(self):
        return self.__runtime_minutes
        
    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if runtime_minutes > 0:
            self.__runtime_minutes = runtime_minutes
        else:
            raise ValueError("runtime should be a positive number")
    
    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year},{self.__rank}>"
    
    def __eq__(self,other):
        return self.__title == other.__title and self.__year == other.__year
        
    def __lt__(self,other):
        if self.__title < other.__title:
            return True
        elif self.__title > other.__title:
            return False
        else:
            if self.__year < other.__year:
                return True
            else:
                return False
    
    def __hash__(self):
        return hash((self.__title,self.__year))
        
    def add_actor(self,actor):
        if type(actor) == Actor:
            self.__actors.append(actor)
    
    def remove_actor(self,actor):
        if type(actor) == Actor:
            if actor in self.__actors:
                self.__actors.remove(actor)
                
    def add_genre(self,genre):
        if type(genre) == Genre:
            self.__genres.append(genre)
            
    def remove_genre(self,genre):
        if type(genre) == Genre:
            if genre in self.__genres:
                self.__genres.remove(genre)

class Movie:
    """Encapsulates information pertaining to a particular movie.

    Attributes:
        title: string representing the title of the movie.
        director: string representing the director of the movie. If more than one director is known to have worked on the movie, my favorite one is used.
        actors: list of strings, each representing the lead actors that appeared in the movie.
        genre: string representing the genre of the movie.
        poster_image_url: string representing a URL to the poster image for the movie.
        trailer_youtube_url: string representing a URL to the trailer for the movie on Youtube.
    """

    def __init__(self, title, director, actors, genre, poster_image_url, trailer_youtube_url):
        self.title = title
        self.director = director
        self.actors = actors
        self.genre = genre
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
from fresh_tomatoes import open_movies_page
from movie import Movie

"""This is the main script that creates the movie objects, appends each
   to a list, and begins the creation of the HTML page using that data.
"""

movie_monty_python = Movie('Monty Python and the Holy Grail', 'Terry Gilliam',
                               ['Graham Chapman', 'John Cleese', 'Eric Idle'],
                               'Adventure/Comedy',
                               'http://www.movie-poster-artwork-finder.com/wp-content/uploads/2012/06/monty-python-and-the-holy-grail-poster-artwork-terry-gilliam-eric-idle-graham-chapman.jpg',  # noqa
                               'https://www.youtube.com/watch?v=LG1PlkURjxE')

movie_uhf = Movie('UHF', 'Jay Levey',
                  ['Weird Al Yankovic', 'Victoria Jackson', 'Kevin McCarthy'],
                  'Comedy',
                  'https://bandbent.files.wordpress.com/2012/04/936full-uhf-poster.jpg',  # noqa
                  'https://www.youtube.com/watch?v=tIJ6utj-DcU')

movie_hot_fuzz = Movie('Hot Fuzz', 'Edgar Wright',
                       ['Simon Pegg', 'Nick Frost', 'Martin Freeman'],
                       'Action/Comedy',
                       'http://cdn.gowatchit.com/posters/original/movie_47312.jpg',  # noqa
                       'https://www.youtube.com/watch?v=ayTnvVpj9t4')

movie_pulp_fiction = Movie('Pulp Fiction', 'Quentin Tarantino',
                           ['John Travolta', 'Uma Thurman',
                            'Samuel L. Jackson'],
                           'Crime/Drama',
                           'http://www.joblo.com/posters/images/full/1994-pulp-fiction-poster1.jpg',  # noqa
                           'https://www.youtube.com/watch?v=s7EdQ4FqbhY')

movie_citizenfour = Movie('Citizenfour', 'Laura Poitras',
                          ['Edward Snowden', 'Glenn Greenwald',
                           'William Binney'],
                          'Documentary',
                          'http://www.joblo.com/posters/images/full/citizenfour-poster.jpg',  # noqa
                          'https://www.youtube.com/watch?v=rHaWhUjV96M')

movie_ameri_psycho = Movie('American Psycho', 'Mary Harron',
                           ['Christian Bale', 'Justin Theroux', 'Josh Lucas'],
                           'Drama',
                           'http://www.joblo.com/posters/images/full/poster-american-psycho1.jpg',  # noqa
                           'https://www.youtube.com/watch?v=2GIsExb5jJU')

movies = [movie_monty_python, movie_uhf, movie_hot_fuzz, movie_pulp_fiction,
          movie_citizenfour, movie_ameri_psycho]

if __name__ == "__main__":
    open_movies_page(movies)

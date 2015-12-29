from fresh_tomatoes import *
from movie import Movie

"""This is the main script that creates the movie objects, appends each to a list, and begins the creation of the HTML page using that data.
"""

movies = []
movies.append(Movie('Monty Python and the Holy Grail', 'Terry Gilliam', ['Graham Chapman', 'John Cleese', 'Eric Idle'], 'Adventure/Comedy', 'http://www.movie-poster-artwork-finder.com/wp-content/uploads/2012/06/monty-python-and-the-holy-grail-poster-artwork-terry-gilliam-eric-idle-graham-chapman.jpg', 'https://www.youtube.com/watch?v=LG1PlkURjxE'))
movies.append(Movie('UHF', 'Jay Levey', ['Weird Al Yankovic', 'Victoria Jackson', 'Kevin McCarthy'], 'Comedy', 'https://bandbent.files.wordpress.com/2012/04/936full-uhf-poster.jpg', 'https://www.youtube.com/watch?v=tIJ6utj-DcU'))
movies.append(Movie('Hot Fuzz', 'Edgar Wright', ['Simon Pegg', 'Nick Frost', 'Martin Freeman'], 'Action/Comedy', 'http://cdn.gowatchit.com/posters/original/movie_47312.jpg', 'https://www.youtube.com/watch?v=ayTnvVpj9t4'))
movies.append(Movie('Pulp Fiction', 'Quentin Tarantino', ['John Travolta', 'Uma Thurman', 'Samuel L. Jackson'], 'Crime/Drama', 'http://www.joblo.com/posters/images/full/1994-pulp-fiction-poster1.jpg', 'https://www.youtube.com/watch?v=s7EdQ4FqbhY'))
movies.append(Movie('Citizenfour', 'Laura Poitras', ['Edward Snowden', 'Glenn Greenwald', 'William Binney'], 'Documentary', 'http://www.joblo.com/posters/images/full/citizenfour-poster.jpg', 'https://www.youtube.com/watch?v=rHaWhUjV96M'))
movies.append(Movie('American Psycho', 'Mary Harron', ['Christian Bale', 'Justin Theroux', 'Josh Lucas'], 'Drama', 'http://www.joblo.com/posters/images/full/poster-american-psycho1.jpg', 'https://www.youtube.com/watch?v=2GIsExb5jJU'))

if __name__ == "__main__":
	open_movies_page(movies)
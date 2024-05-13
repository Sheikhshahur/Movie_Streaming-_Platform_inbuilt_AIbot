import imdb
import sqlite3

def connect_to_database():
    # Connect to your database
    conn = sqlite3.connect('your_database.db')
    return conn

def get_movie_titles_from_database():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM movies")  # Assuming you have a table named 'movies' with a 'title' column
    movie_titles = [row[0] for row in cursor.fetchall()]
    conn.close()
    return movie_titles

def get_movie_ratings(movie_titles):
    ia = imdb.IMDb()
    ratings = {}

    for title in movie_titles:
        # Search for the movie by title
        movies = ia.search_movie(title)

        if movies:
            movie_id = movies[0].movieID
            movie = ia.get_movie(movie_id)
            
            if 'rating' in movie:
                ratings[title] = movie['rating']
            else:
                ratings[title] = "Rating not available"
        else:
            ratings[title] = "Movie not found"

    return ratings

# Get movie titles from the database
movie_titles = get_movie_titles_from_database()

# Get ratings for the movies
movie_ratings = get_movie_ratings(movie_titles)

# Print the ratings
for title, rating in movie_ratings.items():
    print(f"{title}: {rating}")

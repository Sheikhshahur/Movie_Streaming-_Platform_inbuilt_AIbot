import mysql.connector

# Create a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Sheikh@786',
            database='movie_recommender'  # Adjusted database name
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

# Insert a movie recommendation into the database
def insert_recommendation(connection, movie_details):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO recommendation (title, genre, actors, director, description) VALUES ( %s, %s, %s, %s, %s)"
        values = (
            movie_details.get('Title', ''),
            movie_details.get('Genre', ''),
            ', '.join(movie_details.get('Actors', [])),
            movie_details.get('Director', ''),
            movie_details.get('Description', ''),
            movie_details.get('Rating', '')
        )
        cursor.execute(sql, values)
        connection.commit()
        print("Movie recommendation inserted successfully")
    except mysql.connector.Error as error:
        print("Error inserting movie recommendation:", error)

# Close the database connection
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection to MySQL database closed")

# Example usage
def process_dialogflow_response(dialogflow_response):
    # Extract movie details from the Dialogflow response
    movie_details = {}
    for key, value in dialogflow_response.items():
        if key.lower() in ['title', 'genre', 'actors', 'director', 'description', 'rating']:
            if isinstance(value, list):
                value = ', '.join(value)
            movie_details[key.lower()] = value

    # Insert the movie recommendation into the database
    connection = create_connection()
    if connection:
        insert_recommendation(connection, movie_details)
        close_connection(connection)

# Example usage
# Assume dialogflow_response contains the response from Dialogflow
# You need to integrate this code into your existing fulfillment logic
dialogflow_response = {
    'Title': 'Raiders of the Lost Ark',
    'Actors': ['Harrison Ford', 'Karen Allen', 'Paul Freeman'],
    'genre': 'Adventure',
    'Director': 'Steven Spielberg',
    'Description': 'Archaeologist Indiana Jones races against Nazi agents in a quest to find the legendary Ark of the Covenant.',
    'Rating': '⭐⭐⭐⭐⭐ (5/5 stars)'
}
process_dialogflow_response(dialogflow_response)

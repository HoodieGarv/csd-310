# Garvin Stewart
# CSD 310
# 5/4/2026

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title):
    # method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute(
        "SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' "
        "FROM film "
        "INNER JOIN genre ON film.genre_id=genre.genre_id "
        "INNER JOIN studio ON film.studio_id=studio.studio_id"
    )

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n  -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
            film[0], film[1], film[2], film[3]))


try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # -- 1. Display initial films --
    show_films(cursor, "DISPLAYING FILMS")

    # -- 2. Insert a new film --
    cursor.execute(
        "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) "
        "VALUES('The Martian', '2015', 144, 'Ridley Scott', 1, 2)"
    )
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # -- 3. Update Alien to Horror (genre_id=1) --
    cursor.execute("UPDATE film SET genre_id=1 WHERE film_name='Alien'")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # -- 4. Delete Gladiator --
    cursor.execute("DELETE FROM film WHERE film_name='Gladiator'")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid credentials.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found.")
    else:
        print(err)
finally:
    db.close()
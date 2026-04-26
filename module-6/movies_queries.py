# Garvin Stewart
# CSD 310
# 4/26/2026

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # -- Query 1: All Studio Records --
    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}\n")

    # -- Query 2: All Genre Records --
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}\nGenre Name: {genre[1]}\n")

    # -- Query 3: Films with runtime < 2 hours (120 min) --
    print("\n-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()
    for film in films:
        print(f"Film Name: {film[0]}\nRuntime: {film[1]}\n")

    # -- Query 4: Film names and directors, grouped by director --
    print("\n-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    directors = cursor.fetchall()
    for record in directors:
        print(f"Film Name: {record[0]}\nDirector: {record[1]}\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid credentials.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found.")
    else:
        print(err)
finally:
    db.close()
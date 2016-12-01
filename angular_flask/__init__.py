import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for

app = Flask(__name__)

app.config.from_object('angular_flask.settings')

app.url_map.strict_slashes = False

import angular_flask.core
import angular_flask.models
import angular_flask.controllers

@app.route("/")
def hello():
    a = "Hello"
    b = " World"
    print("Inside hello function")
    return a + b

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/movies")
def movieLoad():

    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("select * from Movie order by MovieName")
    cursor.execute(query)

    movies = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('movies.html', movies=movies)

@app.route("/genres")
def genreLoad():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("select MovieName,Genre FROM Movie INNER JOIN Genre ON Movie.MovieID=Genre.MovieID order by Genre;")
    cursor.execute(query)

    genres = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('genres.html', genres=genres)

@app.route("/rooms")
def roomLoad():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("SELECT * FROM Rooms")
    cursor.execute(query)

    rooms = cursor.fetchall()’

    cursor.close()
    cnx.close()

    return render_template('rooms.html', rooms=rooms)

@app.route("/showings")
def showingLoad():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("SELECT * FROM Showing ORDER BY ShowingDateTime")
    cursor.execute(query)

    showings = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('showings.html', showings=showings)


@app.route("/customers")
def customerLoad():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("SELECT * FROM Customer")
    cursor.execute(query)

    customers = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('customers.html', customers=customers)


@app.route("/attend")
def attendLoad():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("")
    cursor.execute(query)

    attends = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('attend.html', attends=attends)


@app.route("/addmovie", methods=['POST'])
def addMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Movie (MovieID, MovieName, YearReleased) "
        "VALUES (%s, %s, %s)"
    )

    data = (request.form['MovieID'], request.form['MovieName'], request.form['YearReleased'])
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('movieLoad'))

@app.route("/deletemovie", methods=['POST'])
def deleteMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = "DELETE FROM Movie WHERE MovieID = %s"
    

    data = (request.form['MovieID'],)
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('movieLoad'))


@app.route("/editmovie", methods=['GET','POST'])
def editMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    
    
    tts = request.form['MovieID']


    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('movieLoad'))



if (__name__) == "__main__":
    app.run(host="0.0.0.0", debug=True)

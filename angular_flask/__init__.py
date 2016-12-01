import os
import json
import angular_flask.core
import angular_flask.models
import angular_flask.controllers
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for

app = Flask(__name__)

app.config.from_object('angular_flask.settings')

app.url_map.strict_slashes = False



@app.route("/")
def hello():
    a = "Hello"
    b = " World"
    print("Inside hello function")
    return a + b

@app.route("/Greet")
def welcome():
    return render_template("Greet.html")

@app.route("/movie")
def movieList():

    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("select * from Movie order by MovieName")
    cursor.execute(query)

    movies = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('movie.html', movie=movie)

@app.route("/addMovies", methods=['POST'])
def addMovies():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Movie (idMovie, MovieName, MovieYear) "
        "VALUES (%s, %s, %s)"
    )

    data = (request.form['idMovie'], request.form['MovieName'], request.form['MovieYear'])
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('movieList'))


@app.route("/deletemovie", methods=['POST'])
def deleteMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = ("DELETE FROM Movie WHERE idMovie = %s")
    

    data = (request.form['idMovie'],)
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('movieList'))


@app.route("/editmovie", methods=['GET','POST'])
def editMovie():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    tts = request.form['idMovie']
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('movieList'))

@app.route("/genres")
def genreList():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("select MovieName,Genre FROM Movie INNER JOIN Genre ON Movie.idMovie=Genre.idMovie order by Genre;")
    cursor.execute(query)

    genres = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('genres.html', genres=genres)


@app.route("/addGenre", methods=['POST'])
def addGenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Genre (Genre, Movie_idMovie) "
        "VALUES (%s, %s)"
    )

    data = (request.form['Genre'], request.form['Movie_idMovie'])
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('genresList'))

@app.route("/deleteGenre", methods=['POST'])
def deleteGenre():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = ("DELETE FROM Genre WHERE Movie_idMovie = %s")
    

    data = (request.form['Movie_idMovie'],)
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('genresList'))

@app.route("/TheatreRoom")
def TheatreRoomList():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("SELECT * FROM TheatreRoom")
    cursor.execute(query)

    rooms = cursor.fetchall()’

    cursor.close()
    cnx.close()

    return render_template('TheatreRoom.html', TheatreRoom=TheatreRoom)

@app.route("/addTheatreRoom", methods=['POST'])
def addTheatreRoom():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO TheatreRoom (RoomNumber, Capacity) "
        "VALUES (%s, %s)"
    )

    data = (request.form['RoomNumber'], request.form['Capacity'])
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('TheatreRoomList'))

@app.route("/deleteTheatreRoom", methods=['POST'])
def deleteTheatreRoom():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = ("DELETE FROM TheatreRoom WHERE RoomNumber = %s")
    

    data = (request.form['RoomNumber'],)
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('TheatreRoomList'))

@app.route("/modifyTheatreRoom", methods=['GET','POST'])
def modifyTheatreRoom():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    tts = request.form['TheatreRoom']
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('TheatreRoomList'))


@app.route("/showings")
def showingList():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("SELECT * FROM Showing ORDER BY ShowingDateTime")
    cursor.execute(query)

    showings = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('showings.html', showings=showings)



@app.route("/addShowing", methods=['POST'])
def addShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Showing(idshowing, ShowingDateTime, Movie_idMovie, TheatreRoom_RoomNumber, TicketPrice) "
        "VALUES (%d, %s, %d, %d, %d)"
    )

    data = (request.form['idshowing'], request.form['ShowingDateTime'], request.form['Movie_idMovie'], request.form['TheatreRoom_RoomNumber'], request.form['TicketPrice'])
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('TheatreRoomList'))

@app.route("/deleteShowing", methods=['POST'])
def deleteShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = ("DELETE FROM Showing WHERE TicketPrice= %s")
    

    data = (request.form['RoomNumber'],)
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('ShowingList'))



@app.route("/modifyShowing", methods=['GET','POST'])
def modifyShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    tts = request.form['idShowing']
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('ShowingList'))

@app.route("/customers")
def customerList():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()

    query = ("SELECT * FROM Customer order by LastName ")
    cursor.execute(query)

    customers = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('customers.html', customers=customers)



@app.route("/addCustomer", methods=['POST'])
def addCustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Showing(idCustomer,FirstName, LastName, EmailAddress, Sex) "
        "VALUES (%d, %s, %s, %s, %s)"
    )

    data = (request.form['idCustomer'], request.form['FirstName'], request.form['LastName'], request.form['EmailAddress'], request.form['Sex'])
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('customerList'))


@app.route("/deletecustomer", methods=['POST'])
def deletecustomer():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    insert_stmt = ("DELETE FROM Showing WHERE LastName= %s")
    

    data = (request.form['LastName'],)
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('customerList'))



@app.route("/modifycustomer", methods=['GET','POST'])
def modifyShowing():
    cnx = mysql.connector.connect(user='root', database='MovieTheatre')
    cursor = cnx.cursor()
    tts = request.form['idCustomer']
    cursor.execute(insert_stmt,data)
    cnx.commit()
    cnx.close()
    return redirect(url_for('customerList'))


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






if (__name__) == "__main__":
    app.run(host="0.0.0.0", debug=True)

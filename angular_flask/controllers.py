import os
import json
import mysql.connector

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from angular_flask import app

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/profile')
@app.route('/search')
@app.route('/movies')
@app.route('/rate')
@app.route('/attend')
@app.route('/staff')

def basic_pages(**kwargs):
	return make_response(open('angular_flask/index.html').read())


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
							   'img/favicon.ico')

# SQL Queries handled below
# -----------------------------






# Gets customer firstname and lastname from MYSQL and sends it to Angularjs frontend
@app.route('/getCustomers', methods=['GET'])
def getCustomers():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select * from Customer order by LastName")
	cursor.execute(query)
	returnString = []
	for i in cursor:
		returnString.append(i)

	json_result = json.dumps(returnString)
	cursor.close()
	cnx.close()
	print(str(json_result))
	return str(json_result)


@app.route("/getMovies", methods=['GET'])
def getMovies():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select * from Movie order by MovieName")
	cursor.execute(query)
	movielist = []
	for movie in cursor:
		movielist.append(movie)

	json_movies = json.dumps(movielist)
	cursor.close()
	cnx.close()
	print(str(json_movies))
	return str(json_movies)


@app.route('/getShowings', methods=['GET'])
def getShowings():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select FirstName, LastName from Customer")
	cursor.execute(query)
	returnString = []
	for i in cursor:
		returnString.append(i)

	json_result = json.dumps(returnString)
	cursor.close()
	cnx.close()
	print(str(json_result))
	return str(json_result)
	
@app.route("/movie")
def movieList():

	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select * from Movie order by MovieName")
	cursor.execute(query)

	movies = cursor.fetchall()
	cursor.close()
	cnx.close()
	json_allMovies = json.dumps(movies)
	return json_allMovies


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



@app.route("/deletemovie", methods=['POST'])
def deleteMovie():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = ("DELETE FROM Movie WHERE idMovie = %s")
	

	data = (request.form['idMovie'],)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()



@app.route("/editmovie", methods=['GET','POST'])
def editMovie():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "update Movie set MovieName = %s, MovieYear = %s where idMovie = %s"

	data = (request.form['MovieName'], request.form['MovieYear'], request.form['idMovie'])
	cnx.commit()
	cnx.close()
	

@app.route("/genres")
def genreList():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select MovieName,Genre FROM Movie INNER JOIN Genre ON Movie.idMovie=Genre.Movie_idMovie order by Genre;")
	cursor.execute(query)

	genres = cursor.fetchall()
	cursor.close()
	cnx.close()
	json_result = json.dumps(genres)
	return json_result



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


@app.route("/deleteGenre", methods=['POST'])
def deleteGenre():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = ("DELETE FROM Genre WHERE Genre = %s and Movie_idMovie = %s")
	

	data = (request.form['Genre'], request.form['Movie_idMovie'],)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()


@app.route("/rooms")
def TheatreRoomList():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("SELECT * FROM TheatreRoom")
	cursor.execute(query)

	rooms = cursor.fetchall()
	json_result = json.dumps(rooms)
	cursor.close()
	cnx.close()
	return json_result


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


@app.route("/deleteTheatreRoom", methods=['POST'])
def deleteTheatreRoom():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = ("DELETE FROM TheatreRoom WHERE RoomNumber = %s")
	

	data = (request.form['RoomNumber'],)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()


@app.route("/modifyTheatreRoom", methods=['GET','POST'])
def modifyTheatreRoom():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "update Rooms set Capacity = %s where RoomNumber = %s"
	data = (request.form['Capacity'], request.form['RoomNumber'])
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()



@app.route("/showings")
def showingList():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("SELECT idShowing, Movie_idMovie, TheatreRoom_RoomNumber, TicketPrice, DATE_FORMAT(ShowingDateTime, '%Y-%m-%d %T.%f') FROM Showing ORDER BY ShowingDateTime")
	cursor.execute(query)

	showings = cursor.fetchall()
	json_result = json.dumps(showings)
	cursor.close()
	cnx.close()
	return json_result




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


@app.route("/deleteShowing", methods=['POST'])
def deleteShowing():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "delete from Showing where idshowing = %d and Movie_idMovie = %d and TheatreRoom_RoomNumber = %d"    

	data = (request.form['idshowing'], request.form['Movie_idMovie'], request.form['TheatreRoom_RoomNumber'])
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()




@app.route("/modifyShowing", methods=['GET','POST'])
def modifyShow():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "update Showing set ShowingDateTime = %s, TicketPrice = %s where (Movie_idMovie = %s and TheatreRoom_RoomNumber = %s and idshowing = %s)"
	data = (request.form['ShowingDateTime'], request.form['TicketPrice'], request.form['Movie_idMovie'], request.form['TheatreRoom_RoomNumber'], request.form['idshowing'])
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()


@app.route("/customers")
def customerList():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("SELECT * FROM Customer order by LastName ")
	cursor.execute(query)

	customers = cursor.fetchall()
	json_result = json.dumps(customers)
	cursor.close()
	cnx.close()
	return json_result



@app.route("/addCustomer", methods=['POST'])
def addCustomer():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = (
		"INSERT INTO Customer (idCustomer,FirstName, LastName, EmailAddress, Sex) "
		"VALUES (%d, %s, %s, %s, %s)"
	)

	data = (request.form['idCustomer'], request.form['FirstName'], request.form['LastName'], request.form['EmailAddress'], request.form['Sex'])
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()



@app.route("/deletecustomer", methods=['POST'])
def deletecustomer():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = ("DELETE FROM Customer WHERE idCustomer = %s")
	

	data = (request.form['idCustomer'],)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()




@app.route("/modifycustomer", methods=['GET','POST'])
def modifyShowing():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "update Customer set FirstName = %s, LastName = %s, Sex = %s, EmailAddress = %s where idCustomer = %s"
	data = (request.form['FirstName'], request.form['LastName'], request.form['Sex'], request.form['EmailAddress'], request.form['CustomerID'])
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()


@app.route("/attend")
def attendLoad():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("select * from Attend")
	query = ("select Customer.FirstName, Customer.LastName, Showing.idShowing, Showing.ShowingDateTime, Movie.idMovie, Movie.MovieName, Attend.Rating from Customer join Attend on Customer.idCustomer = Attend.Customer_idCustomer join Showing on Showing.idShowing = Attend.Showing_idShowing join Movie on Movie.idMovie = Showing.Movie_idMovie order by Attend.Rating")
	cursor.execute(query)

	attends = cursor.fetchall()
	cursor.close()
	cnx.close()


# 404 page
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

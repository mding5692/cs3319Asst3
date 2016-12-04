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
	#print(str(json_result))
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

	post = request.get_json()
	data = (str(post['idMovie']), post['MovieName'], str(post['MovieYear']),)
	print(insert_stmt,data)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data


@app.route("/deletemovie", methods=['POST'])
def deleteMovie():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = ("DELETE FROM Movie WHERE idMovie = %s")
	
	post = request.get_json()
	data = (str(post['idMovie']),)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data



@app.route("/editmovie", methods=['GET','POST'])
def editMovie():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "update Movie set MovieName = %s, MovieYear = %s where idMovie = %s"

	post = request.get_json()
	data = (post['MovieName'], str(post['MovieYear']), str(post['idMovie']))
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data

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

	post = request.get_json()
	data = (post['Genre'], str(post['Movie_idMovie']))
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data

@app.route("/deleteGenre", methods=['POST'])
def deleteGenre():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = ("DELETE FROM Genre WHERE Genre = %s and Movie_idMovie = %s")
	
	post = request.get_json()
	data = (post['Genre'], str(post['Movie_idMovie']),)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data


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

	post = request.get_json()
	data = (str(post['RoomNumber']), str(post['Capacity']))
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data


@app.route("/deleteTheatreRoom", methods=['POST'])
def deleteTheatreRoom():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = ("DELETE FROM TheatreRoom WHERE RoomNumber = %s")
	
	post = request.get_json()
	data = (str(post['RoomNumber']),)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data


@app.route("/modifyTheatreRoom", methods=['GET','POST'])
def modifyTheatreRoom():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "update Rooms set Capacity = %s where RoomNumber = %s"
	post = request.get_json()	
	data = (str(post['Capacity']), str(post['RoomNumber']))
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data

@app.route("/showings")
def showingList():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	query = ("SELECT idShowing, Movie_idMovie, TheatreRoom_RoomNumber, TicketPrice, DATE_FORMAT(ShowingDateTime, '%Y-%m-%s %T.%f') FROM Showing ORDER BY ShowingDateTime")
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
		"VALUES (%s, %s, %s, %s, %s)"
	)

	post = request.get_json()
	data = (str(post['idshowing']), str(post['ShowingDateTime']), str(post['Movie_idMovie']), str(post['TheatreRoom_RoomNumber']), str(post['TicketPrice']))
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data


@app.route("/deleteShowing", methods=['POST'])
def deleteShowing():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "delete from Showing where idshowing = %s and Movie_idMovie = %s and TheatreRoom_RoomNumber = %s"    

	post = request.get_json()
	data = (str(post['idshowing']), str(post['Movie_idMovie']), str(post['TheatreRoom_RoomNumber']))
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data

@app.route("/modifyShowing", methods=['GET','POST'])
def modifyShow():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "update Showing set ShowingDateTime = %s, TicketPrice = %s where (Movie_idMovie = %s and TheatreRoom_RoomNumber = %s and idshowing = %s)"
	data = (str(post['ShowingDateTime']), str(post['TicketPrice']), str(post['Movie_idMovie']), str(post['TheatreRoom_RoomNumber']), str(post['idshowing']))
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data

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
		"VALUES (%s, %s, %s, %s, %s)"
	)

	data = (str(post['idCustomer']), post['FirstName'], post['LastName'], post['EmailAddress'], post['Sex'])
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data

@app.route("/deletecustomer", methods=['POST'])
def deletecustomer():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = ("DELETE FROM Customer WHERE idCustomer = %s")
	

	data = (str(post['idCustomer']),)
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data

@app.route("/modifycustomer", methods=['GET','POST'])
def modifyShowing():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	insert_stmt = "update Customer set FirstName = %s, LastName = %s, Sex = %s, EmailAddress = %s where idCustomer = %s"
	data = (post['FirstName'], post['LastName'], post['Sex'], post['EmailAddress'], str(post['CustomerID']))
	cursor.execute(insert_stmt,data)
	cnx.commit()
	cnx.close()
	return data

@app.route("/attend")
def attendLoad():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()

	#query = ("select * from Attend")
	query = ("select Customer.FirstName, Customer.LastName, Showing.idShowing, Showing.ShowingDateTime, Movie.idMovie, Movie.MovieName, Attend.Rating from Customer join Attend on Customer.idCustomer = Attend.Customer_idCustomer join Showing on Showing.idShowing = Attend.Showing_idShowing join Movie on Movie.idMovie = Showing.Movie_idMovie order by Attend.Rating")
	cursor.execute(query)

	attends = cursor.fetchall()
	json_result = json.dumps(attends)
	print(json_result)
	cursor.close()
	cnx.close()
	return json_result

# 404 page
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

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


@app.route("/movies", methods=['GET'])
def movieList():
	cnx = mysql.connector.connect(user='root', database='MovieTheatre')
	cursor = cnx.cursor()
	
	query = ("select * from Movie order by MovieName")
	cursor.execute(query)

	returnString = []
	for i in cursor:
		returnString.append(i)

	json_result = json.dumps(returnString)
	cursor.close()
	cnx.close()
	print(str(json_result))
	return str(json_result)


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

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

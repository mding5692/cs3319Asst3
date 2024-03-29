'use strict';

/* Used methods */

function cleanData(dataArr,dataType) {

	var result = new Array();

	if (dataType === "customers") {
		for (var i = 0; i < dataArr.length; i++) {
			result.push(dataArr[i].join(" "));
		}
	}

	return result;
}

function formatDataAsSQLInput(data, dataType) {

	var result = new Array();

	if (dataType === "customers") {
		result = data.split(" ");
	}


	return result;
}


/* Controllers */

function StaffController() {

}

function IndexController($scope) {
	
}

function UserProfileController($scope) {
	
}

function MoviesController($scope) {

}

function BuyTicketCtrl($scope, $http) {

	$scope.customers = [];
	$scope.showings = [];
	$scope.customerName ="";
	$scope.showing ="";

	$http.get('/getCustomers').then(function(response) {
        //First function handles success
        $scope.customers = response.data;
    }, function(response) {
        //Second function handles error
        console.log(response);
        alert("Unable to grab customers from database");
    });



	$http.get('/showings').then(function(response) {
        //First function handles success
        $scope.showings = response.data;
    }, function(response) {
        //Second function handles error
        alert("Unable to grab showings from database");
    });

	$scope.buyTicket = function() {
		var continuePurchase = confirm("You sure you want to buy this?");
		if (continuePurchase) {

			var data = {
				custid : $scope.customerName[0],
				showing : $scope.showing[0]
			}

			$http.post('/attendShow', data).then(function(response) {
				console.log(response);
			}, function(response) {
				console.log(response);
			});

			showPurchaseSuccess();
		} else {
			
		}

	};

	function showPurchaseSuccess() {
		alert("Successfully bought ticket");
	}

	function showWarning() {
		alert("Not all information needed filled in");
	}
}

function SearchUsrCtrl($scope, $http) {
	$scope.searchedUsr = "";
	$scope.customers = [];

	$http.get('/getCustomers').then(function(response) {
        //First function handles success
        $scope.customers = response.data;
    }, function(response) {
        //Second function handles error
        alert("Unable to grab customers from database");
    });

}

function StaffFormCtrl($scope, $http) {
	// Adds Movie
	$scope.addMovieNo = 0;
	$scope.addMovieName = "";
	$scope.addMovieYr = 0;
	// Deletes movie
	$scope.delMovieNo = 0;
	// Modifies Movie
	$scope.modMovieNo = 0;
	$scope.modMovieName = "";
	$scope.modMovieYr = 0;
	// Lists All Movies
	$scope.allMovies = [];
	// Add genre for movie
	$scope.addMovieNoForGenre = 0;
	$scope.addMovieGenre = "";
	// Del genre from movie
	$scope.delMovieNoForGenre = 0;
	$scope.delMovieNameForGenre = "";
	$scope.delMovieGenre = "";
	// List genres
	$scope.allGenres = [];
	// Add room
	$scope.addRmNo = 0;
	$scope.addRmCap = 0;
	// Del room
	$scope.delRmNo = 0;
	// Edit room
	$scope.modRmNo = 0;
	$scope.modRmCap = 0;
	// List rooms
	$scope.allRms = [];
	// Add Showing
	$scope.addShowingNo = 0;
	$scope.addShowingMovieNo=0;
	$scope.addShowingDate = 0;
	$scope.addShowingRmNo = 0;
	$scope.addShowingPrice = 0;
	// Del Showing
	$scope.delShowingNo = 0;
	$scope.delShowingMovieNo=0;
	$scope.delShowingRmNo = 0;
	// Edit Showing
	$scope.modShowingNo = 0;
	$scope.modShowingMovieNo=0;
	$scope.modShowingRmNo = 0;
	// list showings
	$scope.allShowings = [];
	// Add cust
	$scope.addCustNo = 0;
	$scope.addCustSex = "";
	$scope.addCustFName = "";
	$scope.addCustLName = "";
	$scope.addCustEmail = "";
	// Del cust
	$scope.delCustNo = 0;
	// Edit cust
	$scope.modCustNo = 0;
	$scope.modCustSex = "";
	$scope.modCustFName = "";
	$scope.modCustLName = "";
	$scope.modCustEmail = "";
	// List cust
	$scope.allCustomers = [];
	// Attending 
	$scope.allAtt = [];

	// Gets Movie function
	$scope.getMovies = function() {
		$http.get('/movie').then(function(response) {
        //First function handles success
        	$scope.allMovies = response.data;
    	}, function(response) {
        //Second function handles error
        	console.log(response);
        	alert("Unable to grab movies from database");
    	});
	}

	$scope.addMovie = function() {
		var movieData = {
			idMovie : $scope.addMovieNo,
			MovieName : $scope.addMovieName,
			MovieYear : $scope.addMovieYr
		};

		var data = JSON.stringify(movieData)

		$http.post('/addMovies', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});
	}

	$scope.editMovie = function() {
		var movieData = {
			idMovie : $scope.modMovieNo,
			MovieName : $scope.modMovieName,
			MovieYear : $scope.modMovieYr
		};

		var data = JSON.stringify(movieData)

		$http.post('/editmovie', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});
	}

	$scope.delMovie = function() {
		var movieData = {
			idMovie: $scope.delMovieNo
		}

		var data = JSON.stringify(movieData)

		$http.post('/deletemovie', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});
	}

	// Gets all rooms
	$scope.getRms = function() {
		$http.get('/rooms').then(function(response) {
        //First function handles success
        	$scope.allRms = response.data;
    	}, function(response) {
        //Second function handles error
        	console.log(response);
        	alert("Unable to grab rooms from database");
    	});
	}

	$scope.addRm = function() {
		var rmData = {
			RoomNumber : $scope.addRmNo,
			Capacity : $scope.addRmCap
		};

		var data = JSON.stringify(rmData)

		$http.post('/addTheatreRoom', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});
	}

	$scope.delRm = function() {
		var rmData = {
			RoomNumber : $scope.delRmNo
		};

		var data = JSON.stringify(rmData)

		$http.post('/deleteTheatreRoom', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});
	}

	$scope.modRm = function() {
		var rmData = {
			RoomNumber : $scope.modRmNo,
			Capacity : $scope.modRmCap
		};

		var data = JSON.stringify(rmData)

		$http.post('/modifyTheatreRoom', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});
	}

	// Gets all shows
	$scope.getShowings = function() {
		$http.get('/showings').then(function(response) {
        //First function handles success
        	console.log(response.data)
        	$scope.allShowings = response.data;
    	}, function(response) {
        //Second function handles error
        	console.log(response);
        	alert("Unable to grab showings from database");
    	});
	}

	$scope.addGenre = function() {
		var genreData = {
			Movie_idMovie : $scope.addMovieNoForGenre,
			Genre : $scope.addMovieGenre
		};

		var data = JSON.stringify(genreData)

		$http.post('/addGenre', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});	
	}

	$scope.delGenre = function() {
		var genreData = {
			Movie_idMovie : $scope.delMovieNoForGenre,
			Genre : $scope.delMovieGenre
		};

		var data = JSON.stringify(genreData)

		$http.post('/deleteGenre', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});	
	}

	$scope.addShowing = function() {
		var showingData = {
			idshowing : $scope.addShowingNo,
			ShowingDateTime : $scope.addShowingDate,
			Movie_idMovie : $scope.addShowingMovieNo,
			TheatreRoom_RoomNumber : $scope.addShowingRmNo,
			TicketPrice : $scope.addShowingPrice
		};

		var data = JSON.stringify(showingData);

		$http.post('/addShowing', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});	
	}


	$scope.delShowing = function() {
		var showingData = {
			idshowing : $scope.delShowingNo,
			Movie_idMovie : $scope.delShowingMovieNo,
			TheatreRoom_RoomNumber : $scope.delShowingRmNo
		};

		var data = JSON.stringify(showingData);

		$http.post('/deleteShowing', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});	
	}

	$scope.modShowing = function() {
		var showingData = {
			idshowing : $scope.modShowingNo,
			ShowingDateTime : $scope.modShowingDate,
			Movie_idMovie : $scope.modShowingMovieNo,
			TheatreRoom_RoomNumber : $scope.modShowingRmNo,
			TicketPrice : $scope.modShowingPrice
		};

		var data = JSON.stringify(showingData);

		$http.post('/modifyShowing', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});			
	}

	$scope.addCust = function() {
		var custData = {
			idCustomer : $scope.addCustNo,
			FirstName : $scope.addCustFName,
			LastName : $scope.addCustLName,
			EmailAddress : $scope.addCustEmail,
			Sex : $scope.addCustSex
		};

		var data = JSON.stringify(custData);

		$http.post('/addCustomer', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});			
	}

	$scope.modCust = function() {
		var custData = {
			CustomerID : $scope.modCustNo,
			FirstName : $scope.modCustFName,
			LastName : $scope.modCustLName,
			EmailAddress : $scope.modCustEmail,
			Sex : $scope.modCustSex
		};

		var data = JSON.stringify(custData);

		$http.post('/modifycustomer', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});			
	}

	$scope.delCust = function() {
		var custData = {
			idCustomer : $scope.delCustNo
		};

		var data = JSON.stringify(custData);

		$http.post('/deletecustomer', data).then(function(data) {
			console.log(data);
			alert("Data is sent");
		}, function(data) {
			console.log(data)
		});			
	}

	$scope.getAttend = function() {
		$http.get('/attending').then(function(response) {
        //First function handles success
        	console.log(response.data)
        	$scope.allAtt = response.data;
    	}, function(response) {
        //Second function handles error
        	console.log(response);
        	alert("Unable to grab genres from database");
    	});	
	}

		// Gets all shows
	$scope.getCustList = function() {
		$http.get('/customers').then(function(response) {
        //First function handles success
        	console.log(response.data)
        	$scope.allCustomers = response.data;
    	}, function(response) {
        //Second function handles error
        	console.log(response);
        	alert("Unable to grab showings from database");
    	});
	}
			// Gets all shows
	$scope.getGenres = function() {
		$http.get('/genres').then(function(response) {
        //First function handles success
        	console.log(response.data)
        	$scope.allGenres = response.data;
    	}, function(response) {
        //Second function handles error
        	console.log(response);
        	alert("Unable to grab genres from database");
    	});
	}

}

function MoviesViewedCtrl($scope, $http) {
	$scope.searchedUser = "";
	$scope.customers = [];
	$scope.moviesWatched = [];
	$scope.allMovies = [];

	$http.get('/customers').then(function(response) {
        //First function handles success
        $scope.customers = response.data;
    }, function(response) {
        //Second function handles error
        console.log(response);
        alert("Unable to grab customers from database");
    });	

	$http.get('/attending').then(function(response) {
	    $scope.allMovies = response.data;
	}, function(response) {
	    	console.log("unable to find");
	});

	$scope.showCustMovies = function() {
		$scope.moviesWatched = [];
		var custID = $scope.searchedUser[0];

		for (var i = 0; i < $scope.allMovies.length; i++) {
			if ($scope.allMovies[i][0] == custID) {
				$scope.moviesWatched.push($scope.allMovies[i][6]);
				$scope.moviesWatched.push($scope.allMovies[i][7]);
			}
		}
	}
}

function RateMovieController($scope) {

}

function MovieRatingCtrl($scope, $http) {
	$scope.selectedCustomer = "";
	$scope.selectedShow = "";
	$scope.allShows = [];
	$scope.shows=[];
	$scope.customers = [];
	$scope.newRating = 0;

	$http.get('/getCustomers').then(function(response) {
        //First function handles success
        $scope.customers = response.data;
    }, function(response) {
        //Second function handles error
        console.log(response);
        alert("Unable to grab customers from database");
    });

	$http.get('/attending').then(function(response) {
        //First function handles success
        console.log(response);
    	$scope.allShows=response.data;

    }, function(response) {
        //Second function handles error
        console.log(response);
        alert("Unable to grab customers from database");
    });

    $scope.getCustShows = function() {
    	$scope.shows = [];
    	var custID = $scope.selectedCustomer[0];

		for (var i = 0; i < $scope.allShows.length; i++) {
			if ($scope.allShows[i][0] == custID) {
				$scope.shows.push($scope.allShows[i]);
			}
		}

    }

	$scope.rateShow = function() {
		if ($scope.newRating > 0 && $scope.newRating <= 5) {
    		var custID = $scope.selectedCustomer[0];
			var showArr = $scope.selectedShow.split(" ");
			var showing = showArr[3];

			var data = {
				rating: $scope.newRating,
				custid : custID,
				showing : showing
			};

			$http.post('/changeRating', data).then(function(response) {
				alert("new rating set");
			}, function(response) {
				console.log(response);
			});

		} else {
			alert("Rating has to be number from 1 to 5, try again!");
		}
	}


}


function SearchShowController($scope) {


}

function SearchFormController($scope, $http) {
	$scope.selectedGenre = "";
	$scope.selectedStartDate = "";
	$scope.selectedEndDate = "";
	$scope.emptySeats = false;
	$scope.movieName = "";
	$scope.allSelection = [];
	$scope.genres = [];
	$scope.uniqGenres = [];
	$scope.uniqDates = [];
	$scope.showings = [];
	var testUniqGenre = {};

	var selectionCriteria = {
		genre: $scope.selectedGenre,
		startDate: $scope.selectedStartDate,
		endDate: $scope.selectedEndDate,
		emptySeats: $scope.emptySeats,
		movieName: $scope.movieName
	}

	$scope.toggleEmptySeats = function() {
		$scope.emptySeats = !($scope.emptySeats);
	};

	$http.get('/genres').then(function(response) {
		console.log(response.data);
		$scope.genres = response.data;
	}, function(response) {
		console.log(response.data);
	});

	$http.get('/uniqGenres').then(function(response) {
		$scope.uniqGenres = response.data;
	}, function(resp) {
		console.log(resp);
	})

	$http.get('/uniqDates').then(function(response) {
		$scope.uniqDates = response.data;
	}, function(resp) {
		console.log(resp);
	})


	$http.get('/showings').then(function(response) {
		console.log(response.data);
		$scope.showings = response.data;
	}, function(response) {
		console.log(response.data);
	});

	$scope.checkDates = function() {
		if ($scope.selectedStartDate == "") {
			alert("Start Date can't be empty");
		}
		if ($scope.selectedStartDate > $scope.selectedEndDate) {
			alert("End date can't be before Start Date");
		}
	}

	$scope.search = function() {
		if ($scope.emptySeats = false) {
			alert("Some shows might not have available seats unless checkbox is checked!");
		}
	}
 }

function SqlInjectCtrl($scope, $http) {
	$scope.result = [];
	$scope.input = "";

	var data = {
		input: $scope.input
	}

	$scope.inject = function() {
		console.log($scope.input);
		$http.post('/showsqlinjection', data).then(function(resp) {
			$scope.results = resp.data;
		}, function(resp) {
			console.log(resp);
		});
	}
}

function AttendController($scope) {
	
}
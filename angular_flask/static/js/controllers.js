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
        $scope.customers = cleanData(response.data,"customers");
    }, function(response) {
        //Second function handles error
        console.log(response);
        alert("Unable to grab customers from database");
    });



	$http.get('/getShowings').then(function(response) {
        //First function handles success
        $scope.showings = response.data;
    }, function(response) {
        //Second function handles error
        alert("Unable to grab showings from database");
    });

	$scope.buyTicket = function() {
		// asks using the 
		confirmPurchase();

	};

	function confirmPurchase() {
		var continuePurchase = confirm("You sure you want to buy this?");
		if (continuePurchase) {
			showPurchaseSuccess();
		} 
	}


	function showPurchaseSuccess() {
		alert("Successfully bought ticket");
	}

	function showWarning() {
		alert("Not all information needed filled in");
	}
}

function SearchUsrCtrl($scope) {
	$scope.searchedCustomer = "";
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
	$scope.addMovieNameForGenre = "";
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
	$scope.delShowingDate = 0;
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

function MoviesViewedCtrl($scope) {
	$scope.searchedUser = "";
}

function RateMovieController($scope) {
}

function MovieRatingCtrl($scope, $http) {
	$scope.customerName = "";
	$scope.selectedMovie = "";
	$scope.movies=[];
	$scope.customers = [];

	$http.get('/getCustomers').then(function(response) {
        //First function handles success
        $scope.customers = cleanData(response.data,"customers");
    }, function(response) {
        //Second function handles error
        console.log(response);
        alert("Unable to grab customers from database");
    });

	$http.get('/getMovies').then(function(response) {
        //First function handles success
        console.log(response);
    	$scope.movies=response.data;

    }, function(response) {
        //Second function handles error
        console.log(response);
        alert("Unable to grab customers from database");
    });


}

function SearchShowController($scope) {


}

function SearchFormController($scope) {
	$scope.selectedGenre = "";
	$scope.selectedStartDate = "";
	$scope.selectedEndDate = "";
	$scope.emptySeats = false;
	$scope.movieName = "";

	$scope.toggleEmptySeats = function() {
		$scope.emptySeats = !($scope.emptySeats);
	};

	$scope.submitInfo = function() {
		showNotFilledWarning();
	};	

	function showNotFilledWarning() {
		alert("Please fill out some info to search with");
	}

 }

function AttendController($scope) {
	
}
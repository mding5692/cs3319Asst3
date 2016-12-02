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
	$scope.delMovieName = "";
	$scope.delMovieYr = 0;
	// Modifies Movie
	$scope.modMovieNo = 0;
	$scope.modMovieName = "";
	$scope.modMovieYr = 0;
	// Lists All Movies
	$scope.allMovies = [];

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
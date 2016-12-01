'use strict';

/* Controllers */

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
        console.log(response);
        $scope.customers = response.data;
    }, function(response) {
        //Second function handles error
        console.log(response);
        alert("Unable to grab customers from database");
    });

	/*$http.get('/getShowings').then(function(response) {
        //First function handles success
        $scope.showings = response.data;
    }, function(response) {
        //Second function handles error
        alert("Unable to grab customers from database");
    });*/

	$scope.buyTicket = function() {
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

function MoviesViewedCtrl($scope) {
	$scope.searchedUser = "";
}

function RateMovieController($scope, $routeParams, Post) {
	var postQuery = Post.get({ postId: $routeParams.postId }, function(post) {
		$scope.post = post;
	});
}

function MovieRatingCtrl($scope) {
	$scope.customerName = "";
	$scope.movie = "";


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
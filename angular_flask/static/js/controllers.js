'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function UserProfileController($scope) {
	
}

function MoviesController($scope) {

}

function BuyTicketCtrl($scope) {

	$scope.customerName ="";
	$scope.showing ="";

	/*$http({
		method: 'GET',
	})*/

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
	$scope.searchedUsr = "";



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
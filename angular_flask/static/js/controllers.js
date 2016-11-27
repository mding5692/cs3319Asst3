'use strict';

/* Controllers */

function IndexController($scope) {
	
}

function UserProfileController($scope) {
	
}

function MoviesController($scope) {

}

function RateMovieController($scope, $routeParams, Post) {
	var postQuery = Post.get({ postId: $routeParams.postId }, function(post) {
		$scope.post = post;
	});
}

function SearchShowController($scope) {

}

function AttendController($scope) {
	
}
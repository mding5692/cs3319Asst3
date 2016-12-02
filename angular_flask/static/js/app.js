'use strict';

angular.module('MovieFlask', ['angularFlaskServices'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/landing.html',
			controller: IndexController
		})
		.when('/profile', {
			templateUrl: 'static/partials/userProfile.html',
			controller: UserProfileController
		})
		.when('/moviesWatched', {
			templateUrl: 'static/partials/moviesWatched.html',
			controller: MoviesController
		})
		.when('/rate', {
			templateUrl: '/static/partials/rateMovies.html',
			controller: RateMovieController
		})
		/* Create a "/blog" route that takes the user to the same place as "/post" */
		.when('/search', {
			templateUrl: 'static/partials/searchShows.html',
			controller: SearchShowController
		}).when('/attend', {
			templateUrl: 'static/partials/attendShow.html',
			controller: AttendController
		}).when('/staff', {
			templateUrl: 'static/partials/staff.html',
			controller: StaffController
		})
		.otherwise({
			redirectTo: '/'
		});

		$locationProvider.html5Mode(true);
	}]);
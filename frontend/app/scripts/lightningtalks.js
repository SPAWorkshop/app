'use strict';

angular.module('lightningtalks', ['ngResource', 'ngRoute'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'partials/session-list.html',
        controller: 'SessionListCtrl'
      })
      .when('/session/:id', {
        templateUrl: 'partials/session-detail.html',
        controller: 'SessionDetailCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
;

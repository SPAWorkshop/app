'use strict';

angular.module('lightningtalks', ['ngResource', 'ngRoute'])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'partials/session-list.html',
        controller: 'SessionListCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
;

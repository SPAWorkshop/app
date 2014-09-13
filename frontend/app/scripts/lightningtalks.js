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
      .when('/talk/create', {
        templateUrl: 'partials/talk-create.html',
        controller: 'TalkCreateCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
;

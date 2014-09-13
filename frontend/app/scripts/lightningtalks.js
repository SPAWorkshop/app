'use strict';

angular.module('lightningtalks', ['ngResource', 'ngRoute', 'ngAnimate', 'flash'])
  .config(function ($routeProvider, $httpProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'partials/session-list.html',
        controller: 'SessionListCtrl'
      })
      .when('/session/:id', {
        templateUrl: 'partials/session-detail.html',
        controller: 'SessionDetailCtrl'
      })
      .when('/talks', {
        templateUrl: 'partials/talk-list.html',
        controller: 'TalkListCtrl'
      })
      .when('/talks/create', {
        templateUrl: 'partials/talk-create.html',
        controller: 'TalkCreateCtrl'
      })
      .when('/registration', {
        templateUrl: 'partials/registration.html',
        controller: 'RegistrationCtrl'
      })
      .when('/login', {
        templateUrl: 'partials/login.html',
        controller: 'LoginCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
    $httpProvider.interceptors.push([
      '$q', '$location', 'tokenStorage', function($q, $location, tokenStorage) {
        return {
          request: function(config) {
            if (config.url.indexOf('http://127.0.0.1:8000') === 0 && tokenStorage.has()) {
              config.headers['Authorization'] = "Token " + (tokenStorage.get());
            }
            return config || $q.when(config);
          },
          responseError: function(rejection) {
            if (rejection.status === 401) {
              tokenStorage.remove();
              $location.path('/');
            }
            return $q.reject(rejection);
          }
        };
      }
    ]);
  })
;

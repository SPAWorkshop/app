'use strict';

angular.module('lightningtalks', ['ngResource', 'ngRoute', 'ngAnimate', 'toasty', 'angular-ladda', 'settings'])
  .config(function ($routeProvider, $httpProvider) {

    /* TODO: TASK 1 - SESSION DETAILS
    *  - configure routing
    */

    $routeProvider
      .when('/', {
        templateUrl: 'partials/sessions/session-list.html',
        controller: 'SessionListCtrl'
      })
      .when('/talks', {
        templateUrl: 'partials/talks/talk-list.html',
        controller: 'TalkListCtrl'
      })
      .when('/talks/create', {
        templateUrl: 'partials/talks/talk-create.html',
        controller: 'TalkCreateCtrl'
      })
      .when('/talks/:id', {
        templateUrl: 'partials/talks/talk-update.html',
        controller: 'TalkUpdateCtrl'
      })
      .when('/registration', {
        templateUrl: 'partials/auth/registration.html',
        controller: 'RegistrationCtrl'
      })
      .when('/login', {
        templateUrl: 'partials/auth/login.html',
        controller: 'LoginCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
    $httpProvider.interceptors.push([
      '$q', '$location', 'tokenStorage', 'settings', function($q, $location, tokenStorage, settings) {
        return {
          request: function(config) {
            if (config.url.indexOf(settings.baseURL) === 0 && tokenStorage.has()) {
              config.headers.Authorization = 'Token ' + (tokenStorage.get());
            }
            return config || $q.when(config);
          },
          responseError:function(rejection) {
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

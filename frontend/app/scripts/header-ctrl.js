'use strict';

angular.module('lightningtalks')
  .controller('HeaderCtrl', function ($scope, $resource, $location, auth) {
    $scope.isUserLoggedIn = function () {
      return auth.isLoggedIn();
    };

    $scope.logout = function () {
      return auth.logout();
    };

  });
'use strict';

angular.module('lightningtalks')
  .controller('HeaderCtrl', function ($scope, $resource, $location, auth, flash, messages) {
    $scope.isUserLoggedIn = function () {
      return auth.isLoggedIn();
    };

    $scope.logout = function () {
      flash(messages.LOGOUT_SUCCESS);
      auth.logout();
    };

  });
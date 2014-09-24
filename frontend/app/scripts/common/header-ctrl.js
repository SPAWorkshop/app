'use strict';

angular.module('lightningtalks')
  .controller('HeaderCtrl', function ($scope, $location, auth, toasty, messages) {
    $scope.isUserLoggedIn = function () {
      return auth.isLoggedIn();
    };

    $scope.logout = function () {
      toasty.pop.success(messages.LOGOUT_SUCCESS);
      auth.logout();
    };
  });
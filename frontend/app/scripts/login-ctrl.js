'use strict';

angular.module('lightningtalks')
  .controller('LoginCtrl', function ($scope, $resource, $location, auth, flash, messages) {
    $scope.submit = function () {
      $resource('http://127.0.0.1:8000/api-auth/login').save($scope.user).$promise.then(function (response) {
        auth.login(response.token);
        flash(messages.LOGIN_SUCCESS);
        $location.path('/');
      });
    }
  });
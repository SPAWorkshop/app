'use strict';

angular.module('lightningtalks')
  .controller('RegistrationCtrl', function ($scope, $resource, $location, flash, messages) {
    $scope.submit = function () {
      $resource('http://127.0.0.1:8000/api-auth/register').save($scope.user).$promise.then(function () {
        flash(messages.REGISTRATION_SUCCESS);
        $location.path('/login');
      });
    }
  });
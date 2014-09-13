'use strict';

angular.module('lightningtalks')
  .controller('RegistrationCtrl', function ($scope, $resource, $location) {
    $scope.submit = function () {
      $resource('http://127.0.0.1:8000/api-auth/register').save($scope.user).$promise.then(function () {
        $location.path('/login');
      });
    }
  });
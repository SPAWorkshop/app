'use strict';

angular.module('lightningtalks')
  .controller('RegistrationCtrl', function ($scope, $resource, $location, toasty, messages) {
    $scope.submit = function () {
      $resource('http://127.0.0.1:8000/api-auth/register').save($scope.user).$promise.then(function () {
        toasty.pop.success(messages.REGISTRATION_SUCCESS);
        $location.path('/login');
      }, function (response) {
        $scope.errors = response.data;
      });
    }
  });
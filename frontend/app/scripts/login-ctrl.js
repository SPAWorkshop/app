'use strict';

angular.module('lightningtalks')
  .controller('LoginCtrl', function ($scope, $resource, $location, auth) {
    $scope.submit = function () {
      var response = $resource('http://127.0.0.1:8000/api-auth/login').save($scope.user).$promise.then(function () {
        auth.login(response.token);
        $location.path('/');
      });
    }
  });
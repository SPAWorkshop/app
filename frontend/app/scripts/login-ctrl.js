'use strict';

angular.module('lightningtalks')
  .controller('LoginCtrl', function ($scope, $resource, $location, auth, toasty, messages) {
    $scope.submit = function () {
      $scope.inProgress = true;
      $resource('http://127.0.0.1:8000/api-auth/login').save($scope.user).$promise.then(function (response) {
        auth.login(response.token);
        toasty.pop.success(messages.LOGIN_SUCCESS);
        $scope.inProgress = false;
        $location.path('/');
      }, function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      });
    }
  });
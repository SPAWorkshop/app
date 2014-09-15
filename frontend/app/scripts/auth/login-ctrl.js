'use strict';

angular.module('lightningtalks')
  .controller('LoginCtrl', function ($scope, $resource, $location, auth, toasty, messages, settings) {
    $scope.submit = function () {
      $scope.inProgress = true;
      $resource(settings.baseURL + '/auth/login').save($scope.user).$promise.then(function (response) {
        auth.login(response.token);
        toasty.pop.success(messages.LOGIN_SUCCESS);
        $scope.inProgress = false;
        $location.path('/');
      }, function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      });
    };
  });

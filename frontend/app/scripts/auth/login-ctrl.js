'use strict';

angular.module('lightningtalks')
  .controller('LoginCtrl', function ($scope, $resource, $location, auth, toasty, messages, settings) {
    $scope.submit = function () {
      $scope.inProgress = true;

      var user = $resource(settings.baseURL + '/auth/login').save($scope.user);

      var onSuccess = function (response) {
        auth.login(response.token);
        toasty.pop.success(messages.LOGIN_SUCCESS);
        $scope.inProgress = false;
        $location.path('/');
      };

      var onError = function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      };

      user.$promise.then(onSuccess, onError);
    };
  });

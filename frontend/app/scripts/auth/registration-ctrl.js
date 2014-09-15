'use strict';

angular.module('lightningtalks')
  .controller('RegistrationCtrl', function ($scope, $resource, $location, toasty, messages, settings) {
    $scope.submit = function () {
      $scope.inProgress = true;
      $resource(settings.baseURL + '/auth/register').save($scope.user).$promise.then(function () {
        toasty.pop.success(messages.REGISTRATION_SUCCESS);
        $scope.inProgress = false;
        $location.path('/login');
      }, function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      });
    };
  });

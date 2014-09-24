'use strict';

angular.module('lightningtalks')
  .controller('RegistrationCtrl', function ($scope, $resource, $location, toasty, messages, settings) {
    $scope.submit = function () {
      $scope.inProgress = true;

      var user = $resource(settings.baseURL + '/auth/register').save($scope.user);

      var onSuccess = function () {
        toasty.pop.success(messages.REGISTRATION_SUCCESS);
        $scope.inProgress = false;
        $location.path('/login');
      };

      var onError = function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      };

      user.$promise.then(onSuccess, onError);
    };
  });

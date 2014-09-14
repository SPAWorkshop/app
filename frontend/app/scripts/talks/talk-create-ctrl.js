'use strict';

angular.module('lightningtalks')
  .controller('TalkCreateCtrl', function ($scope, $resource, $location, auth, toasty, messages) {

    auth.shouldBeLoggedIn();

    $scope.sessions = $resource('http://127.0.0.1:8000/api/sessions').query();

    $scope.submit = function () {
      $scope.inProgress = true;
      $resource('http://127.0.0.1:8000/api/talks').save($scope.talk).$promise.then(function () {
        $scope.inProgress = false;
        toasty.pop.success(messages.TALK_CREATE_SUCCESS);
        $location.path('/talks');
      }, function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      });
    };
  });
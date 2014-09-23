'use strict';

angular.module('lightningtalks')
  .controller('TalkCreateCtrl', function ($scope, $resource, $location, auth, toasty, messages, Session, Talk) {
    auth.shouldBeLoggedIn();

    $scope.sessions = Session.query();

    $scope.submit = function () {
      $scope.inProgress = true;
      Talk.save($scope.talk).$promise.then(function () {
        $scope.inProgress = false;
        toasty.pop.success(messages.TALK_CREATE_SUCCESS);
        $location.path('/talks');
      }, function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      });
    };
  });

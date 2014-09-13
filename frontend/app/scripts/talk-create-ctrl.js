'use strict';

angular.module('lightningtalks')
  .controller('TalkCreateCtrl', function ($scope, $resource, $location, auth, flash, messages) {

    auth.shouldBeLoggedIn();

    $scope.sessions = $resource('http://127.0.0.1:8000/api/sessions').query();

    $scope.submit = function () {
      $resource('http://127.0.0.1:8000/api/talks').save($scope.talk).$promise.then(function () {
        flash(messages.TALK_CREATE_SUCCESS);
        $location.path('/session/' + $scope.talk.session);
      }, function (response) {
        $scope.errors = response.data;
      });
    }
  });
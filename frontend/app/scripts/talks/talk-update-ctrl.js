'use strict';

angular.module('lightningtalks')
  .controller('TalkUpdateCtrl', function ($scope, $location, $routeParams, auth, toasty, messages, settings, Talk) {
    auth.shouldBeLoggedIn();

    $scope.talk = Talk.get({id: $routeParams.id});

    $scope.submit = function () {
      $scope.inProgress = true;
      var talk = Talk.update({id: $routeParams.id}, {title: $scope.talk.title});

      var onSuccess = function () {
        $scope.inProgress = false;
        toasty.pop.success(messages.TALK_UPDATE_SUCCESS);
        $location.path('/talks');
      };

      var onError = function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      };

      talk.$promise.then(onSuccess, onError);
    };
  });
'use strict';

angular.module('lightningtalks')
  .controller('TalkListCtrl', function ($scope, $location, auth, toasty, messages, Talk) {
    auth.shouldBeLoggedIn();

    $scope.talks = Talk.query();

    $scope.delete = function (talk) {
      talk.deleteInProgress = true;

      var onSuccess = function () {
        toasty.pop.success(messages.TALK_DELETE_SUCCESS);
        $scope.talks = Talk.query();
      };

      Talk.delete({id: talk.id}).$promise.then(onSuccess);
    };
  });

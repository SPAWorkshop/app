'use strict';

angular.module('lightningtalks')
  .controller('TalkListCtrl', function ($scope, $resource, $location, auth, toasty, messages, Talk) {

    auth.shouldBeLoggedIn();

    var fetch = function () {
      $scope.talks = Talk.query();
    };

    fetch();

    $scope.delete = function (talk) {
      talk.deleteInProgress = true;
      Talk.delete({id: talk.id}).$promise.then(function () {
        toasty.pop.success(messages.TALK_DELETE_SUCCESS);
        fetch();
      });
    };
  });

'use strict';

angular.module('lightningtalks')
  .controller('TalkListCtrl', function ($scope, $resource, $location, auth, toasty, messages, settings) {

    auth.shouldBeLoggedIn();

    var fetch = function () {
      $scope.talks = $resource(settings.baseURL + '/talks').query();
    };

    fetch();

    $scope.delete = function (talk) {
      talk.deleteInProgress = true;
      $resource(settings.baseURL + '/talks/:id', {id: talk.id}).delete().$promise.then(function () {
        toasty.pop.success(messages.TALK_DELETE_SUCCESS);
        fetch();
      });
    };
  });
'use strict';

angular.module('lightningtalks')
  .controller('TalkListCtrl', function ($scope, $resource, $location, auth, flash, messages) {

    auth.shouldBeLoggedIn();

    var fetch = function () {
      $scope.talks = $resource('http://127.0.0.1:8000/api/talks').query();
    };

    fetch();

    $scope.delete = function (talk) {
      $resource('http://127.0.0.1:8000/api/talks/:id', {id: talk.id}).delete().$promise.then(function () {
        flash(messages.TALK_DELETE_SUCCESS);
        fetch();
      });
    };
  });
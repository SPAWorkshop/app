'use strict';

angular.module('lightningtalks')
  .controller('TalkUpdateCtrl', function ($scope, $resource, $location, $routeParams, auth, flash, messages) {

    auth.shouldBeLoggedIn();

    $scope.talk = $resource('http://127.0.0.1:8000/api/talks/:id', {id: $routeParams.id}).get();

    $scope.submit = function () {
      $resource('http://127.0.0.1:8000/api/talks/:id', {id: $routeParams.id}, {update: {method: 'PUT'}})
        .update({title: $scope.talk.title}).$promise.then(function () {
          flash(messages.TALK_UPDATE_SUCCESS);
          $location.path('/talks');
      }, function (response) {
        $scope.errors = response.data;
      });
    }
  });
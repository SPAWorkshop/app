'use strict';

angular.module('lightningtalks')
  .controller('TalkUpdateCtrl', function ($scope, $resource, $location, $routeParams, auth, toasty, messages, settings) {

    auth.shouldBeLoggedIn();

    $scope.talk = $resource(settings.baseURL + '/talks/:id', {id: $routeParams.id}).get();

    $scope.submit = function () {
      $scope.inProgress = true;
      $resource(settings.baseURL + '/talks/:id', {id: $routeParams.id}, {update: {method: 'PUT'}})
        .update({title: $scope.talk.title}).$promise.then(function () {
          $scope.inProgress = false;
          toasty.pop.success(messages.TALK_UPDATE_SUCCESS);
          $location.path('/talks');
      }, function (response) {
        $scope.inProgress = false;
        $scope.errors = response.data;
      });
    }
  });
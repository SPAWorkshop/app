'use strict';

angular.module('lightningtalks')
  .controller('TalkListCtrl', function ($scope, $resource, $location, auth) {

    auth.shouldBeLoggedIn();

    $scope.talks = $resource('http://127.0.0.1:8000/api/talks').query();
  });
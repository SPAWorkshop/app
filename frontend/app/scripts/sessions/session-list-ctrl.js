'use strict';

angular.module('lightningtalks')
  .controller('SessionListCtrl', function ($scope, $resource) {
    $scope.sessions = $resource('http://127.0.0.1:8000/api/sessions').query();
  });
'use strict';

angular.module('lightningtalks')
  .controller('SessionDetailCtrl', function ($scope, $resource, $routeParams) {
    $scope.session = $resource('http://127.0.0.1:8000/api/sessions/:id', {id: $routeParams.id}).get();
  });
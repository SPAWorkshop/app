'use strict';

angular.module('lightningtalks')
  .controller('SessionDetailCtrl', function ($scope, $resource, $routeParams, settings) {
    $scope.session = $resource(settings.baseURL + '/sessions/:id', {id: $routeParams.id}).get();
  });
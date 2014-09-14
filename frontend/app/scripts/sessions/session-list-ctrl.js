'use strict';

angular.module('lightningtalks')
  .controller('SessionListCtrl', function ($scope, $resource, settings) {
    $scope.sessions = $resource(settings.baseURL + '/sessions').query();
  });
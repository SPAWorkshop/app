'use strict';

angular.module('lightningtalks')
  .controller('SessionDetailCtrl', function ($scope, $routeParams, Session) {
    $scope.session = Session.get({id: $routeParams.id});
  });

'use strict';

angular.module('lightningtalks')
  .controller('SessionListCtrl', function ($scope, Session) {
    $scope.sessions = Session.query();
  });

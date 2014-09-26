'use strict';

angular.module('lightningtalks')
  .controller('TalkListCtrl', function ($scope, $location, auth, toasty, messages, Talk) {
    auth.shouldBeLoggedIn();

    $scope.talks = Talk.query();

    /* TODO: TASK 5 - DELETE TALK
    *  - implement delete function
    */
  });

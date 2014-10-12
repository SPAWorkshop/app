'use strict';

angular.module('lightningtalks')
  .service('Session', function ($resource, settings) {
    /* TODO: TASK 3 - LIMIT TALKS
    *  - check if session has already maximum number of talks
    */
    return $resource(settings.baseURL + '/sessions/:id');
  });

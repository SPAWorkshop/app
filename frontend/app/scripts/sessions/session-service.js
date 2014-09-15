'use strict';

angular.module('lightningtalks')
  .service('Session', function ($resource, settings) {
    return $resource(settings.baseURL + '/sessions/:id');
  });

'use strict';

angular.module('lightningtalks')
  .service('Talk', function ($resource, settings) {
    /* TODO: TASK IV - UPDATE TALK
    *  - add PUT method to talk resource
    */
    return $resource(settings.baseURL + '/talks/:id');
  });

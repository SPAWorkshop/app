'use strict';

angular.module('lightningtalks')
  .service('Talk', function ($resource, settings) {
    return $resource(settings.baseURL + '/talks/:id', null, {update: {method: 'PUT'}});
  });

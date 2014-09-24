'use strict';

angular.module('lightningtalks')
  .service('Session', function ($resource, settings) {
    var Service = $resource(settings.baseURL + '/sessions/:id');

    Service.prototype.maxTalksReached = function () {
      if (this.talks) {
        return (this.talks.length >= this.max_talks);
      }
      return false;
    };

    return Service;
  });

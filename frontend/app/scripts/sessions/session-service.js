'use strict';

angular.module('lightningtalks')
  .service('Session', function ($resource, settings) {
    var Service = $resource(settings.baseURL + '/sessions/:id');

    angular.extend(Service.prototype, {
        maxTalksReached: function() {
            return this.talks.length >= this.max_talks;
        }
    });

    return Service;
  });

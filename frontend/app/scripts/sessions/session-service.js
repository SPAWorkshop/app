'use strict';

angular.module('lightningtalks')
  .service('Session', function ($resource, settings) {
    var Session = $resource(settings.baseURL + '/sessions/:id');

    Session.prototype.maxTalksReached = function () {
      if (this.talks) {
        return (this.talks.length >= this.max_talks);
      } else if (this.talks_count) {
        return (this.talks_count >= this.max_talks);
      }
      return false;
    };

    return Session;
  });

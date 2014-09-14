'use strict';

angular.module('lightningtalks')
  .service('auth', function($window, tokenStorage, $resource, $location, toasty, messages) {
    this.user = null;

    this.fetch = function() {
    };

    this.login = function(token) {
      tokenStorage.set(token);
      this.fetch();
    };

    this.logout = function() {
      tokenStorage.remove();
      $location.path('/');
    };

    this.isLoggedIn = function() {
      tokenStorage.has();
    };

    this.shouldBeLoggedIn = function() {
      if (this.user == null) {
        if (tokenStorage.has()) {
          this.fetch();
        } else {
          toasty.pop.warning(messages.LOGIN_REQUIRED);
          $location.path('/login');
        }
      }
    };
});
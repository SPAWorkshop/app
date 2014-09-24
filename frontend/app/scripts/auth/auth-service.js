'use strict';

angular.module('lightningtalks')
  .service('auth', function($window, tokenStorage, $resource, $location, toasty, messages) {
    this.login = function(token) {
      tokenStorage.set(token);
    };

    this.logout = function() {
      tokenStorage.remove();
      $location.path('/');
    };

    this.isLoggedIn = function() {
      return tokenStorage.has();
    };

    this.shouldBeLoggedIn = function() {
      if (!this.isLoggedIn()) {
        toasty.pop.warning(messages.LOGIN_REQUIRED);
        $location.path('/login');
      }
    };
});
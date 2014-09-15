'use strict';
angular.module('lightningtalks')
  .service('tokenStorage', function($window) {
    this.TOKEN_KEY = 'auth_token';

    this.set = function(token) {
      return $window.localStorage.setItem(this.TOKEN_KEY, token);
    };

    this.remove = function() {
      return $window.localStorage.removeItem(this.TOKEN_KEY);
    };

    this.get = function() {
      return $window.localStorage.getItem(this.TOKEN_KEY);
    };

    this.has = function() {
      return ($window.localStorage !== null) && (this.get() !== null);
    };
});
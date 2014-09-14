'use strict';

angular.module('lightningtalks')
  .service('toasty', function() {
    var messages = [];

    var addMessage = function (msg) {
      messages.push(msg);
    };

    this.pop =  {
      success: addMessage,
      warning: addMessage
    };

    this.hasMessage = function (msg) {
      return messages.indexOf(msg) != -1;
    };
});
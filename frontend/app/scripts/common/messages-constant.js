'use strict';

angular.module('lightningtalks')
  .constant('messages', {
    REGISTRATION_SUCCESS: {
      title: 'Success!',
      msg: 'Registration complete - you could now sign in.'
    },
    TALK_CREATE_SUCCESS: {
      title: 'Success!',
      msg: 'Talk added successfully.'
    },
    TALK_DELETE_SUCCESS: {
      title: 'Success!',
      msg: 'Talk deleted successfully.'
    },
    TALK_UPDATE_SUCCESS: {
      title: 'Success!',
      msg: 'Talk updated successfully.'
    },
    LOGIN_SUCCESS: {
      title: 'Success!',
      msg: 'You are logged in.'
    },
    LOGOUT_SUCCESS: {
      title: 'Success!',
      msg: 'You are logged out.'
    },
    LOGIN_REQUIRED: {
      title: 'Warning!',
      msg: 'You need to be logged in.'
    }
  });
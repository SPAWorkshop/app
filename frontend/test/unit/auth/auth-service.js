'use strict';

describe('auth', function(){
  var auth;
  var $location;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function(_auth_, _$location_) {
    auth = _auth_;
    $location = _$location_;
  }));

  it('should redirect to login page', function() {
    $location.path('/talks/create');

    auth.shouldBeLoggedIn();

    expect($location.path()).toBe('/login');
  });

});
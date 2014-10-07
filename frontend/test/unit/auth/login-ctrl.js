'use strict';

describe('LoginCtrl', function(){
  var scope;
  var ctrl;
  var $httpBackend;
  var $location;
  var auth;
  var toasty;
  var messages;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function($rootScope, $controller, _$httpBackend_, _$location_, _auth_, _messages_, _toasty_) {
  	scope = $rootScope.$new();
    ctrl = $controller('LoginCtrl', {
      $scope: scope
  	});
    $httpBackend = _$httpBackend_;
    $location = _$location_;
    auth = _auth_;
    toasty = _toasty_;
    messages = _messages_;
  }));

  it('should submit user data and log in', function() {
    scope.user = {
      email: 'test@email.com',
      password: 'test-pass'
    };
    var token = 'test-token';
    $httpBackend.expectPOST('http://127.0.0.1:8000/api/auth/login', scope.user).respond(200, {auth_token: token});

    scope.submit();

    $httpBackend.flush();
    expect(auth.isLoggedIn()).toBe(true);
    expect(toasty.hasMessage(messages.LOGIN_SUCCESS)).toBe(true);
    expect($location.path()).toBe('/');
  });

  it('should submit user data and log in', function() {
    scope.user = {
      email: 'test@email.com',
      password: 'test-wrong-pass'
    };
    $httpBackend.expectPOST('http://127.0.0.1:8000/api/auth/login', scope.user).respond(400, {email: ['error']});

    scope.submit();

    $httpBackend.flush();
    expect(auth.isLoggedIn()).toBe(false);
    expect(scope.errors.email[0]).toBe('error');
  });

  afterEach(function () {
    auth.logout();
  });
});
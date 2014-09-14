'use strict';

describe('RegistrationCtrl', function(){
  var scope;
  var ctrl;
  var $httpBackend;
  var $location;
  var toasty;
  var messages;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function($rootScope, $controller, _$httpBackend_, _$location_, _toasty_, _messages_) {
  	scope = $rootScope.$new();
    ctrl = $controller('RegistrationCtrl', {
      $scope: scope
  	});
    $httpBackend = _$httpBackend_;
    $location = _$location_;
    toasty = _toasty_;
    messages = _messages_;
  }));

  it('should submit user data', function() {
    scope.user = {
      email: 'test@email.com',
      password: 'test-pass'
    };
    $httpBackend.expectPOST('http://127.0.0.1:8000/api/auth/register', scope.user).respond(201, '');

    scope.submit();

    $httpBackend.flush();
    expect(toasty.hasMessage(messages.REGISTRATION_SUCCESS)).toBe(true);
    expect($location.path()).toBe('/login');
  });

  it('should handle errors', function() {
    scope.user = {
      email: 'test@email.com',
      password: 'test-invalid-pass'
    };
    $httpBackend.expectPOST('http://127.0.0.1:8000/api/auth/register', scope.user).respond(400, {
      'email': ['error']
    });

    scope.submit();

    $httpBackend.flush();
    expect(scope.errors.email[0]).toBe('error');
  });
});
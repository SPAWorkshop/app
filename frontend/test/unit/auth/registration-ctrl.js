'use strict';

describe('RegistrationCtrl', function(){
  var scope;
  var ctrl;
  var $httpBackend;
  var $location;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function($rootScope, $controller, _$httpBackend_, _$location_) {
  	scope = $rootScope.$new();
    ctrl = $controller('RegistrationCtrl', {
      $scope: scope
  	});
    $httpBackend = _$httpBackend_;
    $location = _$location_;
  }));

  it('should submit user data', function() {
    $httpBackend.expectPOST('http://127.0.0.1:8000/api-auth/register').respond(201, '');

    scope.submit();

    $httpBackend.flush();
    expect($location.path()).toBe('/login');
  });
});
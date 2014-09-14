'use strict';

describe('SessionDetailCtrl', function(){
  var scope;
  var ctrl;
  var $httpBackend;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function($rootScope, $controller, _$httpBackend_) {
  	scope = $rootScope.$new();
    $httpBackend = _$httpBackend_;
    $httpBackend.expectGET('http://127.0.0.1:8000/api/sessions').respond(200, {id: 1});
    ctrl = $controller('SessionDetailCtrl', {
      $scope: scope
  	});
  }));

  it('should fetch session', function() {
    $httpBackend.flush();
    expect(scope.session.id).toBe(1);
  });

});
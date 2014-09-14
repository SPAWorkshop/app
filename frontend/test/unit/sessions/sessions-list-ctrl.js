'use strict';

describe('SessionListCtrl', function(){
  var scope;
  var ctrl;
  var $httpBackend;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function($rootScope, $controller, _$httpBackend_) {
  	scope = $rootScope.$new();
    $httpBackend = _$httpBackend_;
    $httpBackend.expectGET('http://127.0.0.1:8000/api/sessions').respond(200, [{id: 1}]);
    ctrl = $controller('SessionListCtrl', {
      $scope: scope
  	});
  }));

  it('should fetch sessions', function() {
    $httpBackend.flush();
    expect(scope.sessions[0].id).toBe(1);
  });

});
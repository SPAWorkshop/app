'use strict';

describe('TalkListCtrl', function(){
  var scope;
  var ctrl;
  var $httpBackend;
  var toasty;
  var messages;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function($rootScope, $controller, auth, _$httpBackend_, _toasty_, _messages_) {
    $httpBackend = _$httpBackend_;
    auth.login('test-token');
  	scope = $rootScope.$new();
    $httpBackend.expectGET('http://127.0.0.1:8000/api/talks').respond(200, [{id: 1}]);
    ctrl = $controller('TalkListCtrl', {
      $scope: scope
  	});
    toasty = _toasty_;
    messages = _messages_;
  }));

  it('should fetch talks', function() {
    $httpBackend.flush();
    expect(scope.talks[0].id).toBe(1);
  });

  it('should delete talk', function() {
    $httpBackend.expectDELETE('http://127.0.0.1:8000/api/talks/1').respond(200, '');
    $httpBackend.expectGET('http://127.0.0.1:8000/api/talks').respond(200, []);

    scope.delete({id: 1});

    $httpBackend.flush();
    expect(toasty.hasMessage(messages.TALK_DELETE_SUCCESS)).toBe(true);
    expect(scope.talks.length).toBe(0);
  });

});

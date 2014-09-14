'use strict';

describe('TalkCreateCtrl', function(){
  var scope;
  var ctrl;
  var $httpBackend;
  var $location;
  var toasty;
  var messages;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function($rootScope, $controller, auth, _$httpBackend_, _$location_, _messages_, _toasty_) {
    $httpBackend = _$httpBackend_;
    auth.login('test-token');
    $httpBackend.expectGET('http://127.0.0.1:8000/api/sessions').respond(200, [{id: 1}]);
  	scope = $rootScope.$new();
    ctrl = $controller('TalkCreateCtrl', {
      $scope: scope
  	});
    $location = _$location_;
    toasty = _toasty_;
    messages = _messages_;
  }));

  it('should fetch sessions', function() {
    $httpBackend.flush();
    expect(scope.sessions[0].id).toBe(1);
  });

  it('should submit talk data', function() {
    scope.talk = {
      title: 'New Talk',
      session: 1
    };
    $httpBackend.expectPOST('http://127.0.0.1:8000/api/talks', scope.talk).respond(201, '');

    scope.submit();

    $httpBackend.flush();
    expect(toasty.hasMessage(messages.TALK_CREATE_SUCCESS)).toBe(true);
    expect($location.path()).toBe('/talks');
  });

  it('should handle errors', function() {
    scope.talk = {
      title: 'New Talk',
      session: 1
    };
    $httpBackend.expectPOST('http://127.0.0.1:8000/api/talks', scope.talk).respond(400, {session: ['error']});

    scope.submit();

    $httpBackend.flush();
    expect(scope.errors.session[0]).toBe('error');
  });

});
'use strict';

describe('TalkUpdateCtrl', function(){
  var scope;
  var ctrl;
  var $httpBackend;
  var $location;
  var toasty;
  var messages;

  beforeEach(module('lightningtalks'));

  beforeEach(inject(function($rootScope, $controller, $routeParams, auth, _$httpBackend_, _$location_, _messages_, _toasty_) {
    $httpBackend = _$httpBackend_;
    auth.login('test-token');
  	scope = $rootScope.$new();
    $routeParams.id = 1;
    $httpBackend.expectGET('http://127.0.0.1:8000/api/talks/1').respond(200, {title: 'Old Title'});
    ctrl = $controller('TalkUpdateCtrl', {
      $scope: scope
  	});
    $location = _$location_;
    toasty = _toasty_;
    messages = _messages_;
  }));

  it('should fetch talk', function() {
    $httpBackend.flush();
    expect(scope.talk.title).toBe('Old Title');
  });

  it('should submit talk data', function() {
    scope.talk = {
      title: 'New Talk Name'
    };
    $httpBackend.expectPUT('http://127.0.0.1:8000/api/talks/1', scope.talk).respond(200, '');

    scope.submit();

    $httpBackend.flush();
    expect(toasty.hasMessage(messages.TALK_UPDATE_SUCCESS)).toBe(true);
    expect($location.path()).toBe('/talks');
  });

  it('should handle errors', function() {
    scope.talk = {
      title: ''
    };
    $httpBackend.expectPUT('http://127.0.0.1:8000/api/talks/1', scope.talk).respond(400, {title: ['error']});

    scope.submit();

    $httpBackend.flush();
    expect(scope.errors.title[0]).toBe('error');
  });

});
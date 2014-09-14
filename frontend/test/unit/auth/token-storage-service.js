'use strict';

describe('tokenStorage', function(){
  var tokenStorage;
  var localStorage;

  beforeEach(module('lightningtalks'));

  beforeEach(module(function($provide) {
    localStorage = {
      setItem: function (key, val) {
        localStorage[key] = val;
      },
      removeItem: function () {
        delete localStorage[tokenStorage.TOKEN_KEY];
      },
      getItem: function () {
        return localStorage[tokenStorage.TOKEN_KEY];
      }
    };
    $provide.value('$window', {localStorage: localStorage});
  }));

  beforeEach(inject(function(_tokenStorage_) {
    tokenStorage = _tokenStorage_;
  }));

  it('should set token', function() {
    var token = 'test-token';

    tokenStorage.set(token);

    expect(localStorage[tokenStorage.TOKEN_KEY]).toBe(token);
  });

  it('should remove token', function() {
    localStorage[tokenStorage.TOKEN_KEY] = 'test-token';

    tokenStorage.remove();

    expect(localStorage[tokenStorage.TOKEN_KEY]).toBe(undefined);
  });

  it('should return token', function() {
    localStorage[tokenStorage.TOKEN_KEY] = 'test-token';

    var token = tokenStorage.get();

    expect(token).toBe(localStorage[tokenStorage.TOKEN_KEY]);
  });

  it('should check if token exists', function() {
    localStorage[tokenStorage.TOKEN_KEY] = 'test-token';

    var exists = tokenStorage.has();

    expect(exists).toBe(true);
  });

});
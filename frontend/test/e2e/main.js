'use strict';

describe('The main view', function () {

    beforeEach(function () {
        browser.get('http://localhost:3000');
    });

    it('list navigation items', function() {
        var navItems = element.all(by.css('.navigation__item')).count();
        expect(navItems).toEqual(6);
    });

});

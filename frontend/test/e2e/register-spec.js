
'use strict';

describe('The main view', function () {

    beforeEach(function () {
        browser.get('http://localhost:3000/#/registration');
    });

    it('should show errors when password is not provided', function() {
        var passwordErrors = element.all(by.repeater('error in errors.password'));
        expect(passwordErrors.count()).toEqual(0);

        var email = element(by.model('user.email'));
        email.sendKeys('joe@doe.com');
        element(by.css('.register-button')).click().then(function(){
            expect(passwordErrors.count()).toEqual(1);
        });
    });

    it('redirects to /login upon successfull registration', function() {
        var passwordErrors = element.all(by.repeater('error in errors.password'));
        expect(passwordErrors.count()).toEqual(0);

        var email = element(by.model('user.email'));
        var password = element(by.model('user.password'));

        // TODO: send some random email (otherwiser we might try to register user
        // with already taken email which would end up with an error)
        email.sendKeys('joe21@doe.com');
        email.sendKeys('mypass');

        element(by.css('.register-button')).click().then(function(){
            // TODO: fix test below (check browser API)
            expect(browser.getLocationAbsUrl()).toBe('/#/login');
        });
    });

});

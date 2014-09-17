
'use strict';

describe('The main view', function () {

    beforeEach(function () {
        browser.get('http://localhost:3000/#/registration');
    });

    it('should show errors when password is not provided', function() {
        var passwordErrors = element.all(by.repeater('error in errors.password'));
        expect(passwordErrors.count()).toEqual(0);

        var email = element(by.model('user.email'));
        var firstName = element(by.model('user.first_name'));
        var lastName = element(by.model('user.last_name'));
        email.sendKeys('joe@doe.com');
        firstName.sendKeys('Joe');
        lastName.sendKeys('Doe');
        element(by.css('.register-button')).click().then(function(){
            expect(passwordErrors.count()).toEqual(1);
        });
    });

    it('redirects to /login upon successfull registration', function() {
        var passwordErrors = element.all(by.repeater('error in errors.password'));
        expect(passwordErrors.count()).toEqual(0);

        var email = element(by.model('user.email'));
        var password = element(by.model('user.password'));
        var firstName = element(by.model('user.first_name'));
        var lastName = element(by.model('user.last_name'));

        var emailErrors = element.all(by.repeater('error in errors.email'));
        var passwordErrors = element.all(by.repeater('error in errors.password'));
        var firstNameErrors = element.all(by.repeater('error in errors.first_name'));
        var lastNameErrors = element.all(by.repeater('error in errors.last_name'));

        // TODO: send some random email (otherwiser we might try to register user
        // with already taken email which would end up with an error)
        var userId = (new Date()).getTime();
        email.sendKeys('joe' + userId + '@doe.com');
        firstName.sendKeys('Joe');
        lastName.sendKeys('Doe');
        password.sendKeys('mypass');

        element(by.css('.register-button')).click().then(function(){
            expect(emailErrors.count()).toEqual(0);
            expect(passwordErrors.count()).toEqual(0);
            expect(firstNameErrors.count()).toEqual(0);
            expect(lastNameErrors.count()).toEqual(0);
            expect(browser.getLocationAbsUrl()).toMatch('/#/login');
        });
    });

});

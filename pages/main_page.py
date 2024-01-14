from selene import browser


class MainPage:
    sign_in = 'a.HeaderMenu-link.HeaderMenu-link--sign-in'
    burger_menu = 'button.Button--link.Button--medium.Button[aria-label="Toggle navigation"]'

    def open_page(self):
        browser.open('/')
        return self

    def click_sign_in(self):
        return browser.element(self.sign_in).click()

    def click_burger_menu(self):
        return browser.element(self.burger_menu).click()


main_page = MainPage()

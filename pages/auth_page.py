from selene import browser, query


class AuthPage:
    sign_in_text = '.auth-form-header'

    def get_sign_in_text(self):
        return browser.element(self.sign_in_text).get(query.text)


auth_page = AuthPage()

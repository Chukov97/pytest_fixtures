import allure
from pages.main_page import main_page
from pages.auth_page import auth_page
from pages.base_page import base_page


@allure.title("Desktop login")
def test_github_desktop(browser_management_desktop):
    with allure.step("Open auth page"):
        main_page.open_page()
    with allure.step("Click sign in"):
        main_page.click_sign_in()
    with allure.step("Get text"):
        sign_in_text = auth_page.get_sign_in_text()
    with allure.step("Check sign in text"):
        base_page.assert_equals('Sign in to GitHub', sign_in_text,
                                f'Текст на странице {sign_in_text} отличается от "Sign in to GitHub"')


@allure.title("Mobile login")
def test_github_mobile(browser_management_mobile):
    with allure.step("Open auth page"):
        main_page.open_page()
    with allure.step("Open burger menu"):
        main_page.click_burger_menu()
    with allure.step("Click sign in"):
        main_page.click_sign_in()
    with allure.step("Get text"):
        sign_in_text = auth_page.get_sign_in_text()
    with allure.step("Check sign in text"):
        base_page.assert_equals('Sign in to GitHub', sign_in_text,
                                f'Текст на странице {sign_in_text} отличается от "Sign in to GitHub"')

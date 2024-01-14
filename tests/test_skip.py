import allure
import pytest
from selene import browser
from selenium import webdriver

from pages.auth_page import auth_page
from pages.base_page import base_page
from pages.main_page import main_page
from setting import config


@pytest.fixture(params=[(config.window_height_desktop_1, config.window_width_desktop_1),
                        (config.window_height_desktop_2, config.window_width_desktop_2),
                        (config.window_height_mobile_1, config.window_width_mobile_1),
                        (config.window_height_mobile_2, config.window_width_mobile_2)
                        ])
def browser_management(request):
    height, width = request.param
    browser.config.base_url = config.base_url
    browser.config.timeout = config.timeout
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = config.load_strategy
    browser.config.window_height = height
    browser.config.window_width = width
    browser.config.driver_options = driver_options

    yield

    browser.quit()


@allure.title("Desktop login")
def test_github_desktop(browser_management):
    if (
            browser.config.window_width == config.window_width_mobile_1 and
            browser.config.window_height == config.window_height_mobile_1) or (
            browser.config.window_width == config.window_width_mobile_2 and
            browser.config.window_height == config.window_height_mobile_2):
        pytest.skip("Тест только для Desktop")
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
def test_github_mobile(browser_management):
    if (
            browser.config.window_width == config.window_width_desktop_1 and
            browser.config.window_height == config.window_height_desktop_1) or (
            browser.config.window_width == config.window_width_desktop_2 and
            browser.config.window_height == config.window_height_desktop_2):
        pytest.skip("Тест только для Mobile")
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

import pytest
from selene import browser
from selenium import webdriver
from setting import config


@pytest.fixture(params=[(config.window_height_desktop_1, config.window_width_desktop_1),
                        (config.window_height_desktop_2, config.window_width_desktop_2)])
def browser_management_desktop(request):
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


@pytest.fixture(params=[(config.window_height_mobile_1, config.window_width_mobile_1),
                        (config.window_height_mobile_2, config.window_width_mobile_2)])
def browser_management_mobile(request):
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

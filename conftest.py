import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.data import URLs
from data.helpers import generate_credentials, is_backend_login_working
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage

BACKEND_AUTH_AVAILABLE = is_backend_login_working()


@pytest.fixture
def browser():
    selenoid_url = os.getenv("SELENOID_URL") or os.getenv("SELENOID_URI", "")
    browser_version = os.getenv("BROWSER_VERSION", "128.0")

    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if selenoid_url:
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", browser_version)
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False,
            "screenResolution": "1920x1080x24"
        })
        driver = webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def registered_user(browser):
    name, lastname, username, email, password = generate_credentials()
    signin_page = SigninPage(browser)
    signin_page.open(URLs.BASE_URL)
    signin_page.new_register()
    signup_page = SignupPage(browser)
    signup_page.wait_for_url_change(URLs.REGISTER_URL)
    signup_page.register(name, lastname, username, email, password)
    signup_page.wait_for_url_change(URLs.LOGIN_URL)
    return {
        "name": name,
        "lastname": lastname,
        "username": username,
        "email": email,
        "password": password
    }


@pytest.fixture()
def authorized_user(browser, registered_user):
    if not BACKEND_AUTH_AVAILABLE:
        pytest.skip(
            "Бэкенд требует email-активацию. "
            "Установите SEND_ACTIVATION_EMAIL = False в настройках Djoser."
        )
    auth_page = SigninPage(browser)
    auth_page.open(URLs.BASE_URL)
    auth_page.go_login()
    auth_page.wait_for_url_change(URLs.LOGIN_URL)
    auth_page.login(registered_user["email"], registered_user["password"])
    auth_page.wait_for_url_change(URLs.RECIPES_URL)
    return registered_user

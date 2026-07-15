import json
import os
import random
import string
from urllib import request, error as urllib_error

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.data import URLs
from data.helpers import generate_credentials
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage


def _is_backend_login_working():
    try:
        rand = ''.join(random.choices(string.digits, k=8))
        email = f'check{rand}@test.com'
        password = f'Test@123!{rand[:4]}'
        username = f'check_{rand}'
        api_base = URLs.BASE_URL.rstrip('/')

        reg_data = json.dumps({
            'email': email, 'password': password, 'username': username,
            'first_name': 'Check', 'last_name': 'User'
        }).encode()
        req = request.Request(
            f'{api_base}/api/users/',
            data=reg_data,
            headers={'Content-Type': 'application/json'}
        )
        resp = request.urlopen(req, timeout=10)
        if resp.status != 201:
            return False

        login_data = json.dumps({
            'email': email, 'password': password
        }).encode()
        req2 = request.Request(
            f'{api_base}/api/auth/token/login/',
            data=login_data,
            headers={'Content-Type': 'application/json'}
        )
        resp2 = request.urlopen(req2, timeout=10)
        return resp2.status == 200
    except Exception:
        return False


BACKEND_AUTH_AVAILABLE = _is_backend_login_working()


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
    browser.get(URLs.BASE_URL)
    signin_page = SigninPage(browser)
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
    browser.get(URLs.BASE_URL)
    auth_page = SigninPage(browser)
    auth_page.go_login()
    auth_page.wait_for_url_change(URLs.LOGIN_URL)
    auth_page.login(registered_user["email"], registered_user["password"])
    auth_page.wait_for_url_change(URLs.RECIPES_URL)
    return registered_user

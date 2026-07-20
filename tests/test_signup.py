import allure
from pages.signup_page import SignupPage
from data.data import URLs
from data.helpers import generate_credentials


@allure.title("Регистрация пользователя")
class TestSignup:

    @allure.story("Проверка формы регистрации")
    def test_registration_form_displayed(self, browser):
        signup = SignupPage(browser)

        with allure.step("Открыть страницу регистрации"):
            signup.open(URLs.REGISTER_URL)

        with allure.step("Проверить отображение формы регистрации"):
            assert signup.check_elem(), "Форма регистрации не отображается"

        with allure.step("Проверить URL страницы регистрации"):
            assert signup.get_current_url() == URLs.REGISTER_URL, \
                f"Открыт неверный URL: {signup.get_current_url()}"

    @allure.story("Проверка регистрации и перехода на страницу входа")
    def test_registration_redirects_to_login(self, browser):
        name, lastname, username, email, password = generate_credentials()
        signup = SignupPage(browser)

        with allure.step("Открыть страницу регистрации"):
            signup.open(URLs.REGISTER_URL)

        with allure.step("Заполнить форму регистрации"):
            signup.register(name, lastname, username, email, password)

        with allure.step("Проверить переход на страницу входа"):
            signup.wait_for_url_change(URLs.LOGIN_URL)
            assert signup.get_current_url() == URLs.LOGIN_URL, \
                f"Не выполнен переход на страницу входа: {signup.get_current_url()}"

        with allure.step("Проверить отображение формы входа"):
            assert signup.check_elem(), "Форма входа не отображается"

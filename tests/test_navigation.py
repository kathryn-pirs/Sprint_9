import allure
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from pages.recipes_list_page import RecipesListPage
from data.data import URLs


@allure.title("Навигация между страницами")
class TestNavigation:

    @allure.story("Проверка перехода на страницу входа")
    def test_navigate_to_signin(self, browser):
        signin = SigninPage(browser)

        with allure.step("Открыть страницу входа"):
            signin.open(URLs.LOGIN_URL)

        with allure.step("Проверить, что форма входа отображается"):
            assert signin.check_elem(), "Форма входа не отображается"

    @allure.story("Проверка перехода на страницу регистрации")
    def test_navigate_to_signup(self, browser):
        signup = SignupPage(browser)

        with allure.step("Открыть страницу регистрации"):
            signup.open(URLs.REGISTER_URL)

        with allure.step("Проверить, что форма регистрации отображается"):
            assert signup.check_elem(), "Форма регистрации не отображается"

    @allure.story("Проверка перехода на страницу рецептов")
    def test_navigate_to_recipes(self, browser):
        recipes = RecipesListPage(browser)

        with allure.step("Открыть страницу рецептов"):
            recipes.open()

        with allure.step("Проверить, что карточки рецептов отображаются"):
            assert recipes.is_recipe_card_present(), \
                "Карточки рецептов не отображаются"

    @allure.story("Проверка перехода по ссылке «Создать аккаунт»")
    def test_navigate_to_signup_via_link(self, browser):
        signin = SigninPage(browser)
        signup = SignupPage(browser)

        with allure.step("Открыть страницу входа"):
            signin.open(URLs.LOGIN_URL)

        with allure.step("Нажать «Создать аккаунт»"):
            signin.new_register()

        with allure.step("Проверить переход на страницу регистрации"):
            signup.wait_for_url_change(URLs.REGISTER_URL)
            assert signup.get_current_url() == URLs.REGISTER_URL, \
                f"Открыт неверный URL: {signup.get_current_url()}"
            assert signup.check_elem(), "Форма регистрации не отображается"

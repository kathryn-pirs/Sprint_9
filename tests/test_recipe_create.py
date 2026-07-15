import allure
from pages.signin_page import SigninPage
from pages.recipe_create_page import RecipeCreatePage
from data.data import URLs, RECIPE_DATA_SETS
from data.helpers import generate_recipe_data


@allure.title("Создание рецепта")
class TestRecipeCreate:

    @allure.story("Проверка создания рецепта и отображения на главной")
    def test_create_recipe(self, browser, authorized_user):
        create_page = RecipeCreatePage(browser)
        login = SigninPage(browser)

        with allure.step("Переход на страницу создания рецепта"):
            create_page.go_create_recipe()
            create_page.wait_for_url_change(URLs.CREATE_URL)
            assert browser.current_url == URLs.CREATE_URL, \
                f"Открыт неверный URL: {browser.current_url}"

        with allure.step("Заполнение формы и создание рецепта"):
            recipe_data = generate_recipe_data(RECIPE_DATA_SETS)
            create_page.fill_recipe_form(
                name=recipe_data["name"],
                description=recipe_data["description"],
                time=recipe_data["time"],
                amount=recipe_data["amount"],
                ingredients=recipe_data["ingredients"],
                tag=recipe_data["tag"],
                patch_image=recipe_data["patch_image"],
            )

        with allure.step("Проверить кнопку «Выход» на главной"):
            login.open(URLs.BASE_URL)
            assert login.check_elem_logout(), "Кнопка выхода не отображается"

        with allure.step("Проверить карточку рецепта и название"):
            assert create_page.is_recipe_card_displayed(recipe_data["name"]), \
                f"Карточка рецепта «{recipe_data['name']}» не найдена на странице"

        with allure.step("Выход из аккаунта"):
            create_page.go_logout()
            login.wait_for_url_change(URLs.RECIPES_URL)
            assert browser.current_url == URLs.RECIPES_URL, \
                f"Открыт неверный URL: {browser.current_url}"

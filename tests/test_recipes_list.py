import allure
from pages.recipes_list_page import RecipesListPage


@allure.title("Просмотр списка рецептов")
class TestRecipesList:

    @allure.story("Проверка отображения карточек рецептов")
    def test_recipe_cards_displayed(self, browser):
        recipes = RecipesListPage(browser)

        with allure.step("Открыть страницу рецептов"):
            recipes.open()

        with allure.step("Проверить, что карточки рецептов отображаются"):
            assert recipes.is_recipe_card_present(), \
                "Карточки рецептов не найдены на странице"

    @allure.story("Проверка названий рецептов")
    def test_recipe_titles_not_empty(self, browser):
        recipes = RecipesListPage(browser)

        with allure.step("Открыть страницу рецептов"):
            recipes.open()

        with allure.step("Получить названия рецептов"):
            titles = recipes.get_recipe_titles()

        with allure.step("Проверить, что есть хотя бы одно название"):
            assert len(titles) > 0, "Названия рецептов отсутствуют"

        with allure.step("Проверить, что названия не пустые"):
            for title in titles:
                assert title.strip(), "Найдено пустое название рецепта"

    @allure.story("Проверка наличия карточек рецептов")
    def test_multiple_cards_present(self, browser):
        recipes = RecipesListPage(browser)

        with allure.step("Открыть страницу рецептов"):
            recipes.open()

        with allure.step("Проверить количество карточек"):
            count = recipes.get_card_count()
            assert count > 0, \
                f"Ожидалась хотя бы одна карточка, найдено: {count}"

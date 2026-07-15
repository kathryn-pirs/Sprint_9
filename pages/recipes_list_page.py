from .base_page import BasePage
from locators import RecipesListLocators
from data.data import URLs


class RecipesListPage(BasePage):

    def open(self):
        self.driver.get(URLs.RECIPES_URL)
        self.wait_for_overlay(RecipesListLocators.RECIPE_CARD)

    def is_page_loaded(self):
        return self.is_element_present(RecipesListLocators.RECIPE_CARD)

    def get_recipe_cards(self):
        return self.driver.find_elements(*RecipesListLocators.RECIPE_CARD)

    def get_recipe_titles(self):
        titles = self.driver.find_elements(*RecipesListLocators.RECIPE_TITLE_LINK)
        return [t.text for t in titles if t.text.strip()]

    def get_card_count(self):
        return len(self.get_recipe_cards())

    def click_first_recipe(self):
        cards = self.driver.find_elements(*RecipesListLocators.RECIPE_TITLE_LINK)
        if cards:
            cards[0].click()

    def is_recipe_card_present(self):
        return self.is_element_present(RecipesListLocators.RECIPE_CARD)

    def is_tag_checkbox_present(self):
        return self.is_element_present(RecipesListLocators.TAG_CHECKBOX)

    def click_tag(self, tag_name):
        locator = RecipesListLocators.tag_button(tag_name)
        self.click_with_wait(locator)

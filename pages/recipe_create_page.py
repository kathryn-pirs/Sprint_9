from .base_page import BasePage
from locators import RecipeCreateLocators


class RecipeCreatePage(BasePage):

    def go_create_recipe(self):
        self.click_with_wait(RecipeCreateLocators.CREATE_BUTTON_MAIN)

    def go_logout(self):
        self.click_with_wait(RecipeCreateLocators.LOGOUT_BUTTON)

    def fill_recipe_form(self, name, description, time, amount, ingredients, tag, patch_image):
        self.wait_for_overlay(RecipeCreateLocators.NAME_INPUT)
        self.input_text(RecipeCreateLocators.NAME_INPUT, name)
        self.click_with_wait(RecipeCreateLocators.tag_button(tag))
        self.input_text(RecipeCreateLocators.INGREDIENT_NAME_INPUT, ingredients)
        self.wait_for_overlay(RecipeCreateLocators.ingredient_dropdown_item(ingredients))
        self.click_with_wait(RecipeCreateLocators.ingredient_dropdown_item(ingredients))
        self.input_text(RecipeCreateLocators.INGREDIENT_AMOUNT_INPUT, amount)
        self.click_with_wait(RecipeCreateLocators.ADD_INGREDIENT_BUTTON)
        self.input_text(RecipeCreateLocators.COOKING_TIME_INPUT, time)
        self.input_text(RecipeCreateLocators.DESCRIPTION_INPUT, description)
        self.upload_file(RecipeCreateLocators.PHOTO_UPLOAD_INPUT, patch_image)
        self.click(RecipeCreateLocators.CREATE_BUTTON)
        self.click(RecipeCreateLocators.RECIPE_BUTTON)

    def is_recipe_card_displayed(self, name):
        if not self.is_element_visible(RecipeCreateLocators.recipe_card_by_name(name)):
            return False
        self.refresh()
        return self.is_element_present(RecipeCreateLocators.recipe_card_by_name(name))
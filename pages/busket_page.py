from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.locators import BusketPageLocators


class BusketPage(BasePage):

    def should_be_the_same_price(self):
        check_product_price = self.browser.find_element(*BusketPageLocators.CHECK_CART_PRODUCT_PRICE)
        check_product_price_general = self.browser.find_element(*BusketPageLocators.CHECK_CART_GENERAL_PRICE)
        assert check_product_price.text == check_product_price_general.text, 'The price is not the same'
        print('Всё отлично цена совпадает')
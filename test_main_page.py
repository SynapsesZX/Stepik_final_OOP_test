from selenium import webdriver
import pytest

driver = webdriver.Chrome(executable_path='C:\Selenium Chrome\chromedriver.exe')

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language(browser):
    driver.get(link)
    add_to_cart_button = driver.find_element_by_xpath("//button[contains(text(),'Добавить в корзину')]").is_displayed()
    assert add_to_cart_button, 'element not displayed!'



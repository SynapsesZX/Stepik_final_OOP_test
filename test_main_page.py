import time

from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.book_page import BookPage






def login_page_log_button(browser):
    login_button = browser.find_element_by_css_selector("#login_link")
    login_button.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open_link()
    page.go_to_the_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open_link()
    page.should_be_login_link()

def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open_link()
    page.should_be_login_url()

def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open_link()
    page.should_be_login_form()

def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open_link()
    page.should_be_register_form()

def test_guest_can_go_to_login_page_with_return(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open_link()
    page.go_to_the_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()





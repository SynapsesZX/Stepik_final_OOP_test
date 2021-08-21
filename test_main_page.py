from selenium import webdriver
from pages.main_page import MainPage
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome(executable_path='C:\Selenium Chrome\chromedriver.exe')




def login_page_log_button(browser):
    login_button = browser.find_element_by_css_selector("#login_link")
    login_button.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser,link)
    page.open_link()
    page.go_to_the_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open_link()
    page.should_be_login_link()

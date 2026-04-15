import pytest
from locators import TestLocators
from urls import Urls
from helpers import login_user
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNavigation:
    
    def test_go_from_account_to_constructor_by_button(self, driver):
        driver.get(Urls.LOGIN_PAGE)
        login_user(driver)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.GOTO_Personal_Cabinet_Button)).click()
        driver.find_element(*TestLocators.GOTO_Constructor_Button).click()

        assert driver.current_url == Urls.MAIN_URL


    def test_go_from_account_to_constructor_by_logo(self, driver):
        driver.get(Urls.LOGIN_PAGE)
        login_user(driver)
        driver.find_element(*TestLocators.GOTO_Personal_Cabinet_Button).click()
        WebDriverWait(driver, 10).until(EC.url_contains(Urls.PROFILE_PAGE))

        driver.find_element(*TestLocators.GOTO_Logo_Button).click()

        assert driver.current_url == Urls.MAIN_URL

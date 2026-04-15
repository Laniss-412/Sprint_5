import pytest
from locators import TestLocators
from urls import Urls
from helpers import login_user
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAccount:
    def test_go_to_personal_cabinet(self, driver):
        driver.get(Urls.LOGIN_PAGE)
        login_user(driver)

        driver.find_element(*TestLocators.GOTO_Personal_Cabinet_Button).click()
        WebDriverWait(driver, 5).until(EC.url_contains(Urls.PROFILE_PAGE))

        assert Urls.PROFILE_PAGE in driver.current_url


    def test_logout(self, driver):
        driver.get(Urls.LOGIN_PAGE)
        login_user(driver)

        driver.find_element(*TestLocators.GOTO_Personal_Cabinet_Button).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGOUT_profile_button))
        driver.find_element(*TestLocators.LOGOUT_profile_button).click()

        WebDriverWait(driver, 5).until(EC.url_contains(Urls.LOGIN_PAGE))
        assert Urls.LOGIN_PAGE in driver.current_url
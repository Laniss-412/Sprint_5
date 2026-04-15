import pytest
from locators import TestLocators
from urls import Urls
from helpers import login_user
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(Urls.MAIN_URL)

        driver.find_element(*TestLocators.LOGIN_Main_Button).click()
        login_user(driver)

        button_text = driver.find_element(*TestLocators.MAIN_order_button).text
        assert button_text == "Оформить заказ"


    def test_login_from_personal_cabinet(self, driver):
        driver.get(Urls.LOGIN_PAGE)

        driver.find_element(*TestLocators.GOTO_Personal_Cabinet_Button).click()
        login_user(driver)

        assert driver.current_url == Urls.MAIN_URL

    
    def test_login_from_registration_from(self, driver):
        driver.get(Urls.REGISTRATION_PAGE)

        driver.find_element(*TestLocators.LOGIN_Form_Registration).click()
        login_user(driver)

        assert driver.current_url == Urls.MAIN_URL

    def test_login_from_recovery_dorm(self, driver):
        driver.get(Urls.FORGOT_PASSWORD)

        driver.find_element(*TestLocators.LOGIN_Password_Recovery_Form).click()
        login_user(driver)

        assert driver.current_url == Urls.MAIN_URL

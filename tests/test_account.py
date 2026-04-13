import pytest
from locators import TestLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAccount:
    def test_go_to_personal_cabinet(self, driver):
        driver.get("https://stellarburgers.education-services.ru/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_Email_Input))

        driver.find_element(*TestLocators.LOGIN_Email_Input).send_keys("ashakov_43_123@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_Password_Input).send_keys("12345678")
        driver.find_element(*TestLocators.LOGIN_Button).click()

        driver.find_element(*TestLocators.GOTO_Personal_Cabinet_Button).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account/profile"))

        assert "/account/profile" in driver.current_url


    def test_logout(self, driver):
        driver.get("https://stellarburgers.education-services.ru/login")
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_Email_Input))

        driver.find_element(*TestLocators.LOGIN_Email_Input).send_keys("ashakov_43_123@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_Password_Input).send_keys("12345678")
        driver.find_element(*TestLocators.LOGIN_Button).click()
        driver.find_element(*TestLocators.GOTO_Personal_Cabinet_Button).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.LOGOUT_profile_button)).click()

        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
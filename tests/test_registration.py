import pytest
import random
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    def test_registration_success(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.REG_Password_Input))
        email = f'ashakov_43_{random.randint(100, 999)}@ya.ru'

        driver.find_element(*TestLocators.REG_Name_Input).send_keys("Игорь")
        driver.find_element(*TestLocators.REG_Email_Input).send_keys(email)
        driver.find_element(*TestLocators.REG_Password_Input).send_keys("12345678")
        driver.find_element(*TestLocators.REG_Button).click()

        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url 


    def test_registration_short_password_error(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(*TestLocators.REG_Password_Input).send_keys("123")
        driver.find_element(*TestLocators.REG_Button).click()

        error = driver.find_element(*TestLocators.REG_Password_Error)
        assert error.text == "Некорректный пароль"

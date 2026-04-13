import pytest
from locators import TestLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def login_user(self, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_Email_Input))
        driver.find_element(*TestLocators.LOGIN_Email_Input).send_keys("ashakov_43_123@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_Password_Input).send_keys("12345678")
        driver.find_element(*TestLocators.LOGIN_Button).click()

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
    
    def test_login_from_main_page(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")

        driver.find_element(*TestLocators.LOGIN_Main_Button).click()
        self.login_user(driver)

        button_text = driver.find_element(*TestLocators.MAIN_order_button).text
        assert button_text == "Оформить заказ"


    def test_login_from_personal_cabinet(self, driver):
        driver.get("https://stellarburgers.education-services.ru/login")

        driver.find_element(*TestLocators.GOTO_Personal_Cabinet_Button).click()
        self.login_user(driver)

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    
    def test_login_from_registration_from(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")

        driver.find_element(*TestLocators.LOGIN_Form_Registration).click()
        self.login_user(driver)

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_login_from_recovery_dorm(self, driver):
        driver.get("https://stellarburgers.education-services.ru/forgot-password")

        driver.find_element(*TestLocators.LOGIN_Password_Recovery_Form).click()
        self.login_user(driver)

        assert driver.current_url == "https://stellarburgers.education-services.ru/"

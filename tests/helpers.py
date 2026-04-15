from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import Urls

def login_user(driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.LOGIN_Email_Input))
        driver.find_element(*TestLocators.LOGIN_Email_Input).send_keys("ashakov_43_123@yandex.ru")
        driver.find_element(*TestLocators.LOGIN_Password_Input).send_keys("12345678")
        driver.find_element(*TestLocators.LOGIN_Button).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_URL))
import pytest
from locators import TestLocators
from selenium.webdriver.chrome.webdriver import WebDriver

class TestConstructor:
    def test_switch_to_sauces(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        driver.find_element(*TestLocators.SECTION_Sauces).click()
        active_tab = driver.find_element(*TestLocators.SECTION_Sauces).get_attribute("class")
        assert "tab_tab_type_current" in active_tab

    
    def test_switch_to_fillings(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        driver.find_element(*TestLocators.SECTION_Fillings).click()
        active_tab = driver.find_element(*TestLocators.SECTION_Fillings).get_attribute("class")
        assert "tab_tab_type_current" in active_tab

    
    def test_switch_to_buns(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")

        driver.find_element(*TestLocators.SECTION_Sauces).click()
        driver.find_element(*TestLocators.SECTION_Buns).click()
        active_tab = driver.find_element(*TestLocators.SECTION_Buns).get_attribute("class")
        assert "tab_tab_type_current" in active_tab
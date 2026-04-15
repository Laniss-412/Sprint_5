import pytest
from locators import TestLocators
from urls import Urls
from selenium.webdriver.chrome.webdriver import WebDriver

class TestConstructor:
   
   @pytest.mark.parametrize("locator", [TestLocators.SECTION_Sauces, TestLocators.SECTION_Fillings, TestLocators.SECTION_Buns])
   def test_switch_sections(self, driver, locator):
      driver.get(Urls.MAIN_URL)

      if locator == TestLocators.SECTION_Buns:
         driver.find_element(*TestLocators.SECTION_Sauces).click()
    
      driver.find_element(*locator).click()

      active_tab = driver.find_element(*locator).get_attribute("class")
      assert "tab_tab_type_current" in active_tab
        
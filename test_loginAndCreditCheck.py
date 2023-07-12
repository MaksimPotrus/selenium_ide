import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from logger import LoggerABM,verify
@pytest.mark.usefixtures("setup")
class TestLoginAndAdd:

    def setup_method(self, method):
        # self.driver = webdriver.Chrome()

        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.first_tests
    def test_login_and_add(self):
        log = LoggerABM.sample_logger()

        # self.driver.get("https://manage.sugarwish.com/")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.XPATH, "//span[contains(.,\'Sign In\')]").click()
        log.info("\nclick on //span[contains(.,\'Sign In\')]")
        self.driver.find_element(By.XPATH, "//input[@id=\'username\']").click()
        log.info("\nclick on //input[@id=\'username\']")
        self.driver.find_element(By.XPATH, "//input[@id=\'username\']").send_keys(
            "mykola_plakhotnik@pecodesoftware.com")
        log.info("\nsend email")
        self.driver.find_element(By.XPATH, "//input[@id=\'password\']").click()
        log.info("\nclick on //input[@id=\'password\']")
        self.driver.find_element(By.XPATH, "//input[@id=\'password\']").send_keys("XOiz,NoIgQ-gjABROSfbqXd3")
        log.info("\nsend password")
        self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
        log.info("\nclick on submit")
        verify(self.driver.find_element(By.XPATH, "//a[@id='desktopAccountDropdown']/span/span[2]").is_displayed(),
               'element is not displayed',
               'element is displayed')
        log.info("\nverify that element is displayed")
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[@id='desktopAccountDropdown']/span/span[2]")))
        element.click()
        self.driver.find_element(By.XPATH, "//a[@class='sugarwish-dashboard-item']//span[text()='Happiness Dashboard']").click()
        log.info("\ncredit is " + self.driver.find_element(By.XPATH, "//div[@class='credit-info__amount']//span[@class='amount']").text)
        assert self.driver.find_element(By.XPATH, "//div[@class='credit-info__amount']//span[@class='amount']").text == "$0.00"
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[@id='desktopAccountDropdown']/span/span[2]")))
        element.click()
        log.info("\nclick on //a[@id='desktopAccountDropdown']/span/span[2]")
        self.driver.find_element(By.XPATH, "//a[contains(.,\'Log Out\')]").click()
        log.info("\nclick on //a[contains(.,\'Log Out\')]")
        self.driver.close()
        log.info("\ntest finish")
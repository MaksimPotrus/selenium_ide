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
class TestPayment:

    def setup_method(self, method):
        # self.driver = webdriver.Chrome()

        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.first_tests
    def test_payment(self):
        actions = ActionChains(self.driver)
        log = LoggerABM.sample_logger()
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
        self.driver.find_element(By.XPATH, "//span[contains(@class, 'sugarwish-dropdown-text')]").click()
        self.driver.find_element(By.XPATH, "//div[@class='products-wrapper']//a[@href='/products/candy']").click()
        log.info("\nopen candy page")
        self.driver.find_element(By.XPATH, "//label[@class='size-option__field ' and @for='option157']").click()
        log.info("\nclick on send sugarwishes ")
        assert self.driver.find_element(By.XPATH, "//h6[@id='totalPrice']").text == "$25"
        log.info("\nprice is correct 25")
        actions.move_to_element(self.driver.find_element(By.XPATH, "//span[@class='all-counts']")).perform()
        self.driver.find_element(By.XPATH, "//a[@id='showCustomSelectModal']").click()
        actions.move_to_element(self.driver.find_element(By.XPATH, "//span[@class='text-light']")).perform()
        self.driver.find_element(By.XPATH, "//div[@id='collapseOne']//a[contains(@class,'step1_continue')]").click()
        log.info("\nclick on second continue")
        actions.move_to_element(self.driver.find_element(By.XPATH, "//a[@data-ecard_id='15651']")).perform()
        self.driver.find_element(By.XPATH, "//a[contains(@class,'items-wrap')]").click()
        log.info("\nchoose a picture")
        self.driver.find_element(By.XPATH, "//div[contains(@class,'show')]//button[@onclick='continueStep()']").click()
        log.info("\nenter manually click")
        self.driver.find_element(By.XPATH, "//input[@id='receiver-name1']").send_keys("Test name")
        log.info("\ninput name")
        self.driver.find_element(By.XPATH, "//input[@id='receiver-email1']").send_keys("test@test.com")
        log.info("\ninput email")
        actions.scroll_by_amount(500, 500).perform()
        actions.move_to_element(self.driver.find_element(By.XPATH, "//a[@id='continue-btn-1']"))
        self.driver.find_element(By.XPATH, "//a[@id='continue-btn-1']").click()
        self.driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        actions.move_to_element(self.driver.find_element(By.XPATH, "//form[@id='pay-with-paypal']")).perform()
        self.driver.find_element(By.XPATH, "//button[contains(@class,'charge-card-on-file-btn')]").click()
        verify(self.driver.find_element(By.XPATH, "//p[text()='Your order is complete.']").is_displayed(),
               "message is displayed"
               "message is not displayed")
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
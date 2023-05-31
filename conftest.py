import os
import logging
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from logger import LoggerABM

logger = LoggerABM.sample_logger(logLevel=logging.INFO)

@pytest.fixture
def setup(request):
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--headless")
    logger.info("\nstart chrome browser for test")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    logger.info("\nstart ")
    # driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://manage.sugarwish.com/")
    request.cls.driver = driver
    yield driver
    logger.info("quit browser..")
    driver.quit()
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://dev:abmdev321@staging.autobidmaster.com/en/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file_name = str(int(round(time.time() * 1000))) + ".png"
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name

            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "ABM_Automation_Report"

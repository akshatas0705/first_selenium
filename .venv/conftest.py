import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from datetime import datetime


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


# Hook for capturing screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs["setup"]

        screenshots_dir = "reports/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
        file_path = os.path.join(screenshots_dir, file_name)

        driver.save_screenshot(file_path)

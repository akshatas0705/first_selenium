import pytest
from pages.login_page import LoginPage


def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    #comment
    assert "inventory" in driver.current_url


def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.enter_username("invalid_user")
    login.enter_password("wrong_password")
    login.click_login()

    error = login.get_error_message()
    assert "Username and password do not match" in error

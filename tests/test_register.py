import json
import time

import pytest
from selenium.webdriver.common.by import By

from Po.LoginPage import LoginPage
from Po.RegisterPage import RegisterPage
from tests.conftest import browser_selection

test_path = "../reg_data/userdata.json"
with open(test_path, 'r') as f:
    test_data = json.load(f)
    test_list = test_data["data"]
@pytest.mark.parametrize("test_list_item", test_list)
def test_register(browser_selection, test_list_item):
    driver = browser_selection
    user_creation = RegisterPage(driver)
    user_creation.register(test_list_item["firstname"],test_list_item["lastname"],test_list_item["street"],test_list_item["city"],test_list_item["user_name"],test_list_item["password"],test_list_item["re_enter"],test_list_item["state"],test_list_item["zip"],test_list_item["ph_no"],test_list_item["ssn"])
    time.sleep(3)

@pytest.mark.parametrize("test_list_item", test_list)
def test_login(browser_selection, test_list_item):
    driver = browser_selection
    login_action = LoginPage(driver)
    login_action.login(test_list_item["user_name"],test_list_item["password"])
    print("hi")


import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="selecting browser"
    )
@pytest.fixture(scope="function")
def browser_selection(request):
    driver = None
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    yield driver
    driver.close()


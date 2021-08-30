from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['QA'] = 'Sukalpa'
    config._metadata['Env'] = 'Test'


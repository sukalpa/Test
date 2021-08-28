from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup():
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    return driver
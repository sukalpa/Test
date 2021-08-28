from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

from POM.LoginScreen import Login


class Test_login:

    @pytest.mark.usefixtures
    def test_001(self,setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.lp =Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        time.sleep(5)
        self.lp.cliklogin()
        time.sleep(5)
        self.driver.save_screenshot("C:\\Users\\sukal\\PycharmProjects\\Test\\screenshot\\"+"test.png")
        self.driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from utilities.logger import LoggGeneration
from POM.LoginScreen import Login
from utilities.readProperties import Readconfig
from utilities import xlUtility


class Test_login:
    URL = Readconfig.baseurl()
    path ="C:\\Users\\sukal\\PycharmProjects\\FrameworkDesign\\TestData\\LoginData.xlsx"
    username = Readconfig.username()
    password = Readconfig.password()
    logger = LoggGeneration.logGenerate()

    @pytest.mark.usefixtures
    def test_002_DDT(self,setup):
        self.logger.info("***********test_002_DDT************")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = xlUtility.getRowCount(self.path,'Sheet1')
        for r in range(2,self.rows+1):
            self.username_ID = xlUtility.readdata(self.path,'Sheet1',r,1)
            self.password_ID = xlUtility.readdata(self.path, 'Sheet1', r, 2)
            time.sleep(2)
            self.lp.cliklogin()
            time.sleep(5)
            self.driver.quit()






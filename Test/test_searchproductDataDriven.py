import time
import pytest

from POM.SearchProduct import search_Product
from utilities import xlUtility
from utilities.logger import LoggGeneration

from POM.LoginScreen import Login
from utilities.readProperties import Readconfig


class Test_Searchproduct():
    URL = Readconfig.baseurl()
    username = Readconfig.username()
    password = Readconfig.password()
    logger = LoggGeneration.logGenerate()
    path = "C:\\Users\\sukal\\Desktop\\SearchProduct.xlsx"

    @pytest.mark.usefixtures
    def test_searchproduct(self,setup):
        self.logger.info("***********test_001************")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.lp =Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        time.sleep(5)
        self.lp.cliklogin()
        time.sleep(5)
        self.sp = search_Product(self.driver)
        self.sp.Catalog_Menu()
        self.sp.Catalog_SubMenu()
        self.sp.ProductName("Build your own computer")
        self.Category = xlUtility.readfromexcel(self.path,"Sheet1")
        self.sp.Category(self.Category)
        self.sp.Manufacturer = xlUtility.readfromexcel(self.path,"Sheet1")
        self.sp.Vendor = xlUtility.readfromexcel(self.path, "Sheet1")
        self.sp.Warehouse = xlUtility.readfromexcel(self.path, "Sheet1")
        self.sp.Producttype = xlUtility.readfromexcel(self.path, "Sheet1")
        self.sp.Published = xlUtility.readfromexcel(self.path, "Sheet1")
        time.sleep(10)
        self.sp.Search()
        time.sleep(5)
        self.lp.logout()
        self.driver.quit()
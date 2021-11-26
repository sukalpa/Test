from selenium.webdriver.support.ui import Select
class search_Product:

    Catalog_Menu_xpath="//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]"
    Catalog_Product_submenu_xpath= "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]"
    Product_name_txt_xpath = "//input[@id='SearchProductName']"
    Category_dropdown_xpath = "//select[@id='SearchCategoryId']"
    Manufacturer_dropdown_xpath = "//select[@id='SearchManufacturerId']"
    Vendor_dropdown_xpath = "//select[@id='SearchVendorId']"
    Warehouse_dropdown_xpath = "//select[@id='SearchWarehouseId']"
    Product_Type_dropdown_xpath = "//select[@id='SearchProductTypeId']"
    Published_dropdown_xpath = "//select[@id='SearchPublishedId']"
    Search_button = "//button[@id='search-products']"

    def __init__(self,driver):
        self.driver = driver

    def Catalog_Menu(self):
        self.driver.find_element_by_xpath(self.Catalog_Menu_xpath).click()

    def Catalog_SubMenu(self):
        self.driver.find_element_by_xpath(self.Catalog_Product_submenu_xpath).click()

    def ProductName(self,productname):
        self.driver.find_element_by_xpath(self.Product_name_txt_xpath).clear()
        self.driver.find_element_by_xpath(self.Product_name_txt_xpath).send_keys(productname)

    def Category(self,Category):
        list = self.driver.find_element_by_xpath(self.Category_dropdown_xpath)
        sel = Select(list)
        sel.select_by_index(Category)


    def Manufacturer(self,Manufact):
        list = self.driver.find_element_by_xpath(self.Manufacturer_dropdown_xpath)
        sel = Select(list)
        sel.select_by_index(Manufact)

    def Vendor(self,Vendor):
        list = self.driver.find_element_by_xpath(self.Vendor_dropdown_xpath)
        sel = Select(list)
        sel.select_by_index(Vendor)

    def Warehouse(self,Warehouse):
        list = self.driver.find_element_by_xpath(self.Warehouse_dropdown_xpath)
        sel = Select(list)
        sel.select_by_index(Warehouse)

    def ProductType(self,Pro_Type):
        list = self.driver.find_element_by_xpath(self.Product_Type_dropdown_xpath)
        sel = Select(list)
        sel.select_by_index(Pro_Type)
    def Published(self,Published):
        list = self.driver.find_element_by_xpath(self.Published_dropdown_xpath)
        sel = Select(list)
        sel.select_by_index(Published)

    def Search(self):
        self.driver.find_element_by_xpath(self.Search_button).click()







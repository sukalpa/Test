from selenium.webdriver.support.ui import Select
class search_Product:

    Catalog_Menu_xpath="//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]"
    Catalog_Product_submenu_xpath= "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]"
    Product_name_txt_xpath = "//input[@id='SearchProductName']"
    Category_dropdown_xpath = "//select[@id='SearchCategoryId']"
    Manufacturer_dropdown_xpath = "//select[@id='SearchManufacturerId']"
    Vendor_dropdown_xpath = "//select[@id='SearchVendorId']/option[1]"
    Warehouse_dropdown_xpath = "//select[@id='SearchWarehouseId']/option[1]"
    Product_Type_dropdown_xpath = "//select[@id='SearchProductTypeId']/option[1]"
    Published_dropdown_xpath = "//select[@id='SearchPublishedId']/option[1]"
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

    def Vendor(self):
        self.driver.find_element_by_xpath(self.Vendor_dropdown_xpath).click()

    def Warehouse(self):
        self.driver.find_element_by_xpath(self.Warehouse_dropdown_xpath).click()

    def ProductType(self):
        self.driver.find_element_by_xpath(self.Product_Type_dropdown_xpath).click()
    def Published(self):
        self.driver.find_element_by_xpath(self.Published_dropdown_xpath).click()

    def Search(self):
        self.driver.find_element_by_xpath(self.Search_button).click()







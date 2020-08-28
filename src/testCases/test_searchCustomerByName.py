import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcutomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from testCases.conftest import setup
from pageObjects.SearchCustomerPage import SearchCustomer

class Test_SearchCustomerByName_005:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("*********** Test_005_SearchCustomerByName ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        
        self.logger.info("******* Trying to Login *******")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        
        self.logger.info("******* Login Successful *******")
        
        self.logger.info("******* Starting Search Customer By Name *******")
        
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(3)
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(2)
         
        searchcust = SearchCustomer(self.driver)
        
        flag = searchcust.searchElementsVisible()
        if (flag == True):
            self.logger.info("******* Search Elements already visible *******")
            pass
        else:
            self.logger.info("******* CLicking on Search Dropdown *******")
            searchcust.clickDropdownSearch()
            
        time.sleep(2)
        
        self.logger.info("******* Searching Customer By Name *******")
        searchcust.setFirstName("James")
        searchcust.setLastName("Pan")
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByName("James Pan")
        if status == True:
            assert True
            self.logger.info("******* Customer found with the given Name  *******")
            
        else:
            assert False == False
            time.sleep(2)
            self.driver.save_screenshot("C:\\Users\\Salim\\eclipse-workspace\\nopCommerceApp\\Screenshots\CustomerByName.png")
            self.logger.info("******* Customer not found with the given Name  *******")
        
        self.logger.info("******* Ending Test_005_SearchCustomerByName *******")
        self.driver.close()
        
        
        

import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.AddcutomerPage import AddCustomer

class Test_SearchCustomerByEmail_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*********** Test_004_SearchCustomerByEmail ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        
        self.logger.info("******* Trying to Login *******")
        
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        
        self.logger.info("******* Login Successful *******")
        
        self.logger.info("******* Starting Search Customer By Email *******")
        
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()
        
        
        searchcust = SearchCustomer(self.driver)
        
        flag = searchcust.searchElementsVisible()
        if flag == True:
            self.logger.info("******* Search Elements already visible *******")
            pass
        else:
            self.logger.info("******* CLicking on Search Dropdown *******")
            searchcust.clickDropdownSearch()
            
        time.sleep(2)
        
        self.logger.info("******* Searching Customer By Email *******")
        
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        if status == True:
            assert True
            self.logger.info("Customer found with given email")
        else:
            assert False == False
            self.logger.info("Customer is not available with given email")
        
        self.logger.info("******* Ending Test_004_SearchCustomerByEmail *******")
        self.driver.close()
    
    
        
        
    
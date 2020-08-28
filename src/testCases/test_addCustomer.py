from pageObjects.AddcutomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.conftest import setup
from pageObjects.LoginPage import LoginPage
import random
import string
import time
import pytest

class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*********** Test_003_AddCustomer ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        
        self.logger.info("******* Trying to Login *******")
        
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        
        self.logger.info("******* Login Successful *******")
        self.logger.info("******* Starting Add Customer Test *******")
        
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(1)
        self.addcust.clickOnCustomerMenuItem()
        
        self.addcust.clickOnAddnew()
        self.logger.info("******* Providing Customer info *******")
        
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Salim")
        self.addcust.setLastname("Khan")
        self.addcust.setGender("Male")
        self.addcust.setDOB("01/11/1995")
        self.addcust.setCompanyName("QA Automation")
        self.addcust.setCustomerRole("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing purpose......")
        self.addcust.clickOnSave()
        
        self.logger.info("******* Saving Customer info *******")
        self.logger.info("******* Add Customer Validation started *******")
        
        self.msg = self.driver.find_element_by_tag_name("body").text
        if 'customer has been added successfully' in self.msg:
            assert True
            self.logger.info("******* Add Customer Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            assert False
            self.logger.info("******* Add Customer Test Failed *******")
        
        self.driver.close()
        self.logger.info("******* Ending Test_003_AddCustomer Test *******")
        
    
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
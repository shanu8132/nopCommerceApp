import pytest
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    
    logger = LogGen.loggen()
    
    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("************TEST_001_Login************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.logger.info("Verifying Home Page Title...")
        if act_title == "Your store. Login":
            self.logger.info("Home Page Title Passed.")
            self.driver.close()
            assert True
        
        else:
            self.driver.save_screenshot("C:\\Users\\Salim\\eclipse-workspace\\nopCommerceApp\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.info("Home Page Title Failed.")
            self.driver.close()
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression        
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.logger.info("Verifying Login Test...")
        
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("Login Test Passed.")
            self.driver.close()
            assert True
        
        else:
            self.driver.save_screenshot("C:\\Users\\Salim\\eclipse-workspace\\nopCommerceApp\\Screenshots\\"+"test_login.png")
            self.logger.info("Login Test Failed.")
            self.driver.close()
            assert False
        

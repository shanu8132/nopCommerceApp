import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    
    txtEmail_xpath  = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyname_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    drpManagerOfVender_xpath = "//select[@id='VendorId']"
    txtAdmincontent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"
    
    def __init__(self,driver):
        self.driver = driver
    
    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
    
    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()
    
    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()
    
    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)
    
    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)
    
    def setFirstname(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).send_keys(fname)
    
    def setLastname(self,lname):
        self.driver.find_element_by_xpath(self.txtLastname_xpath).send_keys(lname)
    
    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
    
    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(dob)
    
    def setCompanyName(self,comname):
        self.driver.find_element_by_xpath(self.txtCompanyname_xpath).send_keys(comname)
    
    def setCustomerRole(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        
        elif role == 'Guests':
            # Here user can be Registered or Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[@class='k-button']//span[@class='k-select']").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click(); -- Not working in this scenario, we have to use below statement
        self.driver.execute_script("arguments[0].click();",self.listitem)
        
        
    
    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element_by_xpath(self.drpManagerOfVender_xpath))
        drp.select_by_visible_text(value)
    
    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtAdmincontent_xpath).send_keys(content)
        
    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
    
    
        
            
    
    
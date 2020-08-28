from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Users\\Salim\\Documents\\chromedriver_win32\\chromedriver.exe")
        print("Launching Chrome Browser")
    
    elif browser == 'edge':
        driver = webdriver.Edge("C:\\Users\\Salim\\Documents\\edgedriver_win64\\msedgedriver.exe")
        print("Launching Edge Browser")
    
    else:
        driver = webdriver.Chrome("C:\\Users\\Salim\\Documents\\chromedriver_win32\\chromedriver.exe")
        print("Launching Chrome Browser")
        
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
    
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

################# PyTest HTML Report ###############

#It is hook for Adding Environment info to the HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Salim'

#It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
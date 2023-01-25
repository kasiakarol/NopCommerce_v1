import os
from datetime import datetime
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.........")
    return driver

#hook method, if we don't pass any argument, it will ignore it
def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# to customize environment report
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request):
    request.config._metadata.update(
        {
            'Project Name': 'Nopcommerce',
            'Module Name': 'CustRegistration',
            'Tester': 'Kasia'
         }
    )

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Platform", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"



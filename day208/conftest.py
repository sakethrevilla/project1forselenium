import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()

def setup(browser):
    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
        driver=webdriver.Chrome(service=obj)
    elif browser:
        from selenium.webdriver.edge.service import Service
        obj =Service("C:\driver\msedgedriver.exe")
        driver = webdriver.Edge(service=obj)
    return driver


def pytest_addoption(paser):
    paser.addoption("--browser")

@pytest.fixture()

def browser(request):
    return request.config.getoption("--browser")


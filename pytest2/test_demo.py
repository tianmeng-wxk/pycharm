import pytest
from selenium import webdriver

# def setup_function():
#     print("前置条件setup_function")
#
# def teardown_function():
#     print("后置条件def teardown_function")
#
# def setup_module():
#     print("前置条件setup_module")
#
# def teardown_module():
#     print("后置条件teardown_module")
@pytest.mark.first
def test_01():
    print("hello world")

@pytest.mark.second
def test_02():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")



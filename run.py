from selenium import webdriver

from python_class import lesson_06  #导入函数
from python_class.lesson_05 import driver
from python_class.lesson_06 import login
from test_data import test_data     #导入测试函数
from selenium import  webdriver

driver.implicitly_waite(10)

#调用函数，--1先将函数取出来，  2，传参到函数里
url = test_data.url
user_name = test_data.login_date
password = test_data.password


driver = webdriver.Chrome()
driver.get("http://erp.lemfix.com/login.html/")
driver.maximize_window()
driver.implicitly_wait(10)
login(user_name,password)

import time

import document as document
import js as js
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://erp.lemfix.com/login.html/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()


#driver.excute_script('document.getElementById("btnSubmit").click()')


#切换的iframe页面
#1，通过id来切换
#2 通过元素定位xpath来切换iframe
#3 iframe下标，从0开始， htnl -页面 = 0， 第一个宝宝ifrmae里，htm1  1，第二个宝宝2
p_id = driver.find_elements_by_xpath("/div[text()='零售出库/..']").__getattribute__("id")
f_id=p_id+"-frame"
#1
driver.switch_to_frame(f_id)
driver.find_element_by_id("searchNumber").send_keys("314")

#2
driver.switch_to_frame(driver.find_elements_by_xpath("///iframe[@id='{}']".format(f_id)))
driver.find_element_by_id("searchNumber").send_keys("314")

#3
driver.switch_to_frame(1)
driver.find_element_by_id("searchNumber").send_keys("314")
time.sleep()
##点击搜索按钮

##找到单据编号
num = driver.find_elements_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
if "314" in num:
    print("搜索结果是正确的！")
else:
    print("用例测试不太通过")


#写成函数形式
def login(username,password,driver):
    driver.find_element_by_id("username").send_keys("test123")
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_id("btnSubmit").click()

def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()
login_user = driver.find_elements_by_xpath("//p[text()='测试用例']").text
if login_user =="测试用户":
    print("这个登录的用户是：{}".format(login_user()))
    driver.find_elements_by_xpath("/span[text()='零售出库']").click()
else:
    print("这条测试用例不通过")


def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_user(username,password,driver)
    p_id = driver.find_elements_by_xpath("/div[text()='零售出库/..']").__getattribute__("id")
    f_id = p_id + "-frame"
    # 1
    driver.switch_to_frame(f_id)
    driver.find_element_by_id("searchNumber").send_keys("314")

    ##找到单据编号
    num = driver.find_elements_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    if "314" in num:
        print("搜索结果是正确的！")
    else:
        print("用例测试不太通过")

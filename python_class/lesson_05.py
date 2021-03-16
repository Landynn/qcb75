from selenium import webdriver
import time

driver = webdriver.Chrome()  #选择这个浏览器，初始化，打开一个网址  http://erp.lemfix.com/login.html
driver.get("http://120.78.128.25:8765")   
driver.maximize_window()
driver.get("http://120.78.128.25:8765/Index/reg.html")
time.sleep(3)   #睡眠3秒
driver.back()   #退回上个页面
driver.forward()  #下个页面
driver.refresh()  # 刷新页面
driver.find_element_by_id("phone").send_keys("18368045067")
#driver.find_element_by_name("code").send_keys("wee")
driver.find_element_by_name("agree").click()


driver.quit()  #退出

'''
print("结果是")
def add_fun():
    sum = 0
    num = input("请输入任意整数：")
    num = int(num)
    for i in range(num):
        sum += i
    print(sum)

add_fun()
'''
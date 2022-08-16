from selenium import  webdriver
from selenium.webdriver.common.by import By
#模拟鼠标操作才能进行的情况
from selenium.webdriver import ActionChains
import time
with webdriver.Chrome()as driver:
    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    id = driver.find_element(By.ID, "J-userName")
    id.send_keys("账号")#自己的账号
    ps = driver.find_element(By.ID, "J-password")
    ps.send_keys('密码')#自己的密码
    botton = driver.find_element(By.ID, "J-login")
    botton.click()
    time.sleep(4)
    #切换到滑块的div
    huakuai_div = driver.find_element(By.ID,'modal')
    huakuai = huakuai_div.find_element(By.ID,'nc_1_n1z')
    action = ActionChains(driver)
    # 解决特征识别
    script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
    driver.execute_script(script)
    #长按鼠标
    action.click_and_hold(huakuai)
    # 偏移量（F12中查看）
    action.move_by_offset(100, 0)
    action.perform()
    time.sleep(2)
    action.move_by_offset(300,100)
    time.sleep(2)
    #释放鼠标
    action.release()
    #执行上面的操作
    action.perform()
    time.sleep(4)

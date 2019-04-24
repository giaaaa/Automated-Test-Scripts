from selenium import webdriver

from xixi.settings import executable_path

from time import sleep


driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)  # 隐式等待

driver.get("https://xxx.xxx.com")

ele = driver.find_element_by_id("homepage")

ele.find_element_by_css_selector('.signup').click()
sleep(1)
driver.find_element_by_id('studentSignupLink').click()
sleep(1)
driver.find_element_by_id('signup_email').send_keys('xxx@xxx.us')
driver.find_element_by_id('signup_pwd').send_keys('password')
driver.find_element_by_id('studentSignupBtn').click()
sleep(1)

a = driver.find_element_by_id('studentProfileBtn')
list = a.find_elements_by_css_selector('.disabled')
if list != []:
    pass
else:
    print('Error: The button still be clickabled!')

name = 'null'
driver.find_element_by_id('studentFirstName').send_keys(name)

sleep(1)
list = a.find_elements_by_css_selector('.disabled')
if list == []:
    pass
else:
    print('Error: The button still be disabled!')

driver.find_element_by_id('chkExamAct').click()
score = 31
driver.find_element_by_id('actTotalScore').send_keys(score)
driver.find_element_by_id('studentProfileBtn').click()

driver.quit()










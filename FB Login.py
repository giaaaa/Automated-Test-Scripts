from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from xixi.settings import executable_path

from time import sleep

driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)

driver.get("https://xxx.xxx.com")

ele = driver.find_element_by_id("homepage")

ele.find_element_by_css_selector('a[data-target="#signInModal"]').click()
logIn = driver.find_element_by_id('signInModal').find_element_by_css_selector('div[class="modal-content"]')

sleep(3)
facebook = driver.find_element_by_css_selector('#signInModal div[class="qb-btn fb"]')
facebook.click()
email = driver.find_element_by_id('email')
email.send_keys('email')
pwd = driver.find_element_by_id('pass')
pwd.send_keys('pwd')
driver.find_element_by_id('loginbutton').click()

driver.quit()

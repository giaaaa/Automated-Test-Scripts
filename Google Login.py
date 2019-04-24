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
google = driver.find_element_by_css_selector('#signInModal div[class="qb-btn go"]')
google.click()
input = driver.find_element_by_id('identifierId')
input.send_keys('email')
driver.find_element_by_id('identifierNext').click()
sleep(3)
input = driver.find_element_by_css_selector('input[type="password"]')
input.send_keys('password')
driver.find_element_by_id('passwordNext').click()

driver.quit()

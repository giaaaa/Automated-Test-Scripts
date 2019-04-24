from selenium import webdriver

from xixi.settings import executable_path

from time import sleep

from selenium.common.exceptions import WebDriverException

from selenium.common.exceptions import NoSuchElementException

import psycopg2

driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)  # 隐式等待

driver.get("https://xxx.xxx.com")

ele = driver.find_element_by_id("homepage")

ele.find_element_by_css_selector('a[data-target="#signInModal"]').click()
logIn = driver.find_element_by_id('signInModal').find_element_by_css_selector('div[class="modal-content"]')

logIn_Email = logIn.find_element_by_id("signin_email")

email = 'xxx@xxx.com'
logIn_Email.send_keys(email)
logIn_Password = logIn.find_element_by_id("signin_pwd")

logIn_Password.send_keys('password')

logIn_button = logIn.find_element_by_id("studentSignInBtn")
logIn_button.find_element_by_css_selector('div[class="qb-btn-label"]').click()

sleep(10)
url = driver.current_url

if url != "https://xxx.xxx.com/start/#/tutor/dashboard":
    print(url)
    driver.quit()
else:
    pass

conn = psycopg2.connect(database="xxx", user="xxx", password="xxx",host="xx.xx.xx.xx", port="xxxx")  # 连接数据库
cur = conn.cursor()

id = "select id from users where email= '%s' ;" % email
cur.execute(id)
tutor_id = cur.fetchall()
print(tutor_id)
info_card = "select description,price_info from tutor_profiles where tutor_id='%s' and (description is null or tutor_profiles is null);" % tutor_id[0]
cur.execute(info_card)
info_card = cur.fetchall()

if info_card == []:
    profile = driver.find_element_by_css_selector('.dashboard-type-area-main-A-profile')
    profile.find_element_by_tag_name('button').click()
    bio = driver.find_element_by_tag_name('textarea')
    bio.send_keys('description')
    driver.find_element_by_css_selector('.price-info-input').send_keys('11')
    driver.find_element_by_css_selector('.alternate div').click()    # click save changes button
    driver.find_element_by_css_selector('.box-cursor li:nth-child(1)').click()  # click dashboard button
    try:
        driver.find_element_by_css_selector('.dashboard-type-area-main-A-profile')
    except NoSuchElementException:
        pass
else:
    pass









driver.quit()

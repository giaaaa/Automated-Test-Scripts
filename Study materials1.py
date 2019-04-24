from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from xixi.settings import executable_path

driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)  # 隐式等待

# '''
# ele1 = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(By.ID,'homepage'))
#                             #wait time
# '''

driver.get("https://xxx.xxx.com")

ele = driver.find_element_by_id("homepage")

ele.find_element_by_css_selector('a[data-target="#signInModal"]').click()
logIn = driver.find_element_by_id('signInModal').find_element_by_css_selector('div[class="modal-content"]')

# from settings import login
# for one in login:
#     email = one
#     pwd = login[one]
logIn_Email = logIn.find_element_by_id("signin_email")

logIn_Email.send_keys('xxx@xxx.com')
logIn_Password = logIn.find_element_by_id("signin_pwd")

logIn_Password.send_keys('password')

logIn_button = logIn.find_element_by_id("studentSignInBtn")
logIn_button.find_element_by_css_selector('div[class="qb-btn-label"]').click() #log in succeeded；https://xxx.xxx.com/start/#/getStart

driver.find_element_by_css_selector('div > ul li:nth-child(5)').click()      # click study materials




# 依次输入a-z，检查返回的结果首字母是否与所输入的对应

keywords = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for keyword in keywords:
    input_box = driver.find_element_by_css_selector('input[type]')
    input_box.clear()
    input_box.send_keys(keyword)
    div = driver.find_element_by_id('react-autowhatever-1')
    try:
        results = div.find_elements_by_css_selector('li[role]')
        for result in results:
            print(result.text,result)
            if result.text.startswith(keyword.upper()) is True:
                result.click()
                try:
                    driver.find_element_by_css_selector('div[class="limitText"]').click()  # click the result
                    driver.find_element_by_css_selector('div > ul li:nth-child(5)').click()
                    input_box = driver.find_element_by_css_selector('input[type]')
                    input_box.send_keys(keyword)
                    div = driver.find_element_by_id('react-autowhatever-1')
                    results = div.find_elements_by_css_selector('li[role]')
                except NoSuchElementException:
                    print("The skill has no articles.: %s" % result.text)
            else:
                print("%s does not match the result" % result.text)
    except NoSuchElementException:
        pass




driver.quit()

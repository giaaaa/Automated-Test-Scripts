from selenium import webdriver

from xixi.settings import executable_path

from time import sleep

from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import WebDriverException


driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)  # 隐式等待

driver.get("https://xxx.xxxx.com")

ele = driver.find_element_by_id("homepage")

ele.find_element_by_css_selector('a[data-target="#signInModal"]').click()
logIn = driver.find_element_by_id('signInModal').find_element_by_css_selector('div[class="modal-content"]')

logIn_Email = logIn.find_element_by_id("signin_email")

logIn_Email.send_keys('xxx@xxx.com')
logIn_Password = logIn.find_element_by_id("signin_pwd")

logIn_Password.send_keys('password')

logIn_button = logIn.find_element_by_id("studentSignInBtn")
logIn_button.find_element_by_css_selector('div[class="qb-btn-label"]').click()

driver.find_element_by_tag_name('button').click()    # click the Take the test! button

# English
driver.find_element_by_css_selector('.icon_english').click()   # select English

driver.find_element_by_tag_name('button').click()   # click the Start/Continue/Retake button

number = len(driver.find_elements_by_css_selector('a[class="question-number"]') )   # the number of questions

while len(driver.find_elements_by_css_selector('.answered')) != number:
    driver.find_element_by_css_selector('.correct_answer').click()  # click the correct answer
    try:
        next_ques = driver.find_element_by_css_selector('span[class="content"]')
        next_ques.click()  # click the next question button
    except NoSuchElementException:
        submit = driver.find_element_by_css_selector('.diagnostic_submit')
        submit.click()  # submit
        sleep(1)
        driver.find_element_by_css_selector('.button').click()  # click Start Part 2
        try:
            def ele():
                current = driver.find_element_by_css_selector('.current > div > div >a').text
                v = '#header_questions_wrapper div:nth-child(' + str(int(current) + 11) + ') a[class="question-number"]'
                driver.find_element_by_css_selector(v).click()
                sleep(1)
            ele()
            ele()
            ele()
            ele()
            ele()
            sleep(1)
        except WebDriverException:
            submit = driver.find_element_by_css_selector('.diagnostic_submit')
            submit.click()
            sleep(4)
driver.find_element_by_css_selector('.col-md-2 ul li:nth-child(2)').click()   # click English in study plan page
topics = driver.find_elements_by_css_selector('.section-topics:nth-child(1) div[class="topic-content-title col-10"] strong').text
English = ['Conventions: Usage','Production of Writing','Conventions: Sentence Structure','Conventions: Punctuation','Knowledge of Language']

for one in topics:
    for two in English:
        if one == two:
            pass
        else:
            print(one,two)

driver.quit()

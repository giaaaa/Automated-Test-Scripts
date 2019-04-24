from selenium import webdriver

from xixi.settings import executable_path

from time import sleep

from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import WebDriverException



driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)  # 隐式等待

driver.get("https://xxx.xxx.com")

ele = driver.find_element_by_id("homepage")

ele.find_element_by_css_selector('a[data-target="#signInModal"]').click()
logIn = driver.find_element_by_id('signInModal').find_element_by_css_selector('div[class="modal-content"]')

logIn_Email = logIn.find_element_by_id("signin_email")

logIn_Email.send_keys('xxx@xxx.com')
logIn_Password = logIn.find_element_by_id("signin_pwd")

logIn_Password.send_keys('password')

logIn_button = logIn.find_element_by_id("studentSignInBtn")
logIn_button.find_element_by_css_selector('div[class="qb-btn-label"]').click()

driver.find_element_by_css_selector('div[class="section-ct-link box-cursor"] > ul > li:nth-child(6)').click()   # click practice tests

# # Science
#
# driver.find_element_by_css_selector('li:nth-child(4) button').click()
#
# numbers = len(driver.find_elements_by_css_selector('a[class="question-number"]') )   # the number of questions
#
# for number in range(0,numbers):
#     while len(driver.find_elements_by_css_selector('.answered')) != number:
#         driver.find_element_by_css_selector('.correct_answer').click()  # click the correct answer
#         next_ques = driver.find_element_by_css_selector('span[class="content"]')
#         next_ques.click()  # click the next question button
#         sleep(1)
#     driver.find_element_by_css_selector('#header_questions_wrapper div:nth-child(13)').click()
#     sleep(1)
#     driver.find_element_by_css_selector('#header_questions_wrapper div:nth-child(24)').click()
#     sleep(1)
#     driver.find_element_by_css_selector('#header_questions_wrapper div:nth-child(35)').click()
#     sleep(1)
#     submit = driver.find_element_by_css_selector('.diagnostic_submit')
#     submit.click()  # submit
#     sleep(1)
#     score = driver.find_element_by_css_selector('li:nth-child(4) div[class="practice-tests-card-subject-title"] > span > span').text
#     print('Science: The number of correct answers is %d；%s' % (number, score))
#     driver.find_element_by_css_selector('li:nth-child(4) button').click()
# driver.find_element_by_css_selector('.close_button').click()




driver.find_element_by_css_selector('li:nth-child(4) button').click()

numbers = len(driver.find_elements_by_css_selector('a[class="question-number"]') )   # the number of questions

actual = {}

expected = {
    0:'1',1:'3',2:'4',3:'6',4:'7',5:'8',6:'9',7:'10',8:'11',9:'12',10:'13',11:'14',12:'15',13:'16',14:'17',15:'17',16:'18',17:'19',
    18:'19',19:'20',20:'20',21:'21',22:'21',23:'22',24:'23',25:'23',26:'24',27:'24',28:'25',29:'25',30:'26',31:'27',32:'27',33:'28',
    34:'29',35:'30',36:'31',37:'33',38:'34',39:'35',40:'36'
}

for number in range(numbers,-1,-1):
    while len(driver.find_elements_by_css_selector('.answered')) != number:
        driver.find_element_by_css_selector('.correct_answer').click()  # click the correct answer
        try:
            next_ques = driver.find_element_by_css_selector('span[class="content"]')
            next_ques.click()  # click the next question button
        except NoSuchElementException:
            pass
        sleep(1)
    try:
        def ele():
            current = driver.find_element_by_css_selector('.current > div > div >a').text
            v = '#header_questions_wrapper div:nth-child(' + str(int(current)+11) +') a[class="question-number"]'
            driver.find_element_by_css_selector(v).click()
            sleep(1)
        ele()
        ele()
        ele()
        sleep(1)
    except WebDriverException:
        submit = driver.find_element_by_css_selector('.diagnostic_submit')
        submit.click()  # submit
        sleep(1)
    score = driver.find_element_by_css_selector('li:nth-child(4) div[class="practice-tests-card-subject-title"] > span > span').text
    actual[number] = score
    print('Science: The number of correct answers is %d；%s' % (number, score))
    driver.find_element_by_css_selector('li:nth-child(4) button').click()
driver.find_element_by_css_selector('.close_button').click()

for a in expected:
    for b in actual:
        if a == b:
            if  expected[a] != actual[b]:
                print('Science: The number of correct answers: %d does not match to the score: %s' % (a,b))
            else:
                continue

driver.quit()

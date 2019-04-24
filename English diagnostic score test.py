from selenium import webdriver

from xixi.settings import executable_path

from time import sleep

from selenium.common.exceptions import WebDriverException

from selenium.common.exceptions import NoSuchElementException

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

driver.find_element_by_tag_name('button').click()    # click the Take the test! button

# English

driver.find_element_by_css_selector('.icon_english').click()   # select English

driver.find_element_by_tag_name('button').click()   # click the Start/Continue/Retake button

numbers = len(driver.find_elements_by_css_selector('a[class="question-number"]') )   # the number of questions

actual = {}

expected = {
    0:'1/36',1:'1/36',2:'2/36',3:'4/36',4:'5/36',5:'6/36',6:'6/36',7:'7/36',8:'8/36',9:'8/36',10:'9/36',11:'10/36',12:'11/36',
    13:'12/36',14:'14/36',15:'14/36',16:'15/36',17:'16/36',18:'17/36',19:'18/36',20:'19/36',21:'20/36',22:'20/36',23:'21/36',
    24:'22/36',25:'23/36',26:'24/36',27:'25/36',28:'26/36',29:'27/36',30:'28/36',31:'29/36',32:'32/36',33:'34/36',34:'35/36',
    35:'36/36'
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
        driver.find_element_by_css_selector('.button').click()    # click Start Part 2
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
    driver.find_element_by_css_selector('.box-cursor>ul>li:nth-child(1)').click()   # enter to getting started page
    driver.find_element_by_tag_name('button').click()  # click the Take the test! button
    driver.find_element_by_css_selector('.icon_english').click()
    score = driver.find_element_by_css_selector('.part-text>span:nth-child(2)').text
    actual[number] = score
    print('English: The number of correct answers is %d；The score is %s.' % (number, score))
    driver.find_element_by_tag_name('button').click()    # click the Start/Continue/Retake button
driver.find_element_by_css_selector('.close_button').click()

for a in expected:
    for b in actual:
        if a == b:
            if  expected[a] != actual[b]:
                print('Science: The number of correct answers: %d does not match to the score: %s' % (a,b))
            else:
                continue

driver.quit()

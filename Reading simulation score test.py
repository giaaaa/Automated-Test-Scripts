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

driver.find_element_by_css_selector('div[class="section-ct-link box-cursor"] > ul > li:nth-child(6)').click()   # click practice tests

# Reading

driver.find_element_by_css_selector('li:nth-child(2) button').click()

numbers = len(driver.find_elements_by_css_selector('a[class="question-number"]') )   # the number of questions

actual = {}

expected = {
    0:'1',1:'2',2:'3',3:'5',4:'6',5:'7',6:'8',7:'9',8:'10',9:'11',10:'11',11:'12',12:'12',13:'13',14:'14',15:'14',16:'15',17:'15',
    18:'16',19:'17',20:'18',21:'18',22:'19',23:'20',24:'20',25:'21',26:'22',27:'23',28:'23',29:'24',30:'25',31:'26',32:'27',33:'28',
    34:'29',35:'30',36:'31',37:'32',38:'34',39:'35',40:'36'
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
    score = driver.find_element_by_css_selector('li:nth-child(2) div[class="practice-tests-card-subject-title"] > span > span').text
    actual[number] = score
    print('Reading: The number of correct answers is %d；%s' % (number, score))
    driver.find_element_by_css_selector('li:nth-child(2) button').click()
driver.find_element_by_css_selector('.close_button').click()

for a in expected:
    for b in actual:
        if a == b:
            if  expected[a] != actual[b]:
                print('Science: The number of correct answers: %d does not match to the score: %s' % (a,b))
            else:
                continue

driver.quit()

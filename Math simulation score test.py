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

# Math

driver.find_element_by_css_selector('li:nth-child(3) button').click()

numbers = len(driver.find_elements_by_css_selector('a[class="question-number"]') )   # the number of questions
actual = {}

expected = {
    0:'1',1:'3',2:'5',3:'7',4:'9',5:'10',6:'11',7:'11',8:'12',9:'12',10:'13',11:'13',12:'14',13:'14',14:'14',15:'15',16:'15',
    17:'15',18:'15',19:'16',20:'16',21:'16',22:'16',23:'16',24:'17',25:'17',26:'17',27:'18',28:'18',29:'19',30:'19',31:'20',
    32:'20',33:'21',34:'22',35:'22',36:'23',37:'23',38:'24',39:'24',40:'24',41:'25',42:'25',43:'26',44:'26',45:'27',46:'27',
    47:'28',48:'28',49:'29',50:'30',51:'30',52:'31',53:'32',54:'33',55:'34',56:'34',57:'35',58:'35',59:'36',60:'36'
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
        ele()
        ele()
        sleep(1)
    except WebDriverException:
        submit = driver.find_element_by_css_selector('.diagnostic_submit')
        submit.click()  # submit
        sleep(1)
    score = driver.find_element_by_css_selector('li:nth-child(3) div[class="practice-tests-card-subject-title"] > span > span').text
    actual[number] = score
    print('Math: The number of correct answers is %d；%s' % (number, score))
    driver.find_element_by_css_selector('li:nth-child(3) button').click()
driver.find_element_by_css_selector('.close_button').click()

for a in expected:
    for b in actual:
        if a == b:
            if  expected[a] != actual[b]:
                print('Science: The number of correct answers: %d does not match to the score: %s' % (a,b))
            else:
                continue

driver.quit()

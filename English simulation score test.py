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

#  English

driver.find_element_by_css_selector('li:nth-child(1) button').click()

numbers = len(driver.find_elements_by_css_selector('a[class="question-number"]') )   # the number of questions
# for number in range(0,numbers):
#     if len(driver.find_elements_by_css_selector('.answered')) == number:   # the number of answered questions
#         element()
#         continue
#     else:
#         driver.find_element_by_css_selector('.correct_answer').click()  # click the correct answer
#         for number in range(0,numbers):
#             next_ques = driver.find_element_by_css_selector('span[class="content"]')
#             next_ques.click()  # click the next question button
#             element()
actual = {}

expected = {
    0:'1',1:'1',2:'1',3:'2',4:'2',5:'3',6:'4',7:'4',8:'4',9:'5',10:'5',11:'6',12:'6',13:'6',14:'7',15:'7',16:'7',17:'8',18:'8',
    19:'8',20:'9',21:'9',22:'9',23:'10',24:'10',25:'11',26:'11',27:'12',28:'12',29:'13',30:'14',31:'14',32:'14',33:'15',34:'15',
    35:'16',36:'16',37:'16',38:'17',39:'17',40:'18',41:'18',42:'19',43:'19',44:'19',45:'20',46:'20',47:'20',48:'21',49:'21',50:'21',
    51:'22',52:'22',53:'23',54:'23',55:'23',56:'24',57:'24',58:'25',59:'26',60:'26',61:'26',62:'27',63:'27',64:'28',65:'28',66:'29',
    67:'30',68:'31',69:'32',70:'33',71:'34',72:'34',73:'35',74:'35',75:'36'
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
        ele()
        ele()
        sleep(1)
    except WebDriverException:
        submit = driver.find_element_by_css_selector('.diagnostic_submit')
        submit.click()  # submit
        sleep(1)
    score = driver.find_element_by_css_selector('li:nth-child(1) div[class="practice-tests-card-subject-title"] > span > span').text
    actual[number] = score
    print('English: The number of correct answers is %d；%s' % (number, score))
    driver.find_element_by_css_selector('li:nth-child(1) button').click()
driver.find_element_by_css_selector('.close_button').click()

for a in expected:
    for b in actual:
        if a == b:
            if  expected[a] != actual[b]:
                print('Science: The number of correct answers: %d does not match to the score: %s' % (a,b))
            else:
                continue

driver.quit()

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

sleep(1)
driver.find_element_by_tag_name('button').click()    # click the Take the test! button

# Science

driver.find_element_by_css_selector('.icon_science').click()   # select science

driver.find_element_by_tag_name('button').click()   # click the Start/Continue/Retake button

numbers = len(driver.find_elements_by_css_selector('a[class="question-number"]') )   # the number of questions

actual = {}

expected = {
    0:'1/36',1:'4/36',2:'7/36',3:'9/36',4:'11/36',5:'13/36',6:'15/36',7:'17/36',8:'18/36',9:'19/36',10:'20/36',11:'21/36',
    12:'23/36',13:'24/36',14:'25/36',15:'26/36',16:'27/36',17:'29/36',18:'31/36',19:'34/36',20:'36/36'
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
        sleep(1)
    except WebDriverException:
        submit = driver.find_element_by_css_selector('.diagnostic_submit')
        submit.click()  # submit
        sleep(1)
    driver.find_element_by_css_selector('.box-cursor>ul>li:nth-child(1)').click()   # enter to getting started page
    driver.find_element_by_tag_name('button').click()  # click the Take the test! button
    driver.find_element_by_css_selector('.icon_science').click()
    score = driver.find_element_by_css_selector('.part-text>span:nth-child(2)').text
    actual[number] = score
    print('Science: The number of correct answers is %d；The score is %s.' % (number, score))
    driver.find_element_by_tag_name('button').click()    # click the Start/Continue/Retake button
driver.find_element_by_css_selector('.close_button').click()

# expected = {'The number of correct answers':0, 'Score':'1/36',
#             'The number of correct answers':1, 'Score':'4/36',
#             'The number of correct answers':2, 'Score':'7/36',
#             'The number of correct answers':3, 'Score':'9/36',
#             'The number of correct answers':4, 'Score':'11/36',
#             'The number of correct answers':5, 'Score':'13/36',
#             'The number of correct answers':6, 'Score':'15/36',
#             'The number of correct answers':7, 'Score':'17/36',
#             'The number of correct answers':8, 'Score':'18/36',
#             'The number of correct answers':9, 'Score':'19/36',
#             'The number of correct answers':10, 'Score':'20/36',
#             'The number of correct answers':11, 'Score':'21/36',
#             'The number of correct answers':12, 'Score':'23/36',
#             'The number of correct answers':13, 'Score':'24/36',
#             'The number of correct answers':14, 'Score':'25/36',
#             'The number of correct answers':15, 'Score':'26/36',
#             'The number of correct answers':16, 'Score':'27/36',
#             'The number of correct answers':17, 'Score':'29/36',
#             'The number of correct answers':18, 'Score':'31/36',
#             'The number of correct answers':19, 'Score':'34/36',
#             'The number of correct answers':20, 'Score':'36/36'
#             }


for a in expected:
    for b in actual:
        if a == b:
            if  expected[a] != actual[b]:
                print('Science: The number of correct answers: %d does not match to the score: %s' % (a,b))
            else:
                continue


driver.quit()

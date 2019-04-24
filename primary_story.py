from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from xixi.settings import executable_path

from time import sleep

from selenium.webdriver.support.ui import WebDriverWait   # 显式等待

from  selenium.webdriver.support import expected_conditions as EC  #显式等待

from selenium.webdriver.common.by import By



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
logIn_button.find_element_by_css_selector('div[class="qb-btn-label"]').click() #log in succeeded；https://www.xxx.com/start/#/getStart


driver.find_element_by_id('root').find_element_by_tag_name('button').click() #click "take the test!" https://www.xxx.com/start/#/diagnostic

eng_dia = driver.find_element_by_css_selector('a[href="#/diagnostic/test/science"]')
eng_dia.find_element_by_css_selector('div[class="circle_label"]').click() #https://www.xxx.com/start/#/diagnostic/test/english

driver.find_element_by_tag_name('button').click() #diagnostic part1


section = ''
answer = ''
submit = ''
next_ques = ''
def test():
    global section, answer, submit, next_ques
    section = driver.find_element_by_css_selector('div[class="passage_section_wrapper"]') #只有diagnostic页面才有的元素
    answer = driver.find_element_by_css_selector('a[class="answer_item"]')  # 答案A
    submit = driver.find_element_by_tag_name('i')  # 提交按钮
    next_ques = driver.find_element_by_css_selector('span[class="content"]')  #error


try:
    test()
    while section.is_displayed() == True:
        answer.click()  # 选择答案A
        next_ques.click()
        sleep(4)
        test()
except NoSuchElementException:
    answer.click()
    submit.click()


try:
    part2 = driver.find_element_by_tag_name('main').find_element_by_css_selector('a[class="btn button"]')
    if part2.is_displayed() == True:
        part2.click()
        try:
            test()
            while section.is_displayed() == True:
                answer.click()
                next_ques.click()
                sleep(4)
                test()
        except NoSuchElementException:
            answer.click()
            submit.click()
    else:
        pass
except NoSuchElementException:
    pass

# study plan
sleep(4)
find_eclass = driver.find_element_by_css_selector('ul button div')
find_eclass.click()

# eclass
num = driver.find_element_by_tag_name('h3').text.split(' ')
schedule = driver.find_element_by_id('root')
if int(num[0]) != 0:
    schedule.find_element_by_css_selector('img[alt="avatar"]').click()
    sleep(4)
    driver.find_element_by_css_selector('div[class="section-ct-link box-cursor"] > ul > li:nth-child(2)').click() # study plan
else:
    driver.find_element_by_css_selector('div[class="section-ct-link box-cursor"] > ul > li:nth-child(2)').click() # study plan

# practice by skill
sleep(5)
practice_ques = driver.find_element_by_css_selector('ul > li  div:nth-child(3) :nth-child(2)')
practice_ques.click()


answer1 = ''
submit1 = ''
next_ques1 = ''
def test1():
    global answer1, submit1, next_ques1
    answer1 = driver.find_element_by_css_selector('div[class="answer_item"]')
    submit1 = driver.find_element_by_css_selector('i[class="fa fa-check"]')
    next_ques1 = driver.find_element_by_css_selector('div[class="button next_question disabled submit"]')


try:
    test1()
    while next_ques1.is_displayed() == True:
        answer1.click()  # 选择答案A
        next_ques1.click()
        sleep(4)
        test1()
except NoSuchElementException:
    pass

driver.find_element_by_css_selector('header > div > a').click() # close; lead to practice questions

sleep(5)
driver.find_element_by_css_selector('div[class="section-ct-link box-cursor"] > ul > li:nth-child(6)').click()


# simulation
sleep(5)
driver.find_element_by_css_selector('button[type="button"]').click()
try:
    test()
    while section.is_displayed() == True:
        answer.click()  # 选择答案A
        next_ques.click()
        sleep(4)
        test()
except NoSuchElementException:
    answer.click()
    submit.click()


driver.quit()

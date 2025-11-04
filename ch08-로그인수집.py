from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import platform
import pyperclip
from selenium.webdriver import Keys, ActionChains

#. [복사/붙여넣기 함수] 자동 입력 방지 모듈을 우회하기 위해 사람이 복사/붙여넣기 하는 것처럼 동작하기 위한 목적
def copy_and_paste(browser, byType, css, user_input):
    pyperclip.copy(user_input) #. 복사하기
    browser.find_element(byType, css).click() #. 대상 입력상자 포커스
    os_type = platform.system()
    if os_type == "Windows":
        paste_key = Keys.CONTROL
    else:
        paste_key = Keys.COMMAND
    ActionChains(browser).key_down(paste_key).key_down("V").perform() #. 붙여넣기

try:
    input_id=input("로그인 아이디 >> ")
    input_pwd=input("비밀번호 입력 >> ")

    #. 브라우저 생성 (자동 닫힘 해제)
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=opt)

    #. 로그인
    browser.get("https://www.tsherpa.co.kr/mo_membership/login.html?returnUrl=https%3A%2F%2Fsupport.aitextbook.co.kr%2F")
    #id = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/ul/li[1]/input")
    #id.send_keys(input_id)
    copy_and_paste(browser, By.XPATH, "/html/body/div/div[2]/div/div[2]/ul/li[1]/input", input_id)
    time.sleep(1) #. 사람이 복사/붙여넣기 하는 것처럼 가장
    #pwd = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/ul/li[2]/input")
    #pwd.send_keys(input_pwd)
    copy_and_paste(browser, By.XPATH, "/html/body/div/div[2]/div/div[2]/ul/li[2]/input", input_pwd)
    time.sleep(1) #. 사람이 복사/붙여넣기 하는 것처럼 가장
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/a")
    login_button.click()
    time.sleep(2)

except Exception as e:
    print(f'An error occured: {e}')
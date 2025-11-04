from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    input_id=input("로그인 아이디 >> ")
    input_pwd=input("비밀번호 입력 >> ")

    #. 브라우저 생성 (자동 닫힘 해제)
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=opt)

    #. 로그인
    browser.get("https://www.tsherpa.co.kr/mo_membership/login.html?returnUrl=https%3A%2F%2Fsupport.aitextbook.co.kr%2F")
    id = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/ul/li[1]/input")
    id.send_keys(input_id)
    pwd = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/ul/li[2]/input")
    pwd.send_keys(input_pwd)
    login_button = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/a")
    login_button.click()
    time.sleep(2)

except Exception as e:
    print(f'An error occured: {e}')
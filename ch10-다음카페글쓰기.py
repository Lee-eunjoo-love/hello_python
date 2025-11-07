from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#. 브라우저 자동 닫힘 해제
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(options=options)

#. 암시적 대기시간
browser.implicitly_wait(10)

try:
    browser.get("https://accounts.kakao.com/login/?continue=https%3A%2F%2Fcafe.daum.net%2F_c21_%2Fhome%3Fgrpid%3D1Y7AF#login")
    
    login_button_elements = browser.find_elements(By.CSS_SELECTOR, "div.confirm_btn > button.btn_g")    
    for q in login_button_elements:
        if q.text == 'QR코드 로그인':
            confirm_qr_login = input("QR코드 로그인을 하시겠습니까? (Y/N)")
            if confirm_qr_login == "Y":
                qr_login = q
                break
        
    if qr_login is None:
        input_id = input("아이디 >>> ")
        input_password = input("비밀번호 >>> ")
        
        #. 로그인
        id = browser.find_element(By.NAME, "input#loginId")
        id.send_keys(input_id)
        password = browser.find_element(By.NAME, "input#password")
        password.send_keys(input_password)
        button = browser.find_element(By.CSS_SELECTOR, "div.confirm_btn > button.btn_g.highlight.submit")
        button.click()
        time.sleep(3)
    else:
        qr_login.click()
        time.sleep(10)

    
    #. 카페 접속
    browser.get("https://cafe.daum.net/talingpython")
    time.sleep(3)
    
    #. [프레임 전환] ifrme#down 요소로 들어가기
    browser.switch_to.frame(browser.find_element(By.CSS_SELECTOR, '#down'))

    #. 가입 인사 게시판 클릭
    browser.find_element(By.CSS_SELECTOR, '#fldlink_lF1R_309').click()
    time.sleep(2)
    
    #. 첫 게시물 클릭
    browser.find_element(By.CSS_SELECTOR, "a.txt_item").click()
    time.sleep(1)
    
    #. 댓글 달기
    browser.find_element(By.CSS_SELECTOR, "div.box_textarea > textarea").send_keys("안녕하세요. 반갑습니다 :)")
    time.sleep(1)
    
    #. 등록 버튼 클릭
    browser.find_element(By.CSS_SELECTOR, "div.btn_group > button.btn_g.full_type1.confirm_button").click()
    
    #. 다시 뒤로가기
    browser.back()
    time.sleep(1)
    
    #. [프레임 전환] 뒤로가기로 빠져나온 iframe#down 요소로 다시 들어가기
    browser.switch_to.frame("down")
    
    #. 카페 글쓰기 버튼 클릭
    browser.find_element(By.CSS_SELECTOR, "a#cafe_write_article_btn").click()
    time.sleep(2)
    
    #. 제목 작성
    browser.find_element(By.CSS_SELECTOR, "input.title__input").send_keys("안녕하세요. 가입 인사 드립니다!!")
    
    #. [프레임 전환] iframe#keditorContainer_ifr(에디터) 요소로 들어가기
    browser.switch_to.frame("keditorContainer_ifr")
    
    #. 본문 작성
    browser.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("파이썬 공부하러 왔습니다. 잘 부탁드립니다!!")
    
    #. [프레임 전환] iframe#down 요소로 나가기 (나가기는 최상위 프레임으로 전환한 다음 프레임 전환)
    browser.switch_to.default_content()
    browser.switch_to.frame("down")
    
    #. 등록 버튼 클릭
    browser.find_element(By.CSS_SELECTOR, "button.btn_g.full_type1").click()
    time.sleep(2)    
    
except Exception as e:
    print(f'An error occured: {e}')    
    
browser.close()

#. [no such element] 오류 발생시
#. 1. CSS 선택자를 올바로 작성했는지 확인하기
#. 2. time.sleep() 문을 더 길게 조정하여 지연시간 늘리기
#. 3. 해당 요소가 프레임 안에 있는지 확인하기 (프레임 내부에 있으면 프레임 전환 코드 추가)

#. 프레임 전환 : 
#   외부 -> 내부 : (기본)내부에 포함된 프레임으로 전환 가능.
#.  내부 -> 외부 : (예외)외부에 포함된 프레임으로 전환 불가. (전환하려면 최상위 프레임으로 이동 후 하위 요소의 프레임으로 전환 가능)
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = "https://www.instagram.com/?flo=true"

#. 브라우저 자동닫힘 해제
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

try:
    input_id = input("전화번호, 사용자 이름 또는 이메일 >>> ")
    input_password = input("비밀번호 >>> ")
    input_keyword = input("해시태그 입력 >>> ")
    browser = webdriver.Chrome(options=options)
    #. 암시적 대기시간 10초
    browser.implicitly_wait(10)
        
    browser.get(url)
    time.sleep(3)
    
    #. 자동 로그인
    id = browser.find_element(By.NAME, "username")
    id.send_keys(input_id)
    password = browser.find_element(By.NAME, "password")
    password.send_keys(input_password)
    button = browser.find_element(By.CSS_SELECTOR, "form#loginForm > div > div:nth-child(3) > button")
    button.click()
    time.sleep(20)
    
    browser.get(f"https://www.instagram.com/explore/search/keyword/?q=%23{input_keyword}")
    time.sleep(6)
    
    first_element = browser.find_element(By.CSS_SELECTOR, "div._aagu")
    first_element.click()
    time.sleep(5)
    
    while True:
        #. 좋아요 선택(.xyb1xck)/미선택(.xxk16z8)
        like_elements = browser.find_elements(By.CSS_SELECTOR, "svg[aria-label='좋아요'].x1lliihq.x1n2onr6.xyb1xck")
        next_element = browser.find_element(By.CSS_SELECTOR, "div._aaqg._aaqh > button._abl- svg")              
        
        #. 좋아요 선택 전이면 ('좋아요') 선택 다음 게시물로 이동하고, 이미 선택된 상태('좋아요 취소')이면 다음 게시물로 이동.
        if like_elements and like_elements[0].get_attribute("aria-label") == "좋아요":            
            #. 인스타그램 사이트에서 click 이벤트 차단하여 execute_script() 명령으로 대체 #. like_element.click()
            browser.execute_script("document.querySelector('svg[aria-label=\"좋아요\"]').dispatchEvent(new MouseEvent('click', {bubbles: true}));")
            #. 인스타그램 매크로 정책에 따른 자동화 프로그램 설정을 위해 약 2분마다 좋아요를 누르도록 2초 -> 65초(좋아요 65 초 * 다음 65 초 = 약 2분)로 대기시간 변경
            time.sleep(65)

        #. 다음 게시물로 이동        
        next_element.click()
        #. 인스타그램 매크로 정책에 따른 자동화 프로그램 설정을 위해 약 2분마다 좋아요를 누르도록 2초 -> 65초로 대기시간 변경
        time.sleep(65)        
    
except Exception as e:
    print(f'An error occured: {e}')
    
#. 인스타그램 매크로 정책
# [좋아요]: 하루 최대 1000 번 제한 (안정적 횟수 하루 최대 700 번)
# [댓글]: 하루 최대 200 개 제한 (안정적 개수 하루 최대 150 개)
# [팔로우]: 하루 최대 200 번 제한 (안정적 횟수 시간당 최대 10 번)
# [DM]: 하루 최대 80 개 제한 (안정적 개수 최대 50 개)
    
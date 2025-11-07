from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

#. 브라우저 자동 닫힘 해제
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(options=options)

try:
    #. 중고나라 카페 접속
    browser.get('https://cafe.daum.net/talingpython/rRa6')
    time.sleep(1)
        
    item_of_interest = "청소기"#. input("관심 물건 >>> ")
    
    #. 10초마다 새로고침 후 게시글 제목 수집
    while True:
        try:
            #. 이전 크롤링 제목 데이터 로드
            with open('./중고나라.txt', "r", encoding="utf-8") as f:
                crawled_title = f.read().split("\n")
        except Exception as e:
            crawled_title = ""
            
        #. [프레임 전환] iframe#down 프레임으로 들어가기 (새로고침하므로 새로고침 후 매번 프레임전환)
        browser.switch_to.frame("down")
        
        title_elements = browser.find_elements(By.CSS_SELECTOR, "a.txt_item")
        
        number_of_item_of_interest = 0
        for title in title_elements:
            #. 새 게시글이 기존 게시글 목록에 존재하지 않는 신규 게시글이면 (새 게시글 등록 알림)/(새 게시글 관심물건이면 새 게시글을 포함한 관심물건 개수 알림)
            if (title.text not in crawled_title):
                print(f'[알림] 새로운 글이 올라왔어요. - {title.text}')
                with open('./중고나라.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{title.text}\n')
                    #. 새 게시글 제목에 관심 물건 명칭이 포함된 경우 관심 물건 개수 카운트
                    if item_of_interest.strip() != '' and item_of_interest.strip() in title.text:
                        number_of_item_of_interest += 1
            
        if number_of_item_of_interest >= 1:
            print(f'[알림] {item_of_interest} 관련 글이 {number_of_item_of_interest} 건 등록되었습니다.')
            
        browser.refresh()
        time.sleep(10)
    
except Exception as e:
    print(f'An error occured: {e}')
    
browser.close()
from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

try:
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    
    browser = webdriver.Chrome(options=opt)    
    browser.get("https://www.youtube.com/watch?v=_-ugbwhhApI")    
    time.sleep(3)
    
    #. 이전 스크롤 위치와 현지 스크롤 위치가 같으면 마지막까지 스크롤한 것으로 판단하고 반복문을 벗어남
    prev_height = 0
    same_scroll_location_cnt = 0
    while True:
        ActionChains(browser).key_down(Keys.PAGE_DOWN).perform()
        #. time.sleep(5) #. [속도개선] 불필요한 5초대기문을 제거하고 같은 스크롤 위치값의 반복횟수로 판단 목적 주석
        cur_height = browser.execute_script("return document.documentElement.scrollTop")
        if (prev_height == cur_height):
            same_scroll_location_cnt += 1
        else:
            same_scroll_location_cnt = 0
        #. [속도개선] 같은 스크롤 위치값이 200번 반복되면 페이지의 마지막으로 판단하고 반복문을 벗어남
        if (same_scroll_location_cnt == 200):
            break
        
        prev_height = cur_height  
        
    comment_elements = browser.find_elements(By.CSS_SELECTOR, "#content-text")
    for idx, c in enumerate(comment_elements):
        print(f'{idx}. {c.text}')
        
except Exception as e:
    print(f'An error occured: {e}')
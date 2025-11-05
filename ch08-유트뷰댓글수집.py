from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys

try:
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    
    browser = webdriver.Chrome(options=opt)    
    browser.get("https://www.youtube.com/watch?v=_-ugbwhhApI")    
    time.sleep(3)
    
    #. 이전 스크롤 위치와 현지 스크롤 위치가 같으면 마지막까지 스크롤한 것으로 판단하고 반복문을 벗어남
    prev_height = 0
    while True:
        ActionChains(browser).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(5)
        cur_height = browser.execute_script("return document.documentElement.scrollTop")
        if (prev_height == cur_height):
            break
        prev_height = cur_height  
        
    print(prev_height)
        
except Exception as e:
    print(f'An error occured: {e}')
import requests
from bs4 import BeautifulSoup
from selenium import webdriver #. 동적 웹크롤링
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

url = "https://naver.com"

try:
    #response = requests.get(url, headers=headers)
    #response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    #. BeautifulSoup 으로 HTML 파싱
    #soup = BeautifulSoup(response.text, 'html.parser')    
    
    #menu_elements = soup.select('div#topSearchWrap')
    #print(menu_elements)
    
    #for m in menu_elements:
    #    print(m)
    
    #. 데이터 초기화
    menu_list = []
    
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)    
    
    menu_elements = driver.find_elements(By.CLASS_NAME, 'service_name')
    
    for m in menu_elements:
        menu_list.append(m.text)
        
    print(menu_list)
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
    
except Exception as e:
    print(f'An error occured: {e}')
    
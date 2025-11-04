from selenium import webdriver
from selenium.webdriver.common.by import By
import time

keyword = input("상품 입력 >> ")
url = f"https://www.lotteimall.com/search/searchMain.lotte?slog=00101_1&headerQuery={keyword}"

try:
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=opt)
    browser.get(url)
    time.sleep(3)
    
    title_elements = browser.find_elements(By.CSS_SELECTOR, "p.title > a")
    percent_elements = browser.find_elements(By.CSS_SELECTOR, "p.price > strong.percent")
    final_elements = browser.find_elements(By.CSS_SELECTOR, "p.price > strong.final")
    origin_elements = browser.find_elements(By.CSS_SELECTOR, "p.price > span.origin")
    
    num = 1
    for title, percent, final, origin in zip(title_elements, percent_elements, final_elements, origin_elements):
        print(f'{num}. {title.text}')
        print(f'   할인율: {percent.text}, 할인가: {final.text} (정상가: {origin.text})')
        num += 1
        
except Exception as e:
    print(f'An error occured: {e}')    
##------------// requests 와 BeautifulSoup 로 크롤링이 어려움 -> selenium 모듈 사용
#import requests
#from bs4 import BeautifulSoup

##. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
#headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

#keyword = input("상품 입력 >> ")
#url = f"https://www.lotteimall.com/search/searchMain.lotte?slog=00101_1&headerQuery={keyword}"

#try:
#    response = requests.get(url, headers=headers)
#    response.raise_for_status() #. HTTP 요청 에러 발생시 예외 발생
    
#    soup = BeautifulSoup(response.text, 'html.parser')
#    print(response.text)
#    title_elements = soup.select("div.wrap_unitlist")
#    print(title_elements)
#    for t in title_elements:
#        print(t)
    
#except requests.exceptions.RequestException as e:
#    print(f'Error during requests to {url}: {e}')
#except Exception as e:
#    print(f'An error occured: {e}')    

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

keyword = input("키워드 입력 >> ")

#. 브라우저 자동 닫힘 해제
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

try:
    #. 브라우저 생성
    browser = webdriver.Chrome(options=opt)
    
    blog_url_list = []
    title_list = []
    content_list = []
    
    #. 1 ~ 5 페이지까지 조회
    for page_num in range(1, 2):
        browser.get(f"https://section.blog.naver.com/Search/Post.naver?pageNo={page_num}&rangeType=ALL&orderBy=sim&keyword={keyword}")
        time.sleep(2)
        link_elements = browser.find_elements(By.CSS_SELECTOR, "a.desc_inner")
        
        for l in link_elements:
            blog_url_list.append(l.get_attribute("href"))
            
    for blog_url in blog_url_list:
        #. 블로그 페이지 구성이 각각 다른데 모바일은 동일하므로 모바일 페이지로 접속하여 각 블로그 크롤링
        blog_url_for_mobile = blog_url.replace("https://blog.naver", "https://m.blog.naver")
        browser.get(blog_url_for_mobile)
        time.sleep(2)
        title_element = browser.find_element(By.CSS_SELECTOR, 'div.se-component-content span')        
        content_element = browser.find_element(By.CSS_SELECTOR, 'div.se-main-container')
        title_list.append(title_element.text)
        content_list.append(content_element.text)

    browser.close()
                
    for title, content in zip(title_list, content_list):
        print('--------------------------------------------------------------')
        print(f'제목: {title}')
        print('--------------------------------------------------------------')
        print(content.replace("\n", " ").strip())        
        
except Exception as e:
    print(f'An error occured: {e}')

#import requests
#from bs4 import BeautifulSoup
#
##. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
#headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}
#
#keyword = input("검색어 입력 >> ")
#url = "https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={keyword}"
#
#try:
#    response = requests.get(url, headers=headers)
#    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
#    
#    soup = BeautifulSoup(response.text, 'html.parser')
#    
#    section_elements = soup.select("strong.title_post")
#    for s in section_elements:
#        print(s.text)
#    
#except requests.exceptions.RequestException as e:
#    print(f'Error during requests to {url}: {e}')
#    
#except Exception as e:
#    print(f'An error occured: {e}')
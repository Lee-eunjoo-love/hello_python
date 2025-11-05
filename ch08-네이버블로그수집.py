import requests
from bs4 import BeautifulSoup

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

keyword = input("검색어 입력 >> ")
url = "https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={keyword}"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    section_elements = soup.select("strong.title_post")
    for s in section_elements:
        print(s.text)
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
    
except Exception as e:
    print(f'An error occured: {e}')
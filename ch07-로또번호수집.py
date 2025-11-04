import requests
from bs4 import BeautifulSoup

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A1%9C%EB%98%90+%EB%B2%88%ED%98%B8&ackey=re64073b"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발썡
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    lotte_list = []
    lotte_elements = soup.select('div.winning_number > span.ball')
    bonus_elements = soup.select('div.bonus_number > span.ball')
    
    for l in lotte_elements:
        lotte_list.append(l.text)
        
    for b in bonus_elements:
        lotte_list.append(b.text)    
        
    print(lotte_list)
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
    
except Exception as e:
    print(f'An error occured: {e}')        

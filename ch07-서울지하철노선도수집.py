import requests
from bs4 import BeautifulSoup
import urllib.request as req
import os

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

url = 'http://www.seoulmetro.co.kr/kr/cyberStation.do'

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    #. BeautifulSoup 으로 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    subway = soup.select('div.subway-map > svg')
    
    for sw in subway:
        print(sw)
        req.urlretrieve(sw, '지하철노선도.svg')
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
      
except Exception as e:
    print(f'An error occured: {e}')  
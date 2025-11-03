import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

url = 'https://underkg.co.kr/news'

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    #. BeautifulSoup 으로 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #. 데이터를 저장할 리스트 초기화
    title_list = []
    content_list = []
    
    #. 데이터 추출
    title = soup.select('h1.title > a')
    
    for t in title:
        title_list.append(t.text) #. 요소의 내용
        news_url = t.attrs['href'] #. 모든 속성 딕셔너리의 href 키의 값
        
        response_news = requests.get(news_url, headers=headers)
        response_news.raise_for_status #. HTTP 오류 발생시 예외 발생
        soup_news = BeautifulSoup(response_news.text, 'html.parser')
        content = soup_news.select_one('div.read_body')
        content_list.append(content.text.replace("\n", "").strip())
        
    #. Pandas DataFrame 만들기
    chart_df = pd.DataFrame({
        "기사 제목": title_list,
        "기사 내용": content_list
    })
    
    #. 상위 10개
    print(chart_df.head(10))
    
    #. CSV 파일로 저장하는 경우
    #chart_df.to_csv('news-search.csv', index=False, encoding='utf-8-sig')
    
    #. EXCEL 파일로 저장하는 경우
    #now = datetime.now()
    #filename = now.strftime(f'뉴스기사검색_%Y%m%d_%H%M.xlsx')
    #chart_df.to_excel(filename, index=False, engine='openpyxl')

except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
    
except Exception as e:
    print(f'An error occured: {e}')        
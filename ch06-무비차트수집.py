import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

#. 박스오피스
url = 'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&ssc=tab.nx.all&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84&oquery=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94&tqi=jdNzusqVOsVsstJW5qlssssssMw-124645&acq=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94&acr=1&qdt=0&ackey=ookijq85'

#. requests 를 이용해 웹 페이지 HTML 가져오기
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    #. BeautifulSoup 으로 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #. 데이터를 저장할 리스트 초기화
    count_list = []
    title_list = []
    img_list = []
    rank_list = []
    
    #. 무비차트에서 정보 추출
    movies = soup.select('div.list_image_box')
    #print(movies)
    
    movie_rows = soup.select('ul._panel > li')
    #print(movie_rows)
    
    for idx, row in enumerate(movie_rows):        
        count = row.select_one('span.sub_text').get_text(strip=True) if row.select_one('span.sub_text') else 'N/A'
        title = row.select_one('strong.name').get_text(strip=True) if row.select_one('strong.name') else 'N/A'
        img = row.select_one('img').get('src') if row.select_one('img').get('src') else 'N/A'
        count_list.append(count)
        title_list.append(title)
        img_list.append(img)
        rank_list.append(idx + 1)
        
    #. Pandas DataFrame 만들기
    chart_df = pd.DataFrame({
        '순위': rank_list,
        '조회수': count_list,
        '제목': title_list,
        '포스터': img_list,
    })
    
    #. 상위 10개
    print(chart_df.head(10))
    
    #. CSV 피일로 저장하는 경우
    #chart_df.to_csv('movie_chart_top100.csv', index=False, encoding='utf-8-sig')
    
    #. EXCEL 파일로 저장하는 경우
    now = datetime.now()
    filename = now.strftime('무비차트_top100_%Y%m%d_%H%M.xlsx')
    chart_df.to_excel(filename, index=False, engine='openpyxl')
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
        
except Exception as e:
    print(f'An error occured: {e}')
    
    
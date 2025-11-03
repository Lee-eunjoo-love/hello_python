import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

#. User-Agent 설정 (멜론 서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

#. 멜론 차트 URL (최근 24시간 TOP 100)
url = "https://www.melon.com/chart/index.htm"

#. requests 를 이용해 웹 페이지 HTML 가져오기
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    #. BeautifulSoup 으로 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #. 데이터를 저장할 리스트 초기화
    rank_list = []
    title_list = []
    artist_list = []
    
    #. 멜론 차트 테이블에서 정보 추출
    #. 순위 정보는 '.rank01' 클래스, 곡명은 '.rank01 a', 아티스트는 '.rank02 a' 클래스 등을 활용
    songs = soup.select('div.wrap_song_info')
    
    #. TOP 100 곡 가져오기
    song_rows = soup.select('tbody > tr')
    print(song_rows)
    
    for row in song_rows:
        rank = row.select_one('.rank').get_text(strip=True) if row.select_one('.rank') else 'N/A'
        title_element = row.select_one('.rank01 a')
        title = title_element.get_text(strip=True) if title_element else 'N/A'
        artist_element = row.select_one('.rank02 a')
        artist = artist_element.get_text(strip=True) if artist_element else 'N/A'
        
        rank_list.append(rank)
        title_list.append(title)
        artist_list.append(artist)
        
    #. Pandas DataFrame 만들기
    chart_df = pd.DataFrame({
        '순위': rank_list,
        '곡명': title_list,
        '가수명': artist_list
    })
    
    #. 상위 10개 출력
    print(chart_df.head(10))
    
    #. CSV 피일로 저장하는 경우
    #. chart_df.to_csv('melon_chart_top100.csv', index=False, encoding='utf-8-sig')
    
    #. EXCEL 파일로 저장하는 경우
    now = datetime.now()
    filename=now.strftime('멜론차트_top100_%Y%m%d_%H%M.xlsx')
    chart_df.to_excel(filename, index=False, engine="openpyxl")
    
except requests.exceptions.RequestException as e:
    print(f"Error during requests to {url}: {e}")
except Exception as e:
    print(f"An error occured: {e}")
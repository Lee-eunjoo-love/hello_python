import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

keyword = input("키워드 입력 >> ")

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

url = f"https://kin.naver.com/search/list.naver?query={keyword}"

try:
    #. 데이터를 저장할 리스트 초기화
    title_list = []
    date_list = []
    
    for page_num in range(1, 11): #. 1 ~ 10 페이지까지 추출
        response = requests.get(f'{url}&page={page_num}', headers=headers)
        response.raise_for_status() #. HTTP 오류 발생시 예외 발생
        
        #. BeautifulSoup 으로 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #. 데이터 추출
        title = soup.select('ul.basic1 a._nclicks\:kin\.txt._searchListTitleAnchor')
        date = soup.select('dd.txt_inline')
        
        for t, d in zip(title, date):
            title_list.append(f'질문: {t.text}')
            date_list.append(f'날짜: {d.text}')
        
    #. Pandas DataFrame 만들기
    chart_df = pd.DataFrame({
        "지식인 질문 제목": title_list,
        "지식인 질문 일자": date_list
    })
        
    #. 상위 10개
    print(chart_df.head(10))
    
    #. CSV 파일로 저장하는 경우
    #chart_df.to_csv(f'kin_naver_{keyword}.csv', index=False, encoding='utf-8-sig')
    
    #. EXCEL 파일로 저장하는 경우
    #now = datetime.now()
    #filename = now.strftime(f'지식인_{keyword}_%Y%m%d_%H%M.xlsx')
    #chart_df.to_excel(filename, index=False, engine='openpyxl')

except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')    
    
except Exception as e:
    print(f'An error occured: {e}')
    
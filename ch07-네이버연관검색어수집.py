import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

keyword = input("키워드 입력 >> ")
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={keyword}&ackey=xqlefgpy'

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    #. BeautifulSoup 으로 HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.select('div.ad_section.section li div.inner')

    #. 데이터를 저장할 리스트 초기화
    title_list = []
    desc_list = []

    for r in result:
        desc = r.select_one('div.desc_wrap a').get_text(strip=True) if r.select_one('div.desc_wrap a') else ""
        titles = r.select('span.lnk_tit')
        span = []
        for span_tag in titles:
            title = span_tag.text
            span.append(title)
            
        title_list.append(span)
        desc_list.append(desc)
    
    #. Pandas DataFrame 만들기
    chart_df = pd.DataFrame({
        "기사제목": title_list,
        "기사요약": desc_list
    })

    #. 상위 10개
    print(chart_df.head(10))
    
    #. CSV 파일로 저장하는 경우
    #chart_df.to_csv(f'naver-search_{keyword}.csv', index=False, encoding='utf-8-sig')
    
    #. EXCEL 파일로 저장하는 겨우
    #now = datetime.now()
    #filename = now.strftime(f'네이버연관검색_{keyword}_%Y%m%d_%H%M.xlsx')
    #chart_df.to_excel(filename, index=False, engine='openpyxl')

except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')

except Exception as e:
    print(f'An error occured: {e}')
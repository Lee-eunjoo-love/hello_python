import requests
from bs4 import BeautifulSoup
from newspaper import Article
import json

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

api_key = ""
url = "https://www.joongang.co.kr/money"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    title_list = soup.select("ul.card_right_list.rank_list h2.headline > a")
    rank_list = soup.select("ul.card_right_list.rank_list em.rank_count")
    #print(rank_list)
    
    #. 전체 기사 리스트
    for rank, title in zip(rank_list, title_list):
        print(f'{rank.text}. {title.text}')
        
    #. 내용 확인 기사 선택 입력
    selected_news_no = int(input("확인할 뉴스(번호)를 입력하세요 >>> "))
    selected_news = title_list[selected_news_no - 1]
    news_title = selected_news.text
    news_link = selected_news.attrs["href"]
    
    #. 기사 본문 수집
    article = Article(news_link, language="ko")
    article.download()
    article.parse()
    news_content = article.text
    
    #. 기사 본문 출력
    #print(news_content)
    
    #. 기사 내용 요약 (가이드: https://api.ncloud-docs.com/docs/clovastudio-summarization)
    if len(news_content) >= 1900:
        news_content = news_content[:1900]
    
    client_api_key=input("CLOVA API키 >>> ")
    
    headers = {
        'Authorization': f'Bearer {client_api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "texts": [
            news_content
        ],
        "autoSentenceSplitter": True,
        "segCount": -1,
        "segMaxSize": 1000,
        "segMinSize": 300,
        "includeAiFilters": False
    }
    
    #response_summary = requests.post('https://clovastudio.stream.ntruss.com/v1/api-tools/summarization/v2', data=json.dumps(data), headers=headers)
    #response_summary.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    #response_summary_dict = json.loads(response_summary.text)
    #print(response_summary_dict)
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')    
    
except Exception as e:
    print(f'An error occured: {e}')    


#. newspaper 모듈(python3)
# pip install newspaper3K
#      : 뉴스 기사를 수집/분석하고 기사 본문의 텍스트와 이미지 추출과 기사 본문의 기자이름, 이메일 등과 같은 불필요한 정보와 불규칙한 문단 구분, 여백 등을 보기 좋게 가공
#. lxml-html-clean 모듈
# pip install lxml-html-clean

#. 기사 요약 결과
#{'status': {'code': '20000', 'message': 'OK'}, 'result': {'text': '- 연일 최고치를 경신하던 코스피에 제동이 걸림\n- 미국발 악재가 한국을 비롯한 아시아 주요 증시의 발목을 잡
#음\n- 코스피가 장 중 한때 3867.81까지 급락함\n- 국내 증시는 전날 뉴욕증시가 AI 빅테크 고평가 논란으로 일제히 하락하며 시장이 열리자마자 큰 폭으로 하락함\n- AI 고평가 논란에 
#불을 지핀 건 골드만삭스와 모건스탠리 등 글로벌 투자은행(IB)임\n- 미국 백악관이 엔비디아의 최신 AI 반도체 ‘블랙웰’의 중국 수출을 막을 거란 입장을 밝히면서 엔비디아 주가도 3.96% 하락함\n- 미국 연방정부의 셧다운 사태가 장기화할 거란 우려도 투자 심리를 얼어붙게 함\n- 달러 대비 원화가치가 하락한 것 역시 국내 증시엔 악재로 작용함\n- 증시 전문가들은  
#이틀 연속 이어진 국내 증시 하락은 단기적 현상에 그칠 것으로 예상함', 'inputTokens': 929}}
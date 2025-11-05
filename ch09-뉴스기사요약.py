import requests
from bs4 import BeautifulSoup
from newspaper import Article

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
    print(news_content)
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')    
    
except Exception as e:
    print(f'An error occured: {e}')    


#. newspaper 모듈(python3)
# pip install newspaper3K
#      : 뉴스 기사를 수집/분석하고 기사 본문의 텍스트와 이미지 추출과 기사 본문의 기자이름, 이메일 등과 같은 불필요한 정보와 불규칙한 문단 구분, 여백 등을 보기 좋게 가공
#. lxml-html-clean 모듈
# pip install lxml-html-clean

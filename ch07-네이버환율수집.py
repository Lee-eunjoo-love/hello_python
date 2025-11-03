import requests
from bs4 import BeautifulSoup
response = requests.get("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(response.text, "html.parser")
price = soup.select("ul#exchangeList span.value")

for p in price:
    print(p.text)
    
    
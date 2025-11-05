import requests
import json

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

api_key = input("API 인증키 >>> ")
city_name = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    #. JSON 문자열 형식에 데이터를 딕셔너리 형식으로 변환
    data_dict = json.loads(response.text)
    
    print(f'도시명: {data_dict['name']}')
    print(f'현재 날씨: {data_dict['weather'][0]['main']}')
    print(f'현재 기온: {round(data_dict['main']['temp'] - 273.15)}도')
    print(f'체감 온도: {round(data_dict['main']['feels_like'] - 273.15)}도')
    print(f'습도: {data_dict['main']['humidity']} %')
    print(f'풍속: {data_dict['wind']['speed']} m/s')
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url}: {e}')
    
except Exception as e:
    print(f'An error occured: {e}')

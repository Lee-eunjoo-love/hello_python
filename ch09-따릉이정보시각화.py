import requests
import json

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

api_key = input("API 인증키 >>> ")

try:
    start_num = input("조회 대상 시작 대여소 번호 >>> ")
    end_num = input("조회 대상 마지막 대여소 번호 >>> ")
    url = f'http://openapi.seoul.go.kr:8088/{api_key}/json/bikeList/{start_num}/{end_num}/'
    
    response = requests.get(url, headers=headers)
    response.raise_for_status() #. HTTP 오류 발생시 예외 발생
    
    data_dict = json.loads(response.text)
    
    #. {'RESULT': {'CODE': 'INFO-000', 'MESSAGE': '정상 처리되었습니다.'}}
    if "RESULT" in data_dict and data_dict["RESULT"]["CODE"] != "INFO-000":
        error_message = data_dict["RESULT"]["MESSAGE"]
        raise Exception(error_message.replace("\n", " "))
    
    for row in data_dict["rentBikeStatus"]["row"]:
        print(f'대여소 이름: {row["stationName"]}')
        print(f'현재 주차 대수: {row["parkingBikeTotCnt"]}')
        print(f'거치율: {row["shared"]} %')
        print(f'위도/경도 좌푯값: {row["stationLatitude"]}/{row["stationLongitude"]}')
        print('---------------------------------------------------')
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url.replace(api_key, "(인증키)")}: {e}')
    
except Exception as e:
    print(f'An error occured: {e}')
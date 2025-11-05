import requests
import json
import pandas as pd
import pydeck as pdk
import os
import platform
import webbrowser

#. User-Agent 설정 (서버가 봇을 차단할 수 있으므로 브라우저 정보 추가)
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}

api_key = input("API 인증키 >>> ")

#. 시각화 대상 데이터를 담을 딕셔너리 정의
bike_dict = {
    "rackTotCnt": [],
    "stationName": [],
    "parkingBikeTotCnt": [],
    "shared": [],
    "latitude": [],
    "longitude": []
}

try:
    page_num = 0
    while True:
        start_num = 1 + 1000 * page_num #. input("조회 대상 시작 대여소 번호 >>> ")
        end_num = 1000 + 1000 * page_num #. input("조회 대상 마지막 대여소 번호 >>> ")
        url = f'http://openapi.seoul.go.kr:8088/{api_key}/json/bikeList/{start_num}/{end_num}/'
        
        response = requests.get(url, headers=headers)
        response.raise_for_status() #. HTTP 오류 발생시 예외 발생
        
        data_dict = json.loads(response.text)
        
        #. 1000 건씩 무한 반복하며 데이터를 가져오다가 조회 데이터가 없으면 반복문 벗어나기
        if "MESSAGE" in data_dict.keys():
            if data_dict["MESSAGE"] == "해당하는 데이터가 없습니다.":
                break
        
        #. {'RESULT': {'CODE': 'INFO-000', 'MESSAGE': '정상 처리되었습니다.'}}
        if "RESULT" in data_dict and data_dict["RESULT"]["CODE"] != "INFO-000":
            error_message = data_dict["RESULT"]["MESSAGE"]
            raise Exception(error_message.replace("\n", " "))
        
        for row in data_dict["rentBikeStatus"]["row"]:
            bike_dict["stationName"].append(row["stationName"]) 
            bike_dict["parkingBikeTotCnt"].append(int(row["parkingBikeTotCnt"])) 
            bike_dict["shared"].append(int(row["shared"])) 
            bike_dict["latitude"].append(float(row["stationLatitude"])) 
            bike_dict["longitude"].append(float(row["stationLongitude"]))
            bike_dict["rackTotCnt"].append(int(row["rackTotCnt"]))
            #. print(f'대여소 이름: {row["stationName"]}')
            #. print(f'현재 주차 대수: {row["parkingBikeTotCnt"]}')
            #. print(f'거치율: {row["shared"]} %')
            #. print(f'위도/경도 좌푯값: {row["stationLatitude"]}/{row["stationLongitude"]}')
            #. print('---------------------------------------------------')
            
        page_num += 1
    
    chart_df = pd.DataFrame(bike_dict)
    #print(chart_df.to_string())
    
    #. Scatter plot 그리기 (거치율(shared)에 따라 색상 및 원크기 조절)
    layer = pdk.Layer(
        "ScatterplotLayer",
        chart_df,
        get_position = ["longitude", "latitude"],
        get_fill_color = ["255 - shared", "255 - shared", "255"],
        get_radius = "60 * shared / 100",
        pickable = True,
    )
        
    #. 서울 데이터의 위도/경도 좌표값 평균 (서울 중심 좌표)
    lat_center = chart_df["latitude"].mean()
    lon_center = chart_df["longitude"].mean()
    
    #. 지도 초기 뷰 설정
    initial_view = pdk.ViewState(latitude=lat_center, longitude=lon_center, zoom=10)
    
    map = pdk.Deck(layers=[layer], initial_view_state=initial_view, tooltip={"text": "대여소: {stationName}\n현재 주차 대수: {parkingBikeTotCnt}"})
    
    #. 지도를 HTML 파일로 저장
    map_to_html_filename = "./seoul_bike.html"
    map.to_html(map_to_html_filename)
    
    #. 자동으로 HTML 파일 열기
    ap = os.path.abspath(map_to_html_filename)
    if platform.system() == "Windows":
        webbrowser.open(f"file:///{ap.replace('\\', '/')}")
    else:
        webbrowser.open(f'file://{ap}')    
    
except requests.exceptions.RequestException as e:
    print(f'Error during requests to {url.replace(api_key, "(인증키)")}: {e}')
    
except Exception as e:
    print(f'An error occured: {e}')
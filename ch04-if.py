score = int(input("점수 입력 >>"))
if score >= 90:
    print("학점: A") #. 조건을 만족하면 들여쓰기된 문장을 인터프리터가 번역
elif 80 <= score < 90:
    print("학점: B")
elif 70 <= score < 80:
    print("학점: C")
else:
    print("학점: F")
    
num = 10
if num >= 5:
    print("Hello") #. Hello
else:
    print("World")
    
if num >= 30:
    print("Hello")
else:
    print("Python") #. Python
    
age = int(input("나이를 입력하세요"))
if 0 <= age < 13: #. 13세 미만이면
    print("어린이 애니메이션 추천")
elif 13 <= age < 19: #. 13세 이상 19세 미만이면
    print("청소년 액션 영화 추천")
elif age >= 19: #. 19세 이상
    print("성인 드라마 추천")
else:
    print("추천 장르 없음")
    
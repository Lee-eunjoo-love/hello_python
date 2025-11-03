num = 1
while num <= 10:
    print(f"Hello World: {num}")
    num = num + 1 #. 조건을 만족하면 들여쓰기된 문장을 인터프리터가 번역
    
while True:
    foo = input("문자열 입력 >>>")
    if foo == "종료":
        break
    elif foo == "":
        print("아무것도 입력하지 않았습니다. 다시 입력해주세요.")
        continue
    print(f"현재 입력된 문자열의 글자 수는 {len(foo)}개입니다")

x = 0
while x < 5:
    x += 1
    if x == 2:
        continue    
    if x == 4:
        break    
    print(f"{x} -> ") 
    #. 1 -> 
    #. 3 ->
    
username = "user"
password = "pass123"
attempt_count = 0
while attempt_count < 3:
    input_username = input("사용자명:")
    input_password = input("비밀번호:")
    if username == input_username and password == input_password:
        print('로그인 성공')
        attempt_count = 0
        break
    else:
        print("로그인 실패. 다시 시도해 주세요.")
        attempt_count += 1
        
if attempt_count == 3:
    print("로그인 시도 횟수 초과: 관리자에게 문의 바랍니다.")            
        
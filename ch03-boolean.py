#. Boolean : True 또는 False 가 어떤 기호로도 둘러싸여 있지 않으면 불 자료형으로 인식하며 첫글자는 반드시 대문자.
find=""
print(find == "OK")
success="FAIL"
print(success == "SUCCESS")
is_good="GOOD"
print(is_good == "GOOD")

num1 = 20
num2 = 10
print(num1 >= 20 and num2 <= 30) #. True
print(num1 == 20 or num2 == 5) #. True
print(not num1 == 20) #. False

print("---------- 라이브 콘서트 입장 가능 여부 확인 ----------")
age = int(input("나이를 입력하세요"))
is_ticket = input("일반 티켓을 소지하고 있습니까? (Y/N)")
is_vip = input("VIP 티켓을 소지하고 있습니까? (Y/N)")
color = input("옷 색깔을 입력하세요. (BLACK/RED/BLUE/GREEN)")
print(f"입장 가능 여부: {is_vip == "Y" or age >= 18 and is_ticket == "Y" and color == "BLUE"}")
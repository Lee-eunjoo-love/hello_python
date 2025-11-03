for word in ["사과", "포도", "오렌지"]:
    if word == "포도":
        continue #. 사과, 오렌지
    print(word)
    
sum = 0
for i in range(11): #. range(n) : 0 ~ n-1 까지 범위의 숫자 리스트 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum += i
    
print(f'1 ~ 10 까지 합 = {sum}') #. 1 ~ 10 까지 합 = 55

menu = ["짜장면", "짬뽕", "탕수육"]
price = [6000, 7000, 20000]
for i in range(len(menu)):
    print(f"{menu[i]}: {price[i]}")
    
#. zip() : 여러 리스트를 병력적으로 처리
for a, b in zip(menu, price):
    print(f"{a}: {b}")
    
#. enumerate(리스트): 리스트의 인덱스와 함께 원소 처리시 사용
name_list = ["철수", "영희", "영수", "옥순"]
for i, item in enumerate(name_list):
    print(f"{i + 1}등: {item}")
    
animal_list = ["강아지", "고양이'"]    
sound_list = ["멍멍", "야옹"]
for animal, sound in zip(animal_list, sound_list):
    print(f"{animal}: {sound}")
    
count = int(input("숫자 입력 >>>"))
for i in range(count):
    n = i + 1
    j = 1
    print_list = ""
    while j <= n:
        print_list = f'{print_list} {n}'
        j += 1
    print(print_list)
    
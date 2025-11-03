print("강아지가 '멍멍' 짓는다")
print('강아지가 "멍멍" 짓는다')
print("""그는
'안녕'이라고
인사한다""")
print('''그는
"""안녕"""이라고
인사한다''')
print("난\n파이썬이\n좋아")
print("난\t파이썬이\t좋아")
print("I\tLOVE\tPYTHON")
print("난\\파이썬이\\좋아")
print("난\"파이썬이\"좋아")
print("난\'파이썬이\'좋아")
print("난 파이썬이 좋아\b\b")
print("난 파이썬이 좋아\rHello World")

string1 = "Hello"
string2 = "World"
print(string1 + string2)
print(string1 * 10)

string1 = "10"
string2 = "20"
print(string1 + string2)
print(string1 * 10)

foo = "Hello World"
print("Hello" in foo)
print("Python" in foo)
print("Hello" not in foo)
print("Python" not in foo)
print(len(foo))
print(foo.upper(), foo.lower())

print(foo.count("l"))
split = "/"
print(split.join(foo))
print(foo.strip())
print(foo.replace("World", "Python"))

print(foo.split(" "))
print(f"문자열 \'{foo}\'의 길이는 {len(foo)}입니다.")

print("오늘 점심 메뉴는 \r\"돈가스\"")
string1 = "제주도 여행에서 파스타 맛집을 찾아갔어요. 제주도 맛집 추천!"
print(string1.replace("제주도", "#제주도").replace("맛집", "#맛집"))